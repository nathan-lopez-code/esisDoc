from django import forms


class RapportForm(forms.Form):
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "s ou hi cp ki xq",
                "placeholder": "Entrer un message"
            }
        )
    )
