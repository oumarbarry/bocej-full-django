from django import forms
from center.models import Center
from login.models import UserCenter

class CenterForm(forms.ModelForm):
    c_title = forms.CharField()
    c_address = forms.CharField()
    c_email = forms.EmailField()
    c_phone = forms.CharField()

    c_title.widget.attrs.update(
        {'type': 'text', 'name': 'c_title', 'class': 'form-control', 'placeholder': "Titre du centre", 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    c_address.widget.attrs.update(
        {'type': 'text', 'name': 'c_address', 'class': 'form-control', 'placeholder': "Addresse (Ville, Quartier)", 'required': 'True'}
    )
    c_email.widget.attrs.update(
        {'type': 'email', 'name': 'c_email', 'class': 'form-control', 'placeholder': "Email du centre", 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    c_phone.widget.attrs.update(
        {'type': 'tel', 'name': 'c_phone', 'class': 'form-control', 'placeholder': "Numero de telephone du centre", 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    class Meta():
    	model = Center
    	fields = '__all__'
    
class  UserCenterForm(forms.ModelForm):
    full_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField()
    full_name.widget.attrs.update(
        {'type': 'text', 'name': 'full_name', 'class': 'form-control', 'placeholder': "Nom & Prenom(s)", 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    username.widget.attrs.update(
        {'type': 'text', 'name': 'username', 'class': 'form-control', 'placeholder': "Nom d'utilisateur", 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    email.widget.attrs.update(
        {'type': 'email', 'name': 'email', 'class': 'form-control', 'placeholder': "Email", 'data-error': '*Veuillez renseigner ce champ.'}
    )
    password.widget.attrs.update(
    	{'type': 'password', 'name': 'password', 'class': 'form-control', 'placeholder': 'Mot de passe', 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )
    phone.widget.attrs.update(
    	{'type': 'tel', 'name': 'phone', 'class': 'form-control', 'placeholder': 'Numero de telephone du directeur', 'required': 'True', 'data-error': '*Veuillez renseigner ce champ.'}
    )

    class Meta():
    	model = UserCenter
    	fields = '__all__'
    
