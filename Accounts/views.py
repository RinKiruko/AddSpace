from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from AddList.models import Add

from .forms import UserModelForm
from .forms import AddModelForm


@login_required
def get_account_main_page(request):
    user = request.user
    posted_adds = user.adds.all().order_by('PostingDate')
    return render(request, 'Accounts/main_page.html',
                  context={'User': request.user, 'AddList': posted_adds})


def register(request):
    if not request.POST:
        return render(request, 'Accounts/registration.html',
                      context={'RegistrationForm': UserModelForm()})
    else:
        registrating_user = UserModelForm(request.POST)
        if registrating_user.is_valid():
            new_user = registrating_user.save()
            new_user.set_password(request.POST['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('Accounts:Login'))
        else:
            return render(request, 'Accounts/registration.html',
                          context={'RegistrationForm': registrating_user})


@login_required
def create_add(request):
    if request.method == 'GET':
        return render(request, 'Accounts/create_add.html',
                      context={'CreateForm': AddModelForm()})

    add_data = request.POST.dict()
    new_add_form = AddModelForm(add_data)
    if new_add_form.is_valid():
        Author = request.user
        new_add = new_add_form.save()
        Author.adds.add(new_add)
        return HttpResponseRedirect(reverse('Accounts:AllPostedAdds'))
    else:
        return render(request, 'Accounts/create_add.html',
                      context={'CreateForm': new_add_form})


@login_required
def edit_add(request, add_id):
    add = Add.objects.get(pk=add_id)
    if add.Author == request.user:
        if request.method == 'GET':
            edit_add_form = AddModelForm(instance=add)
            return render(request, 'Accounts/create_add.html', context={'CreateForm': edit_add_form})
        else:
            edited_add = AddModelForm(request.POST)
            if edited_add.is_valid():
                edited_add.save()
                return HttpResponseRedirect(reverse('Accounts:AllPostedAdds'))
    else:
        return HttpResponseRedirect(reverse('AddList:GetAdd', kwargs={'id': add_id}))


@login_required
def delete_add(request, add_id):
    add = Add.objects.get(pk=add_id)
    if add.Author == request.user:
        add.delete()
        return HttpResponseRedirect(reverse("Accounts:AllPostedAdds"))
    else:
        return HttpResponseRedirect(reverse('Accounts:GetAdd', kwargs={'id': add_id}))