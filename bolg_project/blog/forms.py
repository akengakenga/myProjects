from django import forms
from django.forms import Textarea

from .models import *
class ArticltForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        fields = ['art_title','art_content']
        widgets = {'art_content': Textarea(attrs={'cols':80,'rows':20})}
        error_messages={
            'art_title' :{'min_length':3,'required': "标题不能为空",'max_length':"标题长度不能超过30"},
            'art_content':{'required':"文章内容不能为空",},

        }

