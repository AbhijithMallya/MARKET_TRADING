from market import app
from flask import render_template , redirect , url_for, flash,get_flashed_messages
from market.models import Item,User
from market.forms import RegisterForm
from market import db



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

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User( username=form.username.data,
                              email_address = form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors!={} : #If no errors from validations
        for err_msg in form.errors.values():
            flash('Error Message : {}'.format(err_msg),category='danger')



    return render_template('register.html',form=form)
    




@app.route('/login')
def login_page():
    return render_template('base.html')

# if __name__ =='__main__':
#     app.debug=True
#     url = 'http://127.0.0.1:5000'
#     webbrowser.open(url)
#     app.run()