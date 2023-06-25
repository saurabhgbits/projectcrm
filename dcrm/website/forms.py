from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# create add record form 
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}), label="")
    email = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}), label="")
    address = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}), label="")
    city =forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"city","class":"form-control"}), label="")
    state =forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget =forms.widgets.TextInput(attrs={"placeholder":"Zip Code","class":"form-control"}), label="")

    class Meta: 
        model = Record
        exclude = ("user",)

