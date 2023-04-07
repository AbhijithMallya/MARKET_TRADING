from flask import Flask, render_template
import webbrowser
from flask_sqlalchemy import SQLAlchemy
#   package      instance

# initialising Flask instance
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#uri -->Uniform Resource Identifier
# db --> database instance
db = SQLAlchemy(app)
#database --> SQLLite3




from market import routes   

