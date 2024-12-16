from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask App
app = Flask(__name__)

# Database Configuration - Using SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # SQLite Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warnings
db = SQLAlchemy(app)

# Define Database Model (Item Table)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Name of the item
    description = db.Column(db.String(200), nullable=False)  # Item description

    def __repr__(self):
        return f'Item {self.id}: {self.name}'


# Create the Database Tables (if they don't already exist)
with app.app_context():
    db.create_all()

# ---------- ROUTES ----------

# 1. Home Page - List all items
@app.route('/')
def index():
    items = Item.query.all()  # Fetch all items from database
    return render_template('index.html', items=items)

# 2. Add Item - Show Form and Handle POST Request
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)  # Create a new Item object
        db.session.add(new_item)  # Add item to database session
        db.session.commit()  # Commit transaction
        return redirect(url_for('index'))  # Redirect to home page
    return render_template('add.html')

# 3. Update Item - Show Form and Handle POST Request
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)  # Get the item by ID or return 404
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()  # Save changes to database
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

# 4. Delete Item
@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)  # Find the item by ID
    db.session.delete(item)  # Delete item
    db.session.commit()  # Commit transaction
    return redirect(url_for('index'))

# Run the Flask Application explicitly on port 5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Host '0.0.0.0' allows external access

