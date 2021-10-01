from django import forms

class ContactForm(forms.Form):
	
	from_email = forms.EmailField(widget=forms.EmailInput(attrs={
		"class":"input",
		"type":"email"
		}),required=True,label="E-mail")
	subject = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text"
		}),required=True,label="subject")
	message=forms.CharField(widget=forms.Textarea(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Your message...",
		"rows":5
		}),required=True,label="") 