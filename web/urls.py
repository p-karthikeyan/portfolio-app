from django.urls import path
from . import views


urlpatterns=[
	path('',views.home,name='home'),
	path('Success',views.about ,name='Success'),
	path('A_bout',views.A_bout,name='A_bout')
]