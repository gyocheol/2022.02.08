from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm : django에서 기본적으로 지원해주는 회원가입
class MyMemberForm(UserCreationForm):
    # UserCreationFrame 이 가진 기본적인 필드 : username, password1, password2
    # password1 : 비밀번호 / password2 : 비밀번호 확인
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
