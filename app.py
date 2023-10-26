from dotenv import load_dotenv
from flask import Flask
from database import Database

app = Flask(__name__)
load_dotenv()
app.config['db']=Database()



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

