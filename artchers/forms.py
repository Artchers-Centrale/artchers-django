from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import district


def mailCentrale(mail):
    test = mail.split('@')
    print(test[1])
    if (test[1] == 'centrale.centralelille.fr') or (test[1] == 'enscl.centralelille.fr') or (test[1] == 'iteem.centralelille.fr') :
        return
    raise ValidationError(
            _("%(value)s n'est pas un mail sous le format xyz@xyz.centralelille.fr"),
            params={"value": mail},
        )



class voteForm(forms.Form):
    mail = forms.EmailField(label="Votre mail en xyz@xyz.centralelille.fr", validators=[mailCentrale], max_length=100, widget=forms.TextInput(attrs={'placeholder': 'xyz@xyz.centralelille.fr'}))
    vote = forms.ModelChoiceField(queryset=district.objects.all(), widget=forms.Select)