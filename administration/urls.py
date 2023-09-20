from django.urls import path
from .views import dashboard, releveDetail
 
app_name = 'administration_app'

urlpatterns = [
    path("", dashboard, name="accueil"),
    path("revele/<int:id>", releveDetail, name="releve"),
    path("revele/<int:id>", releveDetail, name="stage")
]

