from django.forms import ModelForm
from .models import User

from django.contrib.auth.forms import UserCreationForm, UsernameField



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields  = ['name','email','phone','description','password1','password2']
        #labels = {'first_name':'Name',}


    def __init__(self, *args, **kwargs):

        super(CustomUserCreationForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})


class UserForm(ModelForm):
    class Meta:
        model = User
        fields  = ['name','email','phone','description','profile_image']


    def __init__(self, *args, **kwargs):

        super(UserForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})