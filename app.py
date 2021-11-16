from flask import Flask, render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "localhost"
DB_Name = "IlacSepeti"
DB_USER = "postgres"
DB_PASS = "selimyucu03"
conn = psycopg2.connect(dbname=DB_Name, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)
@app.route('/')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM ilac"
    cur.execute(s)
    list_users = cur.fetchall() 
    return render_template('WelcomePage.html', list_users=list_users)

ENV = 'dev'
    
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:selimyucu03@localhost/IlacSepeti'
else: 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/GetMedicine.html', methods=['POST', 'GET'])
def WelcomePage():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        tc = request.form['tc']
        password = request.form['password']
        print(fname,lname)
        if fname == '' or lname == '' or tc == '' or password == '':
            return render_template('WelcomePage.html', message='Lütfen gerekli alanı doldurunuz')
        return render_template('GetMedicine.html')


@app.route('/add_User', methods=['POST'])
def add_User():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        tc = request.form['tc']
        phone = request.form['phone']
        email = request.form['email']
        pswd = request.form['pswd']
        cur.execute("INSERT INTO kullanici (tcNo, isim, telefon, email ,sifre) VALUES (%s,%s,%s,%s,%s)", (tc, name, phone, email, pswd))
        conn.commit()
        flash('User Added successfully')
        return render_template('GetMedicine.html')
if __name__ == '__main__':
    app.debug =True
    app.run()