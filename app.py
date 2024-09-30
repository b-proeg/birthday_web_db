from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_birthday_list():
    try:
        conn = sqlite3.connect('bd.bd')
        cursor = conn.cursor()
        cursor.execute('SELECT first_name, last_name, date, username FROM birthdays')
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@app.route('/')
def index():
    birthday_list = get_birthday_list()
    return render_template('birthday_list.html', birthday_list=birthday_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
