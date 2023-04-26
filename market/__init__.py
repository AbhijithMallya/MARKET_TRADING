from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#   package      instance

# initialising Flask instance
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='6a839465be0f7fc883b3aea9'

#uri -->Uniform Resource Identifier
# db --> database instance
db = SQLAlchemy(app)
#database --> SQLLite3




from market import routes   

