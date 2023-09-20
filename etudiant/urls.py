from django.urls import path
from .views import accueil, team, etudiant_login, releve, stage, parcours


app_name = "etudiant_app"

urlpatterns = [
    path(
        '', accueil, name="acceuil",
    ),
    path(
        'team/', team, name="team"
    ),
    path('login/', etudiant_login, name="login"),
    path('stage/form', stage, name="stage"),
    path('releve/form', releve, name="releve"),
    path('parcous/releve/<int:idReleve>', parcours, name="parcours"),
]
