from flask import Blueprint, render_template

User = Blueprint("User", __name__, static_folder="static",
                 template_folder="templates")


@User.route("/User")
def PharmacyStaffCrud():
    return render_template('UserMainPage.html')
