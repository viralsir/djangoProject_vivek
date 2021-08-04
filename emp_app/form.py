from django import forms


class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=55)
    address=forms.CharField(max_length=150)
    phno=forms.CharField(max_length=10)
    salary=forms.IntegerField()
