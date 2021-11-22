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
            return render_template('PharmacyProblemList.html')
        elif request.form.get("submit_problemMudahale"):
            return redirect(url_for('PharmacyStaff.ProblemMudahaleIndex'))
        elif request.form.get("submit_PharmList"):
            return render_template('PharmacyStockList.html')
        elif request.form.get("submit_Personel_CRUD"):
            return redirect(url_for('PharmacyStaff.PharmacyStaffCrud'))
    return render_template('PharmacyStaff/PharmacyStaffMission.html')


@PharmacyStaff.route('/PharmacyProblemList')
def PharmacyProblemList():
    return render_template('PharmacyStaff/PharmacyProblemList.html')


@PharmacyStaff.route('/ProblemMudahaleIndex', methods=['POST', 'GET'])
def ProblemMudahaleIndex():
    if request.method == "POST":
        if request.form.get("Alan"):
            return redirect(url_for('PharmacyStaff.Alan'))
        elif request.form.get("Sinif"):
            return redirect(url_for('PharmacyStaff.Sinif'))
        elif request.form.get("Mudahale"):
            return redirect(url_for('PharmacyStaff.Mudahale'))
        elif request.form.get("Aktivite"):
            return redirect(url_for('PharmacyStaff.Aktivite'))
        elif request.form.get("Cikti"):
            return redirect(url_for('PharmacyStaff.Cikti'))
        elif request.form.get("Belirtec"):
            return redirect(url_for('PharmacyStaff.Belirtec'))
        elif request.form.get("7"):
            return redirect(url_for('PharmacyStaff.Aktivite'))
    return render_template('PharmacyStaff/Problem/ProblemList.html')


@PharmacyStaff.route('/Alan')
def Alan():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM alanlar")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Alan/AlanList.html', list_users=list_users)


@PharmacyStaff.route('/Sinif')
def Sinif():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM siniflar")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Sinif/SinifList.html', list_users=list_users)

@PharmacyStaff.route('/Mudahale')
def Mudahale():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM Mudahale")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Mudahale/MudahaleList.html', list_users=list_users)

@PharmacyStaff.route('/Aktivite')
def Aktivite():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM aktiviteler")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Aktivite/AktiviteList.html', list_users=list_users)


@PharmacyStaff.route('/Cikti')
def Cikti():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM cikti")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Cikti/CiktiList.html', list_users=list_users)


@PharmacyStaff.route('/Belirtec')
def Belirtec():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM belirtecler")
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/Problem/Belirtec/BelirtecList.html', list_users=list_users)

