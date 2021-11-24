import psycopg2.extras
import psycopg2
from flask import (Blueprint, redirect, render_template, request, flash, url_for)
from flask import Blueprint, render_template

PharmacyStaff = Blueprint("PharmacyStaff", __name__,
                            static_folder="static", template_folder="templates")
DB_HOST = "localhost"
DB_NAME = "IlacSepeti"
DB_USER = "postgres"
DB_PASS = "selimyucu03"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


@PharmacyStaff.route('/PharmacyActions', methods=['POST', 'GET'])
def PharmacyActions():
    if request.method == "POST":
        if request.form.get("submit_problemList"):
            return redirect(url_for('PharmacyStaff.PharmacyProblemList'))
        elif request.form.get("submit_problemMudahale"):
            return redirect(url_for('PharmacyStaff.ProblemMudahaleIndex'))
        elif request.form.get("submit_PharmList"):
            return redirect(url_for('PharmacyStaff.PharmacyStockList'))
    return render_template('PharmacyStaff/PharmacyStaffMission.html')


@PharmacyStaff.route('/EmployeeActions', methods=['POST', 'GET'])
def EmployeeActions():
    if request.method == "POST":
        if request.form.get("ProblemList"):
            return redirect(url_for('PharmacyStaff.problemlist'))
        elif request.form.get("ilacEkle"):
            return redirect(url_for('PharmacyStaff.addilac'))
    return render_template('PharmacyStaff/PharmacyStaffMission.html')


@PharmacyStaff.route('/problemlist')
def problemlist():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problem")
    list_users = cur.fetchall()
    return render_template('PharmacyEmployee/employeelist.html', temp=list_users)


@PharmacyStaff.route('/addilac')
def addilac():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    eczane_id = request.form['eczane_id']
    ilacadi = request.form['ilacadi']
    cur.execute("INSERT INTO eczaneilacbulunur (eczane_id, ilacadi) VALUES (%s,%s)",
                (eczane_id, ilacadi))
    conn.commit()
    list_users = cur.fetchall()
    return render_template('PharmacyEmployee/ilaclist.html', temp=list_users)


@PharmacyStaff.route('/PharmacyProblemList')
def PharmacyProblemList():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problem")
    list_users = cur.fetchall()
    return render_template('Pharmacy/ProblemList/PharmacyProblemList.html', temp=list_users)

@PharmacyStaff.route('/PharmacyStockList')
def PharmacyStockList():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM eczaneilacbulunur")
    list_users = cur.fetchall()
    return render_template('Pharmacy/EnvanterList/PharmacyStockList.html', temp=list_users)


@PharmacyStaff.route('/ProblemMudahaleIndex', methods=['POST', 'GET'])
def ProblemMudahaleIndex():
    if request.method == "POST":
        if request.form.get("ProblemMudahale"):
            return redirect(url_for('PharmacyStaff.ProblemMudahale'))
        elif request.form.get("ProblemCikti"):
            return redirect(url_for('PharmacyStaff.ProblemCikti'))
        elif request.form.get("IlaveMudahaleDetay"):
            return redirect(url_for('PharmacyStaff.IlaveMudahaleDetay'))
        elif request.form.get("IlaveCiktiDetay"):
            return redirect(url_for('PharmacyStaff.IlaveCiktiDetay'))
        elif request.form.get("PersonelProblem"):
            return redirect(url_for('PharmacyStaff.PersonelProblem'))
        elif request.form.get("ProblemCiktiDegerlendirme"):
            return redirect(url_for('PharmacyStaff.ProblemCiktiDegerlendirme'))
        elif request.form.get("ProblemDurumDegerlendirme"):
            return redirect(url_for('PharmacyStaff.ProblemDurumDegerlendirme'))
    return render_template('PharmacyStaff/Problem/ProblemList.html')



@PharmacyStaff.route('/ProblemMudahale')
def ProblemMudahale():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM ProblemMudahale")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/ProblemMudahale/ProblemMudahaleList.html', list_users=list_users)


@PharmacyStaff.route('/ProblemCikti')
def ProblemCikti():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problemcikti")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/ProblemCikti/ProblemCiktiList.html', list_users=list_users)


@PharmacyStaff.route('/IlaveMudahaleDetay')
def IlaveMudahaleDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM ProblemMudahale")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/IlaveMudahaleDetay/IlaveMudahaleDetayList.html', list_users=list_users)


@PharmacyStaff.route('/IlaveCiktiDetay')
def IlaveCiktiDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problemcikti")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/IlaveCiktiDetay/IlaveCiktiDetayList.html', list_users=list_users)

@PharmacyStaff.route('/PersonelProblem')
def PersonelProblem():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM PersonelProblem")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/PersonelProblem/PersonelProblemList.html', list_users=list_users)


@PharmacyStaff.route('/ProblemCiktiDegerlendirme')
def ProblemCiktiDegerlendirme():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        "SELECT P.problemid, B.belirtecID FROM problembirim AS P, belirtecler AS B")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/ProblemCiktiDegerlendirme/ProblemCiktiDegerlendirmeList.html', list_users=list_users)


