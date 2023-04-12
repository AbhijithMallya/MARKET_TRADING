from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html' )


@app.route('/market')
def market_page():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    




@app.route('/login')
def login_page():
    return render_template('base.html')

# if __name__ =='__main__':
#     app.debug=True
#     url = 'http://127.0.0.1:5000'
#     webbrowser.open(url)
#     app.run()