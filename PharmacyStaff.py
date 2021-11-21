from flask import Blueprint, render_template

PharmacyStaff = Blueprint("PharmacyStaff", __name__,
                            static_folder="static", template_folder="templates")


