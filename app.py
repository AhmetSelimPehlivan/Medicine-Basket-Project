from flask import Flask, render_template, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2.extras
import psycopg2

app = Flask(__name__)

DB_HOST = "localhost"
DB_Name = "IlacSepeti"
DB_USER = "postgres"
DB_PASS = "selimyucu03"

conn = psycopg2.connect(dbname=DB_Name, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def index():
    return render_template('index.html')

ENV = 'dev'
    
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:selimyucu03@localhost/IlacSepeti'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/WelcomePage', methods=['POST', 'GET'])
def WelcomePage():
    return render_template('WelcomePage.html', message='Lütfen gerekli alanı doldurunuz')

@app.route('/EczanePanel', methods=['POST', 'GET'])
def pharmacySignIn():
    return render_template('PharmacySignIn.html', message='Lütfen gerekli alanı doldurunuz')


@app.route('/IlacDepoPanel', methods=['POST', 'GET'])
def PharmacyWHSignIn():
   # if request.method == 'POST':
    #   fname = request.form['fname']
    #    lname = request.form['lname']
   #     tc = request.form['tc']
  #      password = request.form['password']
 #       print(fname,lname)
    #        if fname == '' or lname == '' or tc == '' or password == '':
    return render_template('PharmacyWHSignIn.html', message='Lütfen gerekli alanı doldurunuz')
#        return render_template('GetMedicine.html')

@app.route('/add_User', methods=['POST'])
def add_User():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        tc = request.form['tc']
        phone = request.form['phone']
        email = request.form['email']
        pswd = request.form['pswd']
        if name == '' or tc == '' or phone == '' or email == '' or pswd == '':
            return render_template('PharmacySignIn.html', message='Lütfen gerekli alanı doldurunuz')
        else:
            cur.execute("INSERT INTO kullanici (tcNo, isim, telefon, email ,sifre) VALUES (%s,%s,%s,%s,%s)", (tc, name, phone, email, pswd))
            conn.commit()
            return render_template('UserMainPage.html')


@app.route('/Login_User', methods=['POST'])
def Login_User():
    if request.method == 'POST':
        tc = request.form['tc']
        password = request.form['pswd']
       
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * from kullanici WHERE tcno = %s" % tc)
        account = cur.fetchone()
        print(account)
        if account:
            password_rs = account['sifre']
            if password_rs == password:
                return render_template('UserMainPage.html')
            else:
                flash('Incorrect username/password')
        else:
            flash('Incorrect username/password')
            
if __name__ == '__main__':
    app.debug =True
    app.run()