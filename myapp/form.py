from django import forms
from .models import Contact

class MyContact(forms.ModelForm):

    class Meta:
        model = Contact
        fields=['name','phone','email','message']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control', 'class':'email_text','placeholder':'name'}),
     'phone':forms.NumberInput(attrs={'class':'form-control','class':'email_text','placeholder':'Phone_number'}),
     'email':forms.EmailInput(attrs={'class':'form-control','class':'email_text','placeholder':'Email'}),
     'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':"Message" ,'rows':"5" ,'id':"comment", 'name':"Message"}),
     
    }
    
    