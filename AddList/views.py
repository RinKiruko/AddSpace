from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Add
from Accounts.models import User


def get_all_adds(request):
    AllAdds = Add.objects.all()
    paginator = Paginator(AllAdds, 25)

    page = request.GET.get('page')
    AddList = paginator.get_page(page)
    context={'AddList': AddList, 'User':request.user}
    return render(request, 'AddList/index.html', context=context)

def get_add_page(request, id):
    add = get_object_or_404(Add,pk=id)
    context = {'Add': add,
               'User': request.user}
    
    return render(request, 'AddList/add_page.html', context)

def get_user_page(request, id):
    requested_user = get_object_or_404(User, pk=id).order_by('PostingDate')
    if requested_user == request.user:
        return HttpResponseRedirect(reverse('Accounts:AllPostedAdds'))
    context =  {'AddList': requested_user.adds.all().order_by('PostingDate'),
                'RequestedUser': requested_user,
                'User': request.user}
    return render(request, 'AddList/user_page.html', context=context)