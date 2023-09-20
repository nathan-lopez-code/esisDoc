from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import EtudiantLoginForm, SelectDemandeForm, ReleveCoteForm, DemandeStageForm, Parcous
from .models import Etudiant, DemandeStage, ParcousEtudiant, ReleveCote


@login_required(login_url="/login/")
def accueil(request):
    etudiant = Etudiant.objects.get(pk=request.user.id)

    if request.method == "POST":
        form = SelectDemandeForm(request.POST)
        if form.is_valid():
            procedure = form.cleaned_data.get('procedure')
            if procedure == "R":
                return redirect("/releve/form")
            else:
                return redirect("/stage/form")
        else:
            return HttpResponse("formaulaire incorrecte")

    demande1 = ReleveCote.objects.filter(etudiant=etudiant)
    demande2 = DemandeStage.objects.filter(etudiant=etudiant)

    context = {
        "etudiant": etudiant,
        "form": SelectDemandeForm(),
        "demande1": demande1,
        "demande2": demande2,
    }

    return render(
        request, 'etudiant/index.html', context
    )


def releve(request):
    etudiant = Etudiant.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ReleveCoteForm(request.POST, request.FILES)
        if form.is_valid():
            # enregistrer le releve
            r = ReleveCote.objects.create(
                photo_passport=form.cleaned_data.get("photo"),
                telephone=form.cleaned_data.get("telephone"),
                nom_postnom_pere=form.cleaned_data.get("nom_postnom_pere"),
                nom_postnom_mere=form.cleaned_data.get("nom_postnom_mere"),
                etudiant=etudiant,
            )
            r.save()
            # ajouter le parcours

            return redirect(f"/parcous/releve/{r.id}")
        else:
            return HttpResponse(f"formaulaire incorrecte {form.errors}")

    context = {
        "etudiant": etudiant,
        "form": ReleveCoteForm(),
        "demande": "releve de cote"

    }

    return render(
        request, 'etudiant/form_releve.html', context
    )


def parcours(request, idReleve):
    etudiant = Etudiant.objects.get(pk=request.user.id)
    releve = ReleveCote.objects.get(pk=idReleve)

    if request.method == "POST":
        form = Parcous(request.POST)
        if form.is_valid():

            p = ParcousEtudiant.objects.create(
                promotion=form.cleaned_data.get("promotion"),
                annee_academeique=form.cleaned_data.get("annee_academeique"),
                session_reussite=form.cleaned_data.get("session_reussite"),
                session_defense=form.cleaned_data.get("session_defense"),
                filiere=form.cleaned_data.get("filiere"),
                releve=releve,
            )

            p.save()

            context = {
                "etudiant": etudiant,
                "form": Parcous(),
                "demande": "parcours academique",
                "parcours": releve.parcousetudiant_set.all()

            }

            return render(
                request, 'etudiant/form_parcours.html', context
            )
        else:
            return HttpResponse(f"formaulaire incorrecte {form.errors}")

    context = {
        "etudiant": etudiant,
        "form": Parcous(),
        "demande": "parcours academique"

    }

    return render(
        request, 'etudiant/form_parcours.html', context
    )


def stage(request):
    etudiant = Etudiant.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = DemandeStageForm(request.POST)
        if form.is_valid():
            ville = form.cleaned_data.get('ville')
            destinateur = form.cleaned_data.get('destinateur')
            entreprise = form.cleaned_data.get('entreprise')

            d = DemandeStage.objects.create(
                etudiant=etudiant,
                ville=ville,
                destinateur=destinateur,
                entreprise=entreprise
            )
            d.save()

            return render(request, "etudiant/success.html", context={"demande": d})

        else:
            return HttpResponse("formaulaire incorrecte")

    context = {
        "etudiant": etudiant,
        "form": DemandeStageForm(),
        "demande": "stage"
    }

    return render(
        request, 'etudiant/form_Demande.html', context
    )


def team(request):
    return render(
        request, 'etudiant/team.html', None
    )


def etudiant_login(request):
    form = EtudiantLoginForm()

    if request.method == "POST":
        form = EtudiantLoginForm(request.POST)
        try:
            next = request.POST.get('next')
        except:
            next = None

        if form.is_valid():
            email = form.cleaned_data.get('email')
            mot_de_passe = form.cleaned_data.get('mot_de_passe')
            try:
                user = Etudiant.objects.get(email=email)

                if not check_password(mot_de_passe, user.password):
                    return render(request, "etudiant/login.html", context={
                        "form": form,
                        "message_erreur": f"mot de passe incorrecte"
                    })
            except:
                user = None

            if user is not None:
                if next:
                    login(request, user)
                    return redirect(to=next)
                else:
                    login(request, user)
                    return redirect(to="/")

            else:
                return render(request, "etudiant/login.html", context={
                    "form": form,
                    "message_erreur": f"l'email {email} n'a pas ete trouver {user}"
                })
        else:
            return render(request, "etudiant/login.html", context={
                'form': form,
                'message_erreur': f"formulaire invalide {form.is_bound} error : {form.errors}, this is next = {next}"
            })
    else:

        return render(request, "etudiant/login.html", context={
            'form': form
        })
