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
        if request.form.get("submit_detay"):
            return redirect(url_for('PharmacyMission.DetayIndex'))
        elif request.form.get("submit_problemAdd"):
            return redirect(url_for('PharmacyMission.ProblemIndex'))
        elif request.form.get("submit_PharmList"):
            return render_template('PharmacyStockList.html')
        elif request.form.get("submit_Personel_CRUD"):
            return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))
    return render_template('PharmacistAdmin.html')


@PharmacyMission.route('/DetayIndex', methods=['POST', 'GET'])
def DetayIndex():
    if request.method == "POST":
        if request.form.get("CiktiDetay"):
            return redirect(url_for('PharmacyMission.CiktiDetay'))
        elif request.form.get("MudahaleDetay"):
            return redirect(url_for('PharmacyMission.MudahaleDetay'))
    return redirect(url_for('PharmacyMission.MudahaleDetay'))


@PharmacyMission.route('/MudahaleDetay', methods=['POST', 'GET'])
def MudahaleDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT M.alanid, M.sinifid, M.mudahaleid, A.aktiviteid FROM mudahale AS M, aktiviteler AS A GROUP BY M.alanid, M.sinifid, M.mudahaleid, A.aktiviteid")
    list_users = cur.fetchall()
    cur.execute("SELECT * FROM mudahaledetay")
    list_order = cur.fetchall()
    return render_template('Pharmacy/ProblemDetay/MudahaleDetay/MudahaleDetayList.html', list_users=list_users, list_order=list_order)


@PharmacyMission.route('/CiktiDetay', methods=['POST', 'GET'])
def CiktiDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT C.alanid, C.sinifid, c.ciktiid, B.belirtecid FROM cikti AS C, belirtecler AS B GROUP BY Belirtecid, C.alanid, C.sinifid, C.ciktiid")
    list_users = cur.fetchall()
    cur.execute("SELECT * FROM ciktidetay")
    list_order = cur.fetchall()
    return render_template('Pharmacy/ProblemDetay/CiktiDetay/CiktiDetayList.html', list_users=list_users, list_order=list_order)


@PharmacyMission.route('/mudahaledetay/add_MudahaleDetay', methods=['POST', 'GET'])
def add_MudahaleDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST': 
        alanid = request.form['alanid']
        sinifid = request.form['sinifid']
        mudahaleid = request.form['mudahaleid']
        aktiviteid = request.form['aktiviteid']
        sira = request.form['sira']
        if sira=='':
            flash('Lütfen gerekli alanı doldurunuz')
        else:
            cur.execute(
                'SELECT DISTINCT sira FROM mudahaledetay WHERE sira=%s' % (sira))
            data = cur.fetchall()
            if len(data) > 0:
                flash('Girdiğiniz Sıra\'da Zaten Bir İş Mevcut')
            else:
                cur.execute("INSERT INTO mudahaledetay (alanid, sinifid, mudahaleid,aktiviteid,sira) VALUES (%s,%s,%s,%s,%s)",
                            (alanid, sinifid, mudahaleid, aktiviteid, sira))
                conn.commit()
    return redirect(url_for('PharmacyMission.MudahaleDetay'))


@PharmacyMission.route('/ciktidetay/add_CiktiDetay', methods=['POST', 'GET'])
def add_CiktiDetay():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.form.get("CiktiDetay"):
        alanid = request.form['alanid']
        sinifid = request.form['sinifid']
        ciktiid = request.form['ciktiid']
        belirtecid = request.form['belirtecid']
        sira = request.form['sira']
        if sira == '':
            flash('Lütfen gerekli alanı doldurunuz')
        else:
            cur.execute(
                'SELECT DISTINCT sira FROM ciktidetay WHERE sira=%s' % (sira))
            data = cur.fetchall()
            if len(data) > 0:
                flash('Girdiğiniz sıra da bir işlem zaten mevcut')
            else:
                cur.execute("INSERT INTO ciktidetay (alanid, sinifid, ciktiid, belirtecid, sira) VALUES (%s,%s,%s,%s,%s)",
                            (alanid, sinifid, ciktiid, belirtecid, sira))
                conn.commit()
    return redirect(url_for('PharmacyMission.CiktiDetay'))


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
        elif request.form.get("Problem"):
            return redirect(url_for('PharmacyMission.Problem'))
    return redirect(url_for('PharmacyMission.Alan'))


