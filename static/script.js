document.addEventListener('DOMContentLoaded', function() {
    let transactionCount = 0;

    // Add a new transaction input form when the "Add Transaction" button is clicked
    document.getElementById('addTransactionButton').addEventListener('click', function() {
        transactionCount++;

        // Create new input fields for the transaction
        const transactionDiv = document.createElement('div');
        transactionDiv.classList.add('transaction');
        transactionDiv.innerHTML = `
            <h3>Transaction ${transactionCount}</h3>
            <label for="amount${transactionCount}">Amount (AED):</label><br>
            <input type="number" id="amount${transactionCount}" name="amount" required><br><br>
            
            <label for="vat${transactionCount}">VAT (AED):</label><br>
            <input type="number" id="vat${transactionCount}" name="vat" required><br><br>

            <label for="type${transactionCount}">Type:</label><br>
            <select id="type${transactionCount}" name="type" required>
                <option value="credit">Credit</option>
                <option value="debit">Debit</option>
            </select><br><br>

            <label for="category${transactionCount}">Category:</label><br>
            <select id="category${transactionCount}" name="category" required>
                <option value="goods">Goods</option>
                <option value="services">Services</option>
                <option value="investment">Investment</option>
            </select><br><br>
        `;
        
        document.getElementById('transactionFields').appendChild(transactionDiv);
    });

    // When the form is submitted, gather all the data
    document.getElementById('transactionForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const transactions = [];
        const transactionElements = document.querySelectorAll('.transaction');
        
        // Gather each transaction's data
        transactionElements.forEach(function(transactionElement) {
            const amount = parseFloat(transactionElement.querySelector('[name="amount"]').value);
            const vat = parseFloat(transactionElement.querySelector('[name="vat"]').value);
            const type = transactionElement.querySelector('[name="type"]').value;
            const category = transactionElement.querySelector('[name="category"]').value;
            
            transactions.push({ amount, vat, type, category });
        });

        // Get the number of years, interest rate, and VAT rate
        const years = parseInt(document.getElementById('years').value, 10);
        const interestRate = parseFloat(document.getElementById('interestRate').value) / 100;
        const vatRate = parseFloat(document.getElementById('vatRate').value) / 100;

        // Send data to the backend using Fetch API
        fetch('/process-transactions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ transactions, years, interestRate, vatRate })
        })
        .then(response => response.json())
        .then(data => {
            // Display results
            if (data.error) {
                alert('Error: ' + data.error);
            } else {
                document.getElementById('result').style.display = 'block';
                document.getElementById('net_balance').innerText = data.net_balance_before_interest;
                document.getElementById('final_balance').innerText = data.final_balance_with_interest;

                const categoryList = document.getElementById('category_breakdown');
                categoryList.innerHTML = '';
                for (const category in data.category_breakdown) {
                    const li = document.createElement('li');
                    li.innerText = `${category}: ${data.category_breakdown[category]}`;
                    categoryList.appendChild(li);
                }
            }
        })
        .catch(error => alert('Error: ' + error));
    });
});
