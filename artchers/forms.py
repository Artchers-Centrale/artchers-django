from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import district


def mailCentrale(mail):
    test = mail.split('@')
    print(test[1])
    if (test[1] == 'centrale.centralelille.fr') or (test[1] == 'enscl.centralelille.fr') or (test[1] == 'iteem.centralelille.fr') :
        return mail
    raise ValidationError(
            _("%(value)s n'est pas un mail sous le format xyz@xyz.centralelille.fr"),
            params={"value": mail},
            code="badMail"
        )



class voteForm(forms.Form):
    nom = forms.CharField(label = "Votre nom",max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Votre nom'}))
    prenom = forms.CharField(label = "Votre prénom",max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Votre prénom'}))
    mail = forms.EmailField(label="Votre mail en xyz@xyz.centralelille.fr", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Votre mail en xyz@xyz.centralelille.fr'}))
    vote = forms.ModelChoiceField(label="Votre vote est pour le district :", queryset=district.objects.all(), widget=forms.Select)

    def cleanCentrale(self):
        mailtest = self.cleaned_data["mail"]
        mailCentrale(mailtest)
        return mailtest