from flask import (Blueprint, redirect, render_template, request, flash, url_for)
import psycopg2
import psycopg2.extras
PharmacyMission = Blueprint("PharmacyMission", __name__, static_folder="static", template_folder="templates")
DB_HOST = "localhost"
DB_NAME = "IlacSepeti"
DB_USER = "postgres"
DB_PASS = "selimyucu03"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

@PharmacyMission.route('/PharmacyActions', methods=['POST', 'GET'])
def PharmacyActions():
    if request.method == "POST":
        if request.form.get("submit_problemList"):
            return render_template('PharmacyProblemList.html')
        elif request.form.get("submit_problemAdd"):
            return redirect(url_for('PharmacyMission.ProblemIndex'))
        elif request.form.get("submit_PharmList"):
            return render_template('PharmacyStockList.html')
        elif request.form.get("submit_Personel_CRUD"):
            return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))
    return render_template('PharmacistAdmin.html')


@PharmacyMission.route('/PharmacyProblemList')
def PharmacyProblemList():
    return render_template('Pharmacy/PharmacyProblemList.html')


@PharmacyMission.route('/ProblemIndex', methods=['POST', 'GET'])
def ProblemIndex():
    if request.method == "POST":
        if request.form.get("Alan"):
            return redirect(url_for('PharmacyMission.Alan'))
        elif request.form.get("Sinif"):
            return redirect(url_for('PharmacyMission.Sinif'))
        elif request.form.get("Mudahale"):
            return redirect(url_for('PharmacyMission.Mudahale'))
        elif request.form.get("Aktivite"):
            return redirect(url_for('PharmacyMission.Aktivite'))
        elif request.form.get("Cikti"):
            return redirect(url_for('PharmacyMission.Cikti'))
        elif request.form.get("Belirtec"):
            return redirect(url_for('PharmacyMission.Belirtec'))
        elif request.form.get("7"):
            return redirect(url_for('PharmacyMission.Aktivite'))
    return render_template('Pharmacy/Problem/ProblemList.html')


@PharmacyMission.route('/Aktivite')
def Aktivite():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM aktiviteler")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Aktivite/AktiviteList.html', list_users=list_users)


@PharmacyMission.route('/Alan')
def Alan():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM alanlar")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Alan/AlanList.html', list_users=list_users)


@PharmacyMission.route('/Sinif')
def Sinif():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM siniflar")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Sinif/SinifList.html', list_users=list_users)


@PharmacyMission.route('/Cikti')
def Cikti():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM cikti")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Cikti/CiktiList.html', list_users=list_users)


@PharmacyMission.route('/Belirtec')
def Belirtec():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM belirtecler")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Belirtec/BelirtecList.html', list_users=list_users)


@PharmacyMission.route('/Mudahale')
def Mudahale():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM Mudahale")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Mudahale/MudahaleList.html', list_users=list_users)

