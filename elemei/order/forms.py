from  django import forms
from  order.models import *
from django.forms import PasswordInput,ImageField
class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_name','user_image','user_mobile','user_password','user_pay_password']
        widgets = {
            'user_password':PasswordInput(),
            'user_pay_password':PasswordInput(),
        }
        error_messages={
            'user_name':{'required':'用户名不能为空'},
            'user_image':{'required':'头像不能为空'},
            'user_mobile':{'required':'电话不能为空'},
            'user_password':{'required':'密码不能为空'},
            'user_pay_password':{'required':'支付密码不能为空'},
        }