@PharmacyMission.route('/Problem')
def Problem():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM problembirim")
    list_users = cur.fetchall()
    return render_template('Pharmacy/Problem/Problem/ProblemList.html', list_users=list_users)

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
            if alanadi=='' or alanadi=='' or alantipi=='':
                flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute( 'SELECT DISTINCT alanid FROM alanlar WHERE alanid=%s' % (alanID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz Alan ID zaten mevcut')
                else:
                    cur.execute("INSERT INTO alanlar (alanid, alanadi, alantipi) VALUES (%s,%s,%s)",
                            (alanID, alanadi, alantipi))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Alan'))
        elif request.form.get("Sinif"):
            SinifID = request.form['SinifID']
            SinifAdi = request.form['SinifAdi']
            AlanTipi = request.form['AlanTipi']
            if SinifID == '' or SinifAdi == '' or AlanTipi == '':
                flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute(
                    'SELECT DISTINCT sinifid FROM siniflar WHERE sinifid=%s' % (SinifID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz Sınıf ID zaten mevcut')
                else:
                    cur.execute("INSERT INTO siniflar (sinifid, sinifadi, alantipi) VALUES (%s,%s,%s)",
                            (SinifID, SinifAdi, AlanTipi))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Sinif'))
        elif request.form.get("Mudahale"):
            AlanID = request.form['AlanID']
            SinifID = request.form['SinifID']
            MudaheleID = request.form['MudaheleID']
            MudahaleAdi = request.form['MudahaleAdi']
            if AlanID == '' or SinifID == '' or MudaheleID == '' or MudahaleAdi == '':
                flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute(
                    'SELECT DISTINCT * FROM mudahale WHERE sinifid=%s and alanid=%s and mudahaleid=%s' % (SinifID,AlanID,MudaheleID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz MudahaleID zaten mevcut')
                else:
                    cur.execute("INSERT INTO mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (%s,%s,%s,%s)",
                                (AlanID, SinifID, MudaheleID, MudahaleAdi))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Mudahale'))
        elif request.form.get("Aktivite"):
            aktiviteID = request.form['id']
            aktiviteTanim = request.form['tanim']
            if aktiviteID == '' or aktiviteTanim == '':
              flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute(
                    'SELECT DISTINCT * FROM aktiviteler WHERE aktiviteID=%s' % (aktiviteID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz aktiviteID zaten mevcut')
                else:
                    cur.execute("INSERT INTO aktiviteler (aktiviteid, aktivitetanimi) VALUES (%s,%s)",
                                (aktiviteID, aktiviteTanim))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Aktivite'))
        elif request.form.get("Belirtec"):
            BelirtecID = request.form['BelirtecID']
            BelirtecTanimi = request.form['Belirtectanimi']
            if BelirtecID == '' or BelirtecTanimi == '':
              flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute( 'SELECT DISTINCT BelirtecID FROM belirtecler WHERE belirtecid=%s' % (BelirtecID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz BelirtecID zaten mevcut')
                else:
                    cur.execute("INSERT INTO belirtecler (belirtecid, belirtectanimi) VALUES (%s,%s)",
                                (BelirtecID, BelirtecTanimi))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Belirtec'))
        elif request.form.get("Cikti"):
            AlanID = request.form['AlanID']
            SinifID = request.form['SinifID']
            CiktiID = request.form['CiktiID']
            CiktiAdi = request.form['CiktiAdi']
            if AlanID == '' or SinifID == '' or CiktiID == '' or CiktiAdi == '':
                flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute(
                    'SELECT DISTINCT * FROM cikti WHERE sinifid=%s and alanid=%s and ciktiid=%s' % (SinifID, AlanID, CiktiID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz CiktiID zaten mevcut')
                else:
                    cur.execute("INSERT INTO cikti (alanid, sinifid, ciktiid, ciktiadi) VALUES (%s,%s,%s,%s)",
                                (AlanID, SinifID, CiktiID, CiktiAdi))
                    conn.commit()
            return redirect(url_for('PharmacyMission.Cikti'))
        elif request.form.get("Problem"):
            ProblemID = request.form['ProblemID']
            BirimID = request.form['BirimID']
            eslenmetarihi = request.form['tarih']
            if ProblemID == '' or BirimID == '' or eslenmetarihi == '':
                flash('Lütfen gerekli alanı doldurunuz')
            else:
                cur.execute(
                    'SELECT DISTINCT * FROM problembirim WHERE problemid=%s and birimid=%s' % (ProblemID, BirimID))
                data = cur.fetchall()
                if len(data) > 0:
                    flash('Girdiğiniz ProblemID zaten mevcut')
                else:
                    cur.execute("INSERT INTO problembirim (problemid, birimid, eslenmetarihi) VALUES (%s,%s,'%s')",
                                (ProblemID, BirimID, eslenmetarihi))
                    conn.commit()
                return redirect(url_for('PharmacyMission.Problem'))
        return redirect(url_for('PharmacyMission.ProblemIndex'))

@PharmacyMission.route('/Alan/edit/<id>', methods=['POST', 'GET'])
def getAlan_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM alanlar WHERE alanid = %s'% (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Alan/AlanEdit.html', temp=data[0])


@PharmacyMission.route('/Sinif/edit/<id>', methods=['POST', 'GET'])
def getSinif_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM siniflar WHERE sinifid = %s' % (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Sinif/SinifEdit.html', temp=data[0])


@PharmacyMission.route('/mudahale/edit/<alanid>/<sinifid>/<mudahaleid>', methods=['POST', 'GET'])
def getMudahale_Temp(alanid,sinifid,mudahaleid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        'SELECT * FROM mudahale WHERE alanid = %s and sinifid = %s and mudahaleid = %s' % (alanid, sinifid, mudahaleid))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Mudahale/MudahaleEdit.html', temp=data[0])

@PharmacyMission.route('/Aktiviteler/edit/<id>', methods=['POST', 'GET'])
def getAktiviteler_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM aktiviteler WHERE aktiviteid = %s'% (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Aktivite/AktiviteEdit.html', temp=data[0])


@PharmacyMission.route('/Belirtecler/edit/<id>', methods=['POST', 'GET'])
def getBelirtec_Temp(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM Belirtecler WHERE belirtecid = %s' % (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Belirtec/BelirtecEdit.html', temp=data[0])


@PharmacyMission.route('/Cikti/edit/<alanid>/<sinifid>/<ciktiid>', methods=['POST', 'GET'])
def getCikti_Temp(alanid,sinifid,ciktiid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        'SELECT * FROM cikti WHERE alanid = %s and sinifid = %s and ciktiid = %s' % (alanid, sinifid, ciktiid))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('Pharmacy/Problem/Cikti/CiktiEdit.html', temp=data[0])


@PharmacyMission.route('/template/update/<id>', methods=['POST'])
def updateCikti_temp(tcno):
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
        conn.commit()
        return redirect(url_for('PharmacyMission.PharmacyStaffList'))


@PharmacyMission.route('/Mudahale/update/<alanid>/<sinifid>/<mudahaleid>', methods=['POST'])
def updateMudahale_temp(alanid,sinifid,mudahaleid):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        AlanID = request.form['AlanID']
        SinifID = request.form['SinifID']
        MudaheleID = request.form['MudaheleID']
        MudahaleAdi = request.form['MudahaleAdi']
        if AlanID == '' or SinifID == '' or MudaheleID == '' or MudahaleAdi == '':
            flash('Lütfen gerekli alanı doldurunuz')
        else:
            cur.execute(
                'SELECT DISTINCT * FROM mudahale WHERE sinifid=%s and alanid=%s and mudahaleid=%s' % (SinifID, AlanID, MudaheleID))
            data = cur.fetchall()
            if len(data) > 0 and (AlanID == alanid and SinifID == sinifid and MudaheleID == mudahaleid)==0:
                flash('Girdiğiniz MudahaleID zaten mevcut')
            else:
                cur.execute("""UPDATE mudahale SET sinifid=%s , alanid=%s , mudahaleid=%s , mudahaleadi='%s'
                        WHERE sinifid=%s and alanid=%s and mudahaleid=%s""" % (SinifID, AlanID, MudaheleID, MudahaleAdi ,sinifid, alanid, mudahaleid))
        return redirect(url_for('PharmacyMission.Mudahale'))
    

@PharmacyMission.route('/aktivite/update/<aktiviteid>', methods=['POST'])
def updateAktivite_temp(aktiviteid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    AktiviteID = request.form['id']
    AktiviteTanimi = request.form['tanim']
    if AktiviteID == '' or AktiviteTanimi=='':
        flash('Lütfen gerekli alanı doldurunuz')
    else:
        cur.execute(
            'SELECT DISTINCT * FROM aktiviteler WHERE aktiviteid=%s' % (AktiviteID))
        data = cur.fetchall()
        if len(data) > 0 and (AktiviteID == aktiviteid) == 0:
            flash('Girdiğiniz AktiviteID zaten mevcut')
        else:
            cur.execute("""UPDATE aktiviteler SET aktiviteid=%s, aktivitetanimi='%s'
                    WHERE aktiviteid=%s""" % (aktiviteid, AktiviteTanimi, AktiviteID))
    return redirect(url_for('PharmacyMission.Aktivite'))


@PharmacyMission.route('/belirtec/update/<belirtecid>', methods=['POST'])
def updateBelirtec_temp(belirtecid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    BelirtecID = request.form['BelirtecID']
    BelirtecTanimi = request.form['Belirtectanimi']
    if BelirtecID == '' or BelirtecTanimi == '':
        flash('Lütfen gerekli alanı doldurunuz')
    else:
        cur.execute(
            'SELECT DISTINCT * FROM belirtecler WHERE belirtecid=%s' % (BelirtecID))
        data = cur.fetchall()
        if len(data) > 0 and (BelirtecID == belirtecid) == 0:
            flash('Girdiğiniz BelirtecID zaten mevcut')
        else:
            cur.execute("""UPDATE belirtecler SET belirtecid=%s, belirtectanimi='%s'
                    WHERE belirtecid=%s""" % (belirtecid, BelirtecTanimi, BelirtecID))
    return redirect(url_for('PharmacyMission.Belirtec'))
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
        status = request.form['status']
        parola = request.form['pswd']
        cur.execute(
            'SELECT DISTINCT eczane_id FROM eczanecalisani WHERE eczane_id=%s'% (eczane_id))
        dataID = cur.fetchall()
        cur.execute(
            'SELECT tcno FROM eczanecalisani WHERE tcno=%s'% (tcno))
        dataTc = cur.fetchall()
        if len(dataID) == 0:
            flash('Girdiğiniz Eczane_Id mevcut değil')
        if len(dataTc) > 0:
            flash('Girdiğiniz TCNO zaten mevcut')
        else:
            cur.execute("INSERT INTO eczanecalisani (tcno, isim, email, telefon, eczane_id, status, sifre) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (tcno, isim, email, telefon, eczane_id, status, parola))
            conn.commit()
        return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))


@PharmacyMission.route('/edit/<tcno>', methods=['POST', 'GET'])
def get_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM eczanecalisani WHERE tcno = %s'% (tcno))
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
        status = request.form['status']
        parola = request.form['pswd']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE eczanecalisani
            SET tcno = %s,
                isim = %s,
                email = %s,
                telefon = %s,
                eczane_id = %s,
                status = %s,
                sifre = %s
            WHERE tcno = %s
        """, (tcno, isim, email, telefon, eczane_id, status, parola))
        conn.commit()
        return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))


@PharmacyMission.route('/delete/<string:tcno>', methods=['POST', 'GET'])
def delete_staff(tcno):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('DELETE FROM eczanecalisani WHERE tcno = {0}'.format(tcno))
    conn.commit()
    flash('%s TC Numaralı Çalışan Kaldırıldı' % (tcno))
    return redirect(url_for('PharmacyMission.PharmacyStaffCrud'))
