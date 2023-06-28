from django import forms
from main.models import Usuario, Producto

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'descripcion', 'foto', 'categoria', 'id_usuario')