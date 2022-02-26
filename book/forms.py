from dataclasses import field, fields
from django import forms
from book.models import Book,Employee

# class StudentForms(forms.Form):
#     first_name = forms.CharField(max_length = 100)
#     last_name = forms.CharField(max_length = 150)
#     roll_number = forms.IntegerField(help_text="Enter 4 difgit number")
#     password = forms.CharField(widget = forms.PasswordInput())

# print(StudentForms())


class StudentForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

CITY = (
    ('', 'Choose...'),
    ('MI', 'Mumbai'),
    ('Pn', 'Pune'),
    ('Bn', 'Bangole')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label = 'Address',
        widget = forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    # city = forms.CharField()
    city = forms.ChoiceField(choices=CITY)
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
#this is for Book 
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # We can Exclude some values using
        # exclude = ("price")


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#