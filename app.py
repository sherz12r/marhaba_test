from flask import Flask, request, render_template, jsonify
from typing import List, Dict

app = Flask(__name__)

# Function to apply VAT dynamically based on the rules
def apply_vat(transaction: Dict, vat_rate: float) -> float:
    """
    Applies VAT to the transaction based on the category and provided VAT rate.
    """
    amount = transaction['amount']
    transaction_type = transaction['type']
    category = transaction['category']

    # Apply VAT only to 'goods' and 'services' categories
    if category in ['goods', 'services']:
        if transaction_type == 'credit':
            # Subtract VAT for credit transactions (goods or services)
            return amount * (1 - vat_rate)
        elif transaction_type == 'debit':
            # Add VAT for debit transactions (goods or services)
            return amount * (1 + vat_rate)
    # No VAT applied for 'investment'
    return amount  # No VAT for 'investment' category

def calculate_compound_interest(balance: float, years: int, interest_rate: float) -> float:
    """
    Calculates the compound interest on a balance, if the balance is positive.
    """
    if balance > 0:
        return balance * (1 + interest_rate) ** years  # Compound interest formula
    return balance  # No interest if the balance is zero or negative

def process_transactions(transactions: List[Dict], years: int, interest_rate: float, vat_rate: float) -> Dict:
    """
    Processes transactions, applies VAT, calculates net balance, and computes compound interest.
    Returns the breakdown by category and final balance with interest.
    """
    if years <= 0:
        raise ValueError("Years must be a positive integer greater than zero.")
    
    total_balance = 0
    category_totals = {'goods': 0, 'services': 0, 'investment': 0}
    
    # Process each transaction
    for transaction in transactions:
        if transaction['category'] not in category_totals:
            raise ValueError(f"Invalid category: {transaction['category']}")
        
        adjusted_amount = apply_vat(transaction, vat_rate)  # Apply VAT
        
        if transaction['type'] == 'debit':
            # For debit transactions, subtract from total balance
            total_balance -= adjusted_amount
        else:
            # For credit transactions, add to total balance
            total_balance += adjusted_amount
        
        # Update category totals (with VAT applied)
        category_totals[transaction['category']] += adjusted_amount
    
    # Calculate compound interest if the net balance is positive
    final_balance = calculate_compound_interest(total_balance, years, interest_rate)
    
    # Prepare the result
    result = {
        'net_balance_before_interest': total_balance,
        'final_balance_with_interest': final_balance,
        'category_breakdown': category_totals
    }
    
    return result

@app.route('/')
def index():
    """Render the frontend input form."""
    return render_template('index.html')

@app.route('/process-transactions', methods=['POST'])
def process_transactions_endpoint():
    """
    Flask endpoint to process transactions sent via POST request.
    Expects a JSON body with the transaction list, years, interest rate, and VAT rate.
    """
    try:
        data = request.get_json()  # Get JSON data from the request
        transactions = data.get('transactions')  # List of transactions
        years = data.get('years', 0)  # Number of years for interest calculation
        interest_rate = data.get('interestRate', 0.05)  # Interest rate
        vat_rate = data.get('vatRate', 0.05)  # VAT rate
        
        if not transactions:
            return jsonify({'error': 'No transactions provided'}), 400
        
        if years <= 0:
            return jsonify({'error': 'Years must be a positive integer greater than zero'}), 400
        
        result = process_transactions(transactions, years, interest_rate, vat_rate)  # Process the transactions
        return jsonify(result)  # Return the result as JSON
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
