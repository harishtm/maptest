from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from apptest.models import *
from django.core.validators import RegexValidator



class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput, required=True)
        self.fields['description'] = forms.CharField(widget=forms.Textarea)
        self.fields['phone1'] = forms.CharField(max_length=30, required=True,
                                validators=[RegexValidator
                                        (regex='^[0-9]*$',
                                        message='Username must be Alphanumeric',
                                        code='invalid_username'
                                        ),
                                    ])
        self.fields['phone1'].label = "Phone Number"
        self.fields['address1'] = forms.CharField(widget=forms.Textarea)
        self.fields['address1'].label = "Address"
        self.fields['pincode'] = forms.CharField()
        self.fields['state'] = forms.CharField()
        self.fields['country'] = forms.CharField()

        for fieldname in ['username']:
           self.fields[fieldname].help_text = None


    class Meta:
        model = User

        exclude = ('date_joined', 'groups', 'is_active', 'is_staff', \
                    'last_login', 'user_permissions', 'logentry',\
                    'is_superuser')

        fields = ('first_name', 'last_name', 'email', \
                    'username', 'password')

