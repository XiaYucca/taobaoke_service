from django import forms

class AddForm(forms.Form):
    print "addform"
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    image = forms.ImageField()
