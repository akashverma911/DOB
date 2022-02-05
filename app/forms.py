from django import forms


class DobForm(forms.Form):
    date_of_birth = forms.DateField(required=False)
    