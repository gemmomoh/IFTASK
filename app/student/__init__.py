from flask import Blueprint


student_bp=Blueprint('student',__name__, template_folder="templates", static_folder= 'statics')

from app.student import views