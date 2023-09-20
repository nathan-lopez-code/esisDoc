from django import forms


class EtudiantLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Entrez votre email  "
            }
        )
    )
    mot_de_passe = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "mot de passe "
            }
        )
    )


class SelectDemandeForm(forms.Form):
    choice = (
        ("S", "demande de stage",),
        ("R", "Releve de cotes",),
    )

    procedure = forms.CharField(

        widget=forms.Select(
            choices=choice,
            attrs={
                'class': "custom-select mb-4",
                'style': "height: 47px; width: 100%; padding:5px; color:blue",

            },
        )
    )


class ReleveCoteForm(forms.Form):
    photo = forms.ImageField(label="Photo passeport")
    telephone = forms.CharField(
        max_length=14, widget=forms.TextInput(
            attrs={
                'placeholder': "Entrez votre numero de telephone ",
            },
        )
                                )
    nom_postnom_pere = forms.CharField(
        max_length=300, required=True, widget=forms.TextInput(
            attrs={
                'placeholder': "nom et postnom du pere pour l'attestation de frequetation ",
            },
        ))
    nom_postnom_mere = forms.CharField(max_length=300, required=True, widget=forms.TextInput(
            attrs={
                'placeholder': "nom et postnom de la mere pour l'attestation de frequetation",
            },
        ))


class DemandeStageForm(forms.Form):
    ville = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Entrez la ville ou passer le stage",

            },
        )
    )
    destinateur = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Entrez le nom a qui s'adressera la lettre de stage",

            },
        )
    )
    entreprise = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Entrez le nom de l'entreprise",

            },
        )
    )


class Parcous(forms.Form):
    PROMOTION_CHOIX = (
        ("Preparatoire", "Preparatoire"),
        ("Licence 1", "Licence 1"),
        ("Licence 2", "Licence 2"),
        ("Licence 3", "Licence 3"),
    )

    promotion = forms.CharField(
        widget=forms.Select(
            choices=PROMOTION_CHOIX,
            attrs={
                'class': "custom-select mb-4",
                'style': "height: 47px; width: 100%; padding:5px; color:blue",

            },
        )
    )
    annee_academeique = forms.CharField(max_length=100,
                widget=forms.TextInput(
                    attrs={
                        'class': "",
                        'placeholder': "Entrez l'annee academique (ex:2023-2024)",

                    },
                )
         )
    session_reussite = forms.CharField(
        widget=forms.Select(
            choices=(("premiere session", "premiere session"), ("deuxieme session", "deuxieme session")),
            attrs={
                'class': "custom-select mb-4",
                'style': "height: 47px; width: 100%; padding:5px; color:blue",

            },
        )
    )
    # attribut optionel
    session_defense = forms.CharField(
        required=False, max_length=100,

        widget=forms.TextInput(
            attrs={
                'class': "",
                'placeholder': "Entrez la session de defense (optionel)",

            },
        )
                                      )
    filiere = forms.CharField(
        required=False, max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': "",
                'placeholder': "Entrez la filiere (optionel)",

            },
        )
    )
