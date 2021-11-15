from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('WelcomePage.html')

ENV = 'dev'
    
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:selimyucu03@localhost/IlacSepeti'
else: 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Eczane(db.Model):
    __tablename__= 'Eczane'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), primary_key=False)
    address = db.Column(db.Text(), primary_key=False)
    city = db.Column(db.String(25), primary_key=False)
    committee = db.Column(db.Integer, primary_key=False) 
    workhours = db.Column(db.Date, primary_key=False)
    
    def __init__(self, id, name, address, city, committee, workhours):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.committee = committee
        self.workhours = workhours

@app.route('/GetMedicine.html', methods=['POST'])
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

if __name__ == '__main__':
    app.debug =True
    app.run()