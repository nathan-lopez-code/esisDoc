from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

from django.urls import reverse


class Etudiant(AbstractUser):
    sexe = models.CharField(max_length=2, choices=(("M", "M"), ("F", "F")), default="M", null=True, blank=True)
    lieu_de_naissance = models.CharField(default="Lubumbashi", max_length=50, null=True, blank=True)
    date_de_naissance = models.DateField(default=date(2000, 1, 1), null=True, blank=True)
    promotion = models.CharField(default="Genie logiciel", null=True, blank=True, max_length=50)


class Infos(models.Model):
    TYPE = (
        ('information', 'information'),
        ('important', 'important'),
        ('urgent', 'urgent'),
    )

    date = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=TYPE, max_length=30)
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=5000)
    auteur = models.ForeignKey(Etudiant, on_delete=models.CASCADE)


class DocumentAcademique(models.Model):
    STATUT = (
        ("en cours", "en cours"),
        ("rejeter", "rejeter"),
        ("approuver", "approuver")
    )

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True)
    date_soumission = models.DateTimeField(auto_now=True)
    statut = models.CharField(choices=STATUT, max_length=100, default="en cours")


# procedure
class ReleveCote(DocumentAcademique):
    photo_passport = models.FileField(upload_to="releveCote/")
    nom_postnom_pere = models.CharField(max_length=300, blank=True, null=True)
    nom_postnom_mere = models.CharField(max_length=300, blank=True, null=True)
    telephone = models.CharField(max_length=14)


    def get_absolute_url(self):
        return reverse("administration_app:releve", kwargs={"id": self.pk})


class ParcousEtudiant(models.Model):
    PROMOTION_CHOIX = (
        ("Preparatoire", "Preparatoire"),
        ("Licence 1", "Licence 1"),
        ("Licence 2", "Licence 2"),
        ("Licence 3", "Licence 3"),
    )

    promotion = models.CharField(choices=PROMOTION_CHOIX, max_length=100)
    annee_academeique = models.CharField(max_length=100)
    session_reussite = models.CharField(
        choices=(("premiere session", "premiere session"), ("deuxieme session", "deuxieme session")), max_length=100)

    # attribut optionel
    session_defense = models.CharField(blank=True, null=True, max_length=100)
    filiere = models.CharField(blank=True, null=True, max_length=40)

    releve = models.ForeignKey(ReleveCote, on_delete=models.CASCADE)


class DemandeStage(DocumentAcademique):
    name = models.CharField(max_length=100, default="demande de stage")
    ville = models.CharField(max_length=100, )
    destinateur = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("administration_app:releve", kwargs={"id": self.pk})


# presentation
class Team(models.Model):
    name = models.CharField(max_length=100)
    promotion = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="team/")


class Rapport(models.Model):
    destination = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="destination")
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=1000000, )

    class Meta:
        ordering = ["-date"]
