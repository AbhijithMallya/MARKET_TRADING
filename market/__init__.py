from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


#   package      instance

# initialising Flask instance
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='6a839465be0f7fc883b3aea9'

#uri -->Uniform Resource Identifier
# db --> database instance
db = SQLAlchemy(app)
#database --> SQLLite3

bcrypt=Bcrypt(app)




from market import routes   

