from flask import Flask, render_template
import os, random, pyodbc

app = Flask(__name__)

server = 'quote-webapp-db-srv.database.windows.net'
database = 'quotes'
username = 'ffhsroot'
password = 'Welcome$24'
driver = '{ODBC Driver 18 for SQL Server}'

def get_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM quotes')
    count = cursor.fetchone()[0]
    if count > 0:
        random_id = random.randint(1, count)
        cursor.execute('SELECT id, quote, author FROM quotes WHERE id = ?', (random_id,))
        quote_data = cursor.fetchone()
        if quote_data:
            return render_template('quote.html', quote=quote_data[1], author=quote_data[2])
        else:
            return "Quote not found", 404
    else:
        return "No quotes found", 404

if __name__ == '__main__':
    app.run()
