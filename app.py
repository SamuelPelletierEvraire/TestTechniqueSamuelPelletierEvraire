from dotenv import load_dotenv
from flask import Flask
from database import Database
import psycopg2.extras

app = Flask(__name__)
load_dotenv()
app.config['db']=Database()



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.get('/top<int:n>')
def get_TopN(n: int):
    if n < 1 or n > 100:
        return {"erreur": "nombre invalide"}
    curseur = app.config['db'].connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curseur.execute('SELECT * from louis_v005.crawl LIMIT '+str(n))
    return [dict(row) for row in curseur.fetchall()]

if __name__ == '__main__':
    app.run()