@PharmacyStaff.route('/ProblemDurumDegerlendirme')
def ProblemDurumDegerlendirme():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problemdurumdegerlendirme")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/ProblemDurumDegerlendirme/ProblemDurumDegerlendirmeList.html', list_users=list_users)

@PharmacyStaff.route('/template/ProblemTemplate', methods=['POST'])
def add_ProblemTemplate():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        if request.form.get("ProblemMudahale"):
            print("sdsd")
            alanID = request.form['alanID']
            sinifID = request.form['sinifID']
            mudahaleID = request.form['mudahaleID']
            problemID = request.form['problemID']
            cur.execute(
                'SELECT DISTINCT * FROM problemmudahale WHERE alanid=%s and sinifid=%s and mudahaleid=%s and problemid=%s' % (alanID, sinifID, mudahaleID, problemID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/ProblemMudahale/ProblemMudahaleList.html')
            cur.execute("INSERT INTO problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (%s,%s,%s,%s)",
                        (alanID, sinifID, mudahaleID, problemID))
            conn.commit()
            return redirect(url_for('PharmacyStaff.ProblemMudahale'))
        elif request.form.get("ProblemCikti"):
            alanID = request.form['alanID']
            sinifID = request.form['sinifID']
            ciktiID = request.form['ciktiID']
            problemID = request.form['problemID']
            cur.execute(
                'SELECT DISTINCT * FROM problemcikti WHERE alanid=%s and sinifid=%s and ciktiid=%s and problemid=%s' % (alanID, sinifID, ciktiID, problemID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Sinif/SinifList.html')
            cur.execute("INSERT INTO problemcikti (alanid, sinifid, ciktiid, problemid) VALUES (%s,%s,%s,%s)",
                        (alanID, sinifID, ciktiID, problemID))
            conn.commit()
            return redirect(url_for('PharmacyStaff.ProblemCikti'))
        elif request.form.get("PersonelProblem"):
            ProblemID = request.form['ProblemID']
            tcno = request.form['tcno']
            cur.execute(
                'SELECT DISTINCT * FROM PersonelProblem WHERE ProblemID=%s and KullaniciAdi=%s' , (ProblemID,tcno))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template(
                    'PharmacyStaff/Problem/PersonelProblem/PersonelProblemList.html')
            cur.execute("INSERT INTO PersonelProblem (ProblemID, KullaniciAdi) VALUES (%s,%s)",
                        (ProblemID, tcno))
            conn.commit()
            return redirect(url_for('PharmacyStaff.PersonelProblem'))
        elif request.form.get("add_skor"):
            ProblemID = request.form['problemid']
            tcno = request.form['belirtecid']
            skor = request.form['skor']
            skortarihi = request.form['skortarihi']
            
            cur.execute("INSERT INTO problemciktidegerlendirme (ProblemID, tcno, skor, skortarihi) VALUES (%s,%s,%s,%s)",
                        (ProblemID, tcno, skor, skortarihi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.PersonelProblem'))
        elif request.form.get("add_problem"):
            problemtipiid = request.form['problemtipiid']
            problemtanimi = request.form['problemtanimi']
            problemtanimlayiciismi = request.form['problemtanimlayiciismi']
            problemtanimlayicitcno = request.form['problemtanimlayicitcno']
            hedeflenenamactanimi = request.form['hedeflenenamactanimi']
            cur.execute('INSERT INTO problem (problemtipiid,problemtanimi,problemitanimlayiciismi,problemitanimlayantcno,hedeflenenamactanimi) VALUES (%s,\'%s\',\'%s\',%s,\'%s\')' % (
                problemtipiid, problemtanimi, problemtanimlayiciismi, problemtanimlayicitcno, hedeflenenamactanimi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.PharmacyProblemList'))
    return redirect(url_for('PharmacyStaff.ProblemMudahaleIndex'))


@PharmacyStaff.route('/template/edit/<id>', methods=['POST', 'GET'])
def get_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM aktiviteler WHERE aktiviteid = %s' % (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('PharmacyStaff/PharmacyStaffEdit.html', staff=data[0])


@PharmacyStaff.route('/template/update/<id>', methods=['POST'])
def update_temp(tcno):
    if request.method == 'POST':
        tcno = request.form['tcno']
        isim = request.form['name']
        email = request.form['email']
        telefon = request.form['phone']
        eczane_id = request.form['id']
        parola = request.form['pswd']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE eczanecalisani
            SET tcno = %s,
                isim = %s,
                email = %s,
                telefon = %s,
                eczane_id = %s,
                parola = %s
            WHERE tcno = %s
        """, (tcno, isim, email, telefon, eczane_id, parola, tcno))
        flash('eczanecalisani Updated Successfully')
        conn.commit()
        return redirect(url_for('PharmacyStaff.PharmacyStaffList'))


@PharmacyStaff.route('/template/delete/<string:tcno>', methods=['POST', 'GET'])
def delete_temp(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM eczanecalisani WHERE tcno = {0}'.format(tcno))
    conn.commit()
    #flash('eczanecalisani Removed Successfully')
    return redirect(url_for('PharmacyStaff.PharmacyStaffList'))