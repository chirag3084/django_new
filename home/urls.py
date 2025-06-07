from django.urls import path
from . import views

# Registering the app's namespace
app_name = "home"

urlpatterns = [
    path("login/", views.login_p, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("forgetPassword/", views.forgetPassword, name="forgetPassword"),
    path("", views.home, name="home"), 
    path("export_data_as_json/", views.export_data_as_json, name="export_data_as_json"),
    path("add_transcation/", views.add_transcation, name="add_transcation"),
    path("view_transcation/", views.view_transcation, name="view_transcation"),
    path("export_data_as_json_by_id/<int:id>", views.export_data_as_json_by_id, name="export_data_as_json_by_id"),
    # path("load_json_data/", views.load_json_data, name="load_json_data"),
    path("export_data_as_text/", views.export_data_as_text, name="export_data_as_text"),
    
]
