from flask import (Blueprint, redirect, render_template, request)

PharmacyMission = Blueprint("PharmacyMission", __name__, static_folder="static", template_folder="templates")


@PharmacyMission.route('/PharmacyActions', methods=['POST', 'GET'])
def PharmacyActions():
    print("Burda")
    if request.method == "POST":
        if request.form.get("submit_problemList"):
            return render_template('PharmacyProblemList.html')
        elif request.form.get("submit_problemAdd"):
            return render_template('PharmacyProblemAdd.html')
        elif request.form.get("submit_PharmList"):
            return render_template('PharmacyStockList.html')
        elif request.form.get("submit_Personel_CRUD"):
            return render_template('PharmacyStaffCrud.html')
    return render_template('PharmacistAdmin.html')


@PharmacyMission.route('/PharmacyProblemList')
def PharmacyProblemList():
    return render_template('PharmacyProblemList.html')


@PharmacyMission.route('/PharmacyProblemAdd')
def PharmacyProblemAdd():
    return render_template('PharmacyProblemAdd.html')


@PharmacyMission.route('/PharmacyStockList')
def PharmacyStockList():
    return render_template('PharmacyStockList.html')


@PharmacyMission.route('/PharmacyStaffCrud')
def PharmacyStaffCrud():
    return render_template('PharmacyStaffCrud.html')