@PharmacyStaff.route('/template/ProblemTemplate', methods=['POST'])
def add_ProblemTemplate():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        if request.form.get("Alan"):
            alanID = request.form['id']
            alanadi = request.form['name']
            alantipi = request.form['type']
            cur.execute(
                'SELECT DISTINCT alanid FROM alanlar WHERE alanid=%s' % (alanID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Alan/AlanList.html')
            cur.execute("INSERT INTO alanlar (alanid, alanadi, alantipi) VALUES (%s,%s,%s)",
                        (alanID, alanadi, alantipi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.Alan'))
        elif request.form.get("Sinif"):
            SinifID = request.form['SinifID']
            SinifAdi = request.form['SinifAdi']
            AlanTipi = request.form['AlanTipi']
            cur.execute(
                'SELECT DISTINCT sinifid FROM siniflar WHERE sinifid=%s' % (SinifID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Sinif/SinifList.html')
            cur.execute("INSERT INTO siniflar (sinifid, sinifadi, alantipi) VALUES (%s,%s,%s)",
                        (SinifID, SinifAdi, AlanTipi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.Sinif'))
        elif request.form.get("Mudahale"):
            AlanID = request.form['AlanID']
            SinifID = request.form['SinifID']
            MudaheleID = request.form['MudaheleID']
            MudahaleAdi = request.form['MudahaleAdi']
            cur.execute("INSERT INTO mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (%s,%s,%s,%s)",
                        (AlanID, SinifID, MudaheleID, MudahaleAdi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.Mudahale'))
        elif request.form.get("Aktivite"):
            aktiviteID = request.form['id']
            aktiviteTanim = request.form['tanim']
            cur.execute(
                'SELECT DISTINCT aktiviteID FROM aktiviteler WHERE aktiviteid=%s' % (aktiviteID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Aktivite/AktiviteList.html')
            cur.execute("INSERT INTO aktiviteler (aktiviteid, aktivitetanimi) VALUES (%s,%s)",
                        (aktiviteID, aktiviteTanim))
            conn.commit()
            return redirect(url_for('PharmacyStaff.Aktivite'))
        elif request.form.get("Belirtec"):
            BelirtecID = request.form['BelirtecID']
            BelirtecTanimi = request.form['Belirtectanimi']
            cur.execute(
                'SELECT DISTINCT BelirtecID FROM belirtecler WHERE belirtecid=%s' % (BelirtecID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Belirtec/BelirtecList.html')
            cur.execute("INSERT INTO belirtecler (belirtecid, belirtectanimi) VALUES (%s,%s)",
                        (BelirtecID, BelirtecTanimi))
            conn.commit()
            return redirect(url_for('PharmacyStaff.Belirtec'))
        elif request.form.get("Cikti"):
            AlanID = request.form['AlanID']
            SinifID = request.form['SinifID']
            CiktiID = request.form['CiktiID']
            CiktiAdi = request.form['CiktiAdi']
            cur.execute(
                'SELECT DISTINCT ciktiid FROM cikti WHERE ciktiid=%s' % (CiktiID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('PharmacyStaff/Problem/Cikti/CiktiList.html')
            cur.execute("INSERT INTO cikti (alanid, sinifid,ciktiid, ciktiadi) VALUES (%s,%s,%s,%s)",
                        (AlanID, SinifID, CiktiID, CiktiAdi))
            conn.commit()
        return redirect(url_for('PharmacyStaff.Cikti'))
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

######


@PharmacyStaff.route('/PharmacyStockList')
def PharmacyStockList():
    return render_template('PharmacyStockList.html')


@PharmacyStaff.route('/PharmacyStaffCrud')
def PharmacyStaffCrud():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM eczanecalisani"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('PharmacyStaff/PharmacyStaffList.html', list_users=list_users)


@PharmacyStaff.route('/add_Pharmacy_Staff', methods=['POST'])
def add_Pharmacy_Staff():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        tcno = request.form['tcno']
        isim = request.form['name']
        email = request.form['email']
        telefon = request.form['phone']
        eczane_id = request.form['id']
        parola = request.form['pswd']
        cur.execute(
            'SELECT DISTINCT eczane_id FROM eczanecalisani WHERE eczane_id=%s' % (eczane_id))
        dataID = cur.fetchall()
        cur.execute(
            'SELECT tcno FROM eczanecalisani WHERE tcno=%s' % (tcno))
        dataTc = cur.fetchall()
        if len(dataID) == 0:
           # flash('Girdiğiniz Eczane_Id mevcut değil')
            render_template('PharmacyStaff/PharmacyStaffList.html')
        if len(dataTc) > 0:
          #  flash('Girdiğiniz TCNO zaten mevcut')
            render_template('PharmacyStaff/PharmacyStaffList.html')
        cur.execute("INSERT INTO eczanecalisani (tcno, isim, email, telefon, eczane_id, sifre) VALUES (%s,%s,%s,%s,%s,%s)",
                    (tcno, isim, email, telefon, eczane_id, parola))
        conn.commit()
        return redirect(url_for('PharmacyStaff.PharmacyStaffCrud'))


@PharmacyStaff.route('/edit/<tcno>', methods=['POST', 'GET'])
def get_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM eczanecalisani WHERE tcno = %s', (tcno))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('PharmacyStaff/PharmacyStaffEdit.html', staff=data[0])


@PharmacyStaff.route('/update/<tcno>', methods=['POST'])
def update_staff(tcno):
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


@PharmacyStaff.route('/delete/<string:tcno>', methods=['POST', 'GET'])
def delete_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM eczanecalisani WHERE tcno = {0}'.format(tcno))
    conn.commit()
    #flash('eczanecalisani Removed Successfully')
    return redirect(url_for('PharmacyStaff.PharmacyStaffList'))
