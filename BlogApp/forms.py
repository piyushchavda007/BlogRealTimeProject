from django import forms
from BlogApp.models import Comment

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
 		model=Comment
 		fields=('name','email','body')




# from django import forms
# from .models import *
# class HotelForm(forms.ModelForm):
#     class Meta:
#         model = Hotel
#         fields = ['name', 'hotel_Main_Img']