from dotenv import load_dotenv
from flask import Flask
from database import Database
import psycopg2.extras

app = Flask(__name__)
load_dotenv()
app.config['db']=Database()



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!', 200

@app.get('/top<int:n>')
def get_TopN(n: int):
    if n < 1 or n > 100:
        return {"erreur": "nombre invalide"}, 400
    curseur = app.config['db'].connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curseur.execute('''SELECT c.* 
    from louis_v005.crawl c
    inner join louis_v005.score s on c.id = s.entity_id
    order by s.score desc LIMIT '''+str(n))
    return [dict(row) for row in curseur.fetchall()], 200

if __name__ == '__main__':
    app.run()