@PharmacyMission.route('/template/ProblemTemplate', methods=['POST'])
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
                render_template('Pharmacy/Problem/Alan/AlanList.html')
            cur.execute("INSERT INTO alanlar (alanid, alanadi, alantipi) VALUES (%s,%s,%s)",
                        (alanID, alanadi, alantipi))
            conn.commit()
            return redirect(url_for('PharmacyMission.Alan'))
        elif request.form.get("Sinif"):
            SinifID = request.form['SinifID']
            SinifAdi = request.form['SinifAdi']
            AlanTipi = request.form['AlanTipi']
            cur.execute(
                'SELECT DISTINCT sinifid FROM siniflar WHERE sinifid=%s' % (SinifID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('Pharmacy/Problem/Sinif/SinifList.html')
            cur.execute("INSERT INTO siniflar (sinifid, sinifadi, alantipi) VALUES (%s,%s,%s)",
                        (SinifID, SinifAdi, AlanTipi))
            conn.commit()
            return redirect(url_for('PharmacyMission.Sinif'))
        elif request.form.get("Mudahale"):
            AlanID = request.form['AlanID']
            SinifID = request.form['SinifID']
            MudaheleID = request.form['MudaheleID']
            MudahaleAdi = request.form['MudahaleAdi']
            cur.execute("INSERT INTO mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (%s,%s,%s,%s)",
                        (AlanID, SinifID, MudaheleID, MudahaleAdi))
            conn.commit()
            return redirect(url_for('PharmacyMission.Mudahale'))
        elif request.form.get("Aktivite"):
            aktiviteID = request.form['id']
            aktiviteTanim = request.form['tanim']
            cur.execute(
                'SELECT DISTINCT aktiviteID FROM aktiviteler WHERE aktiviteid=%s' % (aktiviteID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('Pharmacy/Problem/Aktivite/AktiviteList.html')
            cur.execute("INSERT INTO aktiviteler (aktiviteid, aktivitetanimi) VALUES (%s,%s)",
                        (aktiviteID, aktiviteTanim))
            conn.commit()
            return redirect(url_for('PharmacyMission.Aktivite'))
        elif request.form.get("Belirtec"):
            BelirtecID = request.form['BelirtecID']
            BelirtecTanimi = request.form['Belirtectanimi']
            cur.execute(
                'SELECT DISTINCT BelirtecID FROM belirtecler WHERE belirtecid=%s' % (BelirtecID))
            data = cur.fetchall()
            if len(data) > 0:
                # flash('Girdiğiniz Eczane_Id mevcut değil')
                render_template('Pharmacy/Problem/Belirtec/BelirtecList.html')
            cur.execute("INSERT INTO belirtecler (belirtecid, belirtectanimi) VALUES (%s,%s)",
                        (BelirtecID, BelirtecTanimi))
            conn.commit()
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
                render_template('Pharmacy/Problem/Cikti/CiktiList.html')
            cur.execute("INSERT INTO cikti (alanid, sinifid,ciktiid, ciktiadi) VALUES (%s,%s,%s,%s)",
                        (AlanID, SinifID, CiktiID, CiktiAdi))
            conn.commit()
        return redirect(url_for('PharmacyMission.Cikti'))
    return redirect(url_for('PharmacyMission.ProblemIndex'))

@PharmacyMission.route('/template/edit/<id>', methods=['POST', 'GET'])
def get_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM aktiviteler WHERE aktiviteid = %s'% (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/PharmacyStaffEdit.html', staff=data[0])


@PharmacyMission.route('/template/update/<id>', methods=['POST'])
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
        return redirect(url_for('PharmacyMission.PharmacyStaffList'))


@PharmacyMission.route('/template/delete/<string:tcno>', methods=['POST', 'GET'])
def delete_temp(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM eczanecalisani WHERE tcno = {0}'.format(tcno))
    conn.commit()
    #flash('eczanecalisani Removed Successfully')
    return redirect(url_for('PharmacyMission.PharmacyStaffList'))

######

@PharmacyMission.route('/PharmacyStockList')
def PharmacyStockList():
    return render_template('PharmacyStockList.html')


@PharmacyMission.route('/PharmacyStaffCrud')
def PharmacyStaffCrud():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM eczanecalisani"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('Pharmacy/PharmacyStaffList.html', list_users=list_users)


@PharmacyMission.route('/add_Pharmacy_Staff', methods=['POST'])
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
            'SELECT DISTINCT eczane_id FROM eczanecalisani WHERE eczane_id=%s'% (eczane_id))
        dataID = cur.fetchall()
        cur.execute(
            'SELECT tcno FROM eczanecalisani WHERE tcno=%s'% (tcno))
        dataTc = cur.fetchall()
        if len(dataID) == 0:
           # flash('Girdiğiniz Eczane_Id mevcut değil')
            render_template('Pharmacy/PharmacyStaffList.html')
        if len(dataTc) > 0:
          #  flash('Girdiğiniz TCNO zaten mevcut')
            render_template('Pharmacy/PharmacyStaffList.html')
        cur.execute("INSERT INTO eczanecalisani (tcno, isim, email, telefon, eczane_id, sifre) VALUES (%s,%s,%s,%s,%s,%s)", (tcno, isim, email, telefon, eczane_id, parola))
        conn.commit()
        return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))


@PharmacyMission.route('/edit/<tcno>', methods=['POST', 'GET'])
def get_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM eczanecalisani WHERE tcno = %s', (tcno))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/PharmacyStaffEdit.html', staff=data[0])


@PharmacyMission.route('/update/<tcno>', methods=['POST'])
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
        return redirect(url_for('PharmacyMission.PharmacyStaffList'))


@PharmacyMission.route('/delete/<string:tcno>', methods=['POST', 'GET'])
def delete_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('DELETE FROM eczanecalisani WHERE tcno = {0}'.format(tcno))
    conn.commit()
    #flash('eczanecalisani Removed Successfully')
    return redirect(url_for('PharmacyMission.PharmacyStaffList'))
