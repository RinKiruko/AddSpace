from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect

from AddList.models import Add
from Accounts.models import User
from AddList.views import get_add_page


@login_required(login_url='account/login/')
def get_account_main_page(request):
	user = request.user
	posted_adds = user.add.all()
	return render(request, 'Accounts/main_page.html', 
				  context={'User': request.user, 'AddList': posted_adds})

def register(request):
	if not request.POST:
		return render(request, 'Accounts/registration.html')
	else:
		new_user_form = RegisterUserForm(request.POST)
		if register_user_form.is_valid():
			register_user_form.save()
		else:
			return render(request, 'Accounts/registration.html', 
						context={'RegistrationForm':new_user_form})
		

@login_required(login_url='account/login/')
def create_add(request):
	if request.method == 'GET':
		return render('Accounts/create_add.html')

	add_data = request.POST
	add_data['Author'] = request.user
	create_add_form = CreateAddForm(add_data)
	if create_add_form.is_valid():
		create_add_form.save()
		return HttpResponseRedirect('account/')
	else:
		return render(request, 'Accounts/create_add.html',
					  context={'CreateForm':create_add_form})

@login_required(login_url='account/login/')
def edit_add(request, add_id):
	add = Add.object.get(pk=add_id)	
	if add.Author.id == request.user.id:
		if request.method == 'GET':
			edit_add_form = EditAddForm(add)
			return render(request, 'Accounts/create_add.html', context={'EditForm': edit_add_form})
		else:
			edit_add_form = EditAddForm(request.POST)
			if edit_add_form.is_valid():
				edit_add_form.save()
				return HttpResponseRedirect(reverse('Accounts:AllPostedAdds'))
	else:
		return HttpResponseRedirect(reverse('AddList:GetAdd',kwargs={'id': add_id}))

@login_required(login_url='account/login')
def delete_add(request, add_id):
	add = Add.objects.get(pk=add_id)	
	if add.Author.id == request.user.id:
		add.delete()
	else:
		HttpResponseRedirect(reverse('Accounts:GetAdd', kwargs={'id':add_id}))