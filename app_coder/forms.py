from django import forms

class QuestionForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    question = forms.CharField(max_length=150, label='Pregunta')
    phone = forms.CharField(max_length=40, label='Telefono')
    email = forms.EmailField(label='Email')

class ProductForm(forms.Form):
    nameprod = forms.CharField(max_length=40, min_length=3, label='Nombre')
    price = forms.CharField(max_length=10, label='Precio')

class ClientForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Email')

