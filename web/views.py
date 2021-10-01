from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm

def home(request):
	return render(request,'web/home.html')
def about(request):
	return render(request,'web/about.html')
def A_bout(request):
	if request.method =='GET':
		form=ContactForm()
	else:
		form=ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject,message,from_email,['adhiyamaanstudent3@gmail.com',from_email])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('Success')
	return render(request,'web/A_bout.html',{'form':form})


# Create your views here.
