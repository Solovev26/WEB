from .models import UserData, Message
from django.forms import ModelForm, TextInput, Textarea


class UserDataForm(ModelForm):
  class Meta:
    model = UserData
    fields = ["f_name", "l_name", "e_mail", "password"]
    widgets = {"f_name": TextInput(attrs={
                  'placeholder':"Ivan",
                }),
               "l_name": TextInput(attrs={
                  'placeholder':"Ivanov"
                }),
               "e_mail": TextInput(attrs={
                  'placeholder':"IvanIvanov@mail.ru"
                }),
               "password": TextInput(attrs={
                  'placeholder':"*****",
                  'type': "password"
                }),
              }

class MsgForm(ModelForm):
  class Meta:
    model = Message
    fields = ["f_name", "e_mail", "msg"]
    widgets = {"f_name": TextInput(attrs={
                  'placeholder':"Ivan",
                }),
               "e_mail": TextInput(attrs={
                  'placeholder':"IvanIvanov@mail.ru"
                }),
               "msg": Textarea(attrs={
                }),
              }
