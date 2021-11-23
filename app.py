from flask import Flask, render_template, request, url_for, session, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2.extras
import psycopg2
from PharmacyMission import PharmacyMission
from PharmacyStaff import PharmacyStaff
from User import User

app = Flask(__name__)
app.secret_key = "Aspehli1"
app.register_blueprint(PharmacyMission, url_prefix="/Pharmacy_Admin")
app.register_blueprint(PharmacyStaff, url_prefix="/PharmacyStaff")
app.register_blueprint(User, url_prefix="/User")

DB_HOST = "localhost"
DB_NAME = "IlacSepeti"
DB_USER = "postgres"
DB_PASS = "selimyucu03"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

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

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == "POST":
        if request.form.get("EczanePanel"):
            return redirect(url_for('PharmacyWelcomePage'))
        elif request.form.get("WelcomePage"):
            return redirect(url_for('WelcomePage'))
        elif request.form.get("PharmacistStaff"):
            return redirect(url_for('PharmacistStaff'))
    return render_template('index.html')

@app.route('/WelcomePage')
def WelcomePage():
    return render_template('WelcomePage.html')
@app.route('/EczanePanel')
def PharmacyWelcomePage():
    return render_template('PharmacyWelcomePage.html')
@app.route('/PharmacistStaff')
def PharmacistStaff():
    return render_template('PharmacistStaff.html')


@app.route('/Add_Pharm', methods=['POST', 'GET'])
def add_pharmacy():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        tc = request.form['tc']
        name = request.form['name']
        phone = request.form['phone']
        pswd = request.form['pswd']
        email = request.form['email']
        if name == '' or tc == '' or phone == '' or email == '' or pswd == '':
            return render_template('PharmacyWelcomePage.html', message='Lütfen gerekli alanı doldurunuz')
        else:
            cur.execute('SELECT tcno FROM eczaci WHERE tcno=%s' % (tc))
            dataTc = cur.fetchall()
            if len(dataTc) > 0:
                flash('Girilen Tc Numarası Zaten Mevcut')
            else:             
                cur.execute("INSERT INTO eczaci (tcNo, isim, telefon, adminparola, email) VALUES (%s,%s,%s,%s,%s)",
                            (tc, name, phone, pswd, email))
                conn.commit()
            return render_template('PharmacistAdmin.html')
    return redirect(url_for('PharmacyWelcomePage'))


@app.route('/LogIn_Pharm_Admin', methods=['POST', 'GET'])
def LogIn_Pharm():
    if request.method == 'POST':
        tc = request.form['tc']
        password = request.form['pswd']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * from eczaci WHERE tcno = %s" % (tc))
        account = cur.fetchone()
        print(account)
        if account:
            password_rs = account['adminparola']
            if password_rs == password:
                return render_template('PharmacistAdmin.html')
            else:
                flash('Yanlış TcNo veya kullanıcı adı')
        else:
            flash('Yanlış TcNo veya kullanıcı adı')
        return redirect(url_for('PharmacyWelcomePage'))

@app.route('/Login_Pharmacy_Staff', methods=['POST'])
def Login_Pharmacy_Staff():
    if request.method == 'POST':
        tc = request.form['tcno']
        id = request.form['id']
        status = request.form['status']
        password = request.form['pswd']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(
            "SELECT * from eczanecalisani WHERE eczane_id = %s and tcno = %s and status=%s" % (id, tc ,status))
        account = cur.fetchone()
        print(account)
        if account:
            password_rs = account['sifre']
            if password_rs == password:
                return render_template('PharmacyStaff/PharmacyStaffMission.html')
            else:
                flash('Yanlış TcNo veya kullanıcı adı')
        else:
            flash('Yanlış TcNo veya kullanıcı adı')
    return redirect(url_for('PharmacistStaff'))


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
            cur.execute(
                'SELECT DISTINCT * FROM kullanici WHERE tcno=%s' % (tc))
            user = cur.fetchall()
            if len(user) > 0:
                flash('%s TC numaralı kullanıcı zaten mevcut'% (tc))
            else:
                cur.execute("INSERT INTO kullanici (tcNo, isim, telefon, email ,sifre) VALUES (%s,%s,%s,%s,%s)",
                            (tc, name, phone, email, pswd))
                conn.commit()
                return render_template('UserMainPage.html')
    return redirect(url_for('WelcomePage'))


@app.route('/Login_User', methods=['POST'])
def Login_User():
    if request.method == 'POST':
        tc = request.form['tc']
        password = request.form['pswd']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * from kullanici WHERE tcno = %s" % (tc))
        account = cur.fetchone()
        print(account)
        if account:
            password_rs = account['sifre']
            if password_rs == password:
                return render_template('UserMainPage.html')
            else:
                flash('Yanlış TcNo veya kullanıcı adı')
        else:
            flash('Yanlış TcNo veya kullanıcı adı')
    return redirect(url_for('WelcomePage'))

if __name__ == '__main__':
    app.debug =True
    app.run()