from django.shortcuts import render
from etudiant.models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def dashboard(request):
    releve = ReleveCote.objects.filter(statut="en cours")
    stage = DemandeStage.objects.filter(statut="en cours")

    context = {
        'releve': releve,
        'stage': stage,
    }

    return render(request, "administration/dashboard.html", context)


def releveDetail(request, id):
    releve = ReleveCote.objects.get(pk=id)

    rapports = Rapport.objects.filter(destination=releve.etudiant)

    if request.method == "POST":
        form = RapportForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("message")
            rapport_instance = Rapport(
                destination=releve.etudiant,
                message=message
            )

            rapport_instance.save()


            # envoye le mail

            subject = ''
            message = message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["nathan.lopez.code@gmail.com", ]
            #send_mail(subject, message, email_from, recipient_list, fail_silently=False,)

    form = RapportForm()

    context = {
        "releve": releve,
        "parcours": ParcousEtudiant.objects.filter(releve=releve),
        'rapports': Rapport.objects.filter(destination=releve.etudiant),
        "form": form
    }

    return render(request, "administration/procedure_detail.html", context)


def StageDetail(request, id):
    pass
