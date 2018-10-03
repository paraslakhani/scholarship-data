from django.shortcuts import render,redirect

# Create your views here.
from .forms import UserDataForm
def user_data(request):
	if request.method == "POST":
		form = UserDataForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user_data')
	else:
		form = UserDataForm()
	return(render(request,'user_data.html',{'form':form}))