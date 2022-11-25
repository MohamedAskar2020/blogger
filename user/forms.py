from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreateForm(forms.ModelForm):
    
    username = forms.CharField(max_length=30, label="اسم المستخدم", help_text="اسم المستخدم يجب ألا يحتوي على مسافات.")
    email = forms.EmailField(label="البريد الالكتروني")
    first_name = forms.CharField(max_length=100, label="الاسم الأول")
    last_name = forms.CharField(max_length=100, label="الاسم الأخير")
    password1 = forms.CharField(min_length= 8, label="كلمة المرور", widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, label="تأكيد كلمة المرور", widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("كلمة المرور غير متطابقة")
        return cd['password2']

    def clean_username(self):
        
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError("اسم المستخدم موجود مسبقا")
        return cd['username']    

class LoginForm(forms.ModelForm):
    
    username = forms.CharField(label="اسم المستخدم")
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
class UserUpdateForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=100, label="الاسم الأول")
    last_name = forms.CharField(max_length=100, label="الاسم الأخير")
    email = forms.EmailField(label="البريد الالكتروني")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('image',)