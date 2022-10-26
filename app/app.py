from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
app = Flask(__name__)

dialect = "postgresql"
username = "postgres"
password = os.environ.get('HOUSING_DB_PW')
host = "dlovettdb.cqmsika5khyc.us-east-2.rds.amazonaws.com"
port = "5432"
database = "housing"
database_uri = f"{dialect}://{username}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

@app.route("/")
def home():
    # engine.execute('SELECT * FROM housing_pri')
    with engine.connect() as conn:
        df = pd.read_sql('price_index', conn)
        html = df.to_html()
    return html

if __name__ == "__main__":
    app.run()