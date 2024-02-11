# Import necessary modules from Flask
from flask import Flask, render_template, redirect, url_for, request

# Import the inventory_dict from the 'inventory' module
from inventory import inventory_dict

# Create a Flask web application instance
app = Flask(__name__)

# Initialize user_dict with the content of inventory_dict
user_dict = inventory_dict

# Initialize an empty cart as a global variable
cart = {}

# Route to render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add items to the cart based on the POST request
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Extract item details from the form submission
    item_name = request.form.get('item_name')
    item_quantity = int(request.form.get('item_quantity'))
    item_price = float(request.form.get('item_price'))
    
    # Check if the item is already in the cart, if so, update the quantity; otherwise, add it to the cart
    if item_name in cart:
        cart[item_name]['quantity'] += item_quantity
    else:
        cart[item_name] = {'quantity': item_quantity, 'price': item_price}

    # Redirect back to the index page after adding to the cart
    return redirect(url_for('index'))

# Route to delete selected items from the cart based on the POST request
@app.route('/delete_items', methods=['POST'])
def delete_items():
    # Extract selected items from the form submission
    selected_items = request.form.getlist('selected_items')

    # Remove selected items from the cart
    for item_name in selected_items:
        if item_name in cart:
            del cart[item_name]

    # Redirect back to the view_cart page after deleting items
    return redirect(url_for('view_cart'))

# Route to display the contents of the cart
@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart, total_price=calculate_total_price(cart))

# Function to calculate the total price of items in the cart
def calculate_total_price(cart):
    total_price = sum(data['quantity'] * data['price'] for data in cart.values())
    return '{:.2f}'.format(total_price)

# Route to handle login functionality (dummy implementation)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # If the request method is POST, redirect to the index page (dummy implementation)
    if request.method == 'POST':
        return redirect(url_for('index'))

    # Render the login page for GET requests
    return render_template('login.html')

# Route to handle user registration (dummy implementation)
@app.route('/login/register/', methods=['GET', 'POST'])
def register():
    # If the request method is POST, process user registration and redirect to the index page (dummy implementation)
    if request.method == 'POST':
        user_id = len(user_dict) + 1
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        user_dict[user_id] = [email, name, password]
        return redirect(url_for('index'))

    # Render the registration page for GET requests
    return render_template('register.html')

# Route to display the user database (dummy implementation)
@app.route("/user_database")
def user_database():
    return render_template("database.html", inventory_dict=user_dict)

# Run the Flask app in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
