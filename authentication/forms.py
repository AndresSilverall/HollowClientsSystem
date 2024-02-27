from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateNewUser, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Nombre de usuario",
            "id": "typeUsername"
            })
        
        self.fields["email"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Email", 
            "id": "typeEmail"
            })
        
        self.fields["password1"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Contraseña", 
            "id": "typePasswor1"
            })
        
        self.fields["password2"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Repita su contraseña", 
            "id": "typePassword2"
            })


# Restablecer contraseña
class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        
        self.fields['old_password'].widget.attrs.update({
            'id': 'old_password',
            'required': True,
            'class': 'form-control form-control-ls', 
            'placeholder': "Ingrese su antigua contraseña"
            })
        
        self.fields['new_password1'].widget.attrs.update({
            'id': 'new_password1', 
            'required': True,
            'class': 'form-control form-control-ls', 
            'placeholder': "Ingrese su nueva contraseña"
            })
        
        self.fields['new_password2'].widget.attrs.update({
            'id': 'new_password2', 
            'class': 'form-control form-control-ls', 
            'required': True,
            'placeholder': "Confirme su nueva contraseña"
            })