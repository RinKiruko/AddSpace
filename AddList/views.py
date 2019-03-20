import uuid
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Add
from Accounts.models import User


def get_all_adds(request):
    AllAdds = Add.objects.all()
    paginator = Paginator(AllAdds, 25)

    page = request.GET.get('page')
    AddList = paginator.get_page(page)
    return render(request, 'Index.html', context={'AddList': AddList})

def get_add_page(request, id):
    add = get_object_or_404(Add,pk=id)
    context = {'add': add,
               'user': request.user}
    
    return render(request, 'AddList/AddPage.html', context)

def get_user_page(request, uuid):
    requested_user = get_object_or_404(User, Hash=uuid)
    context =  {'requested_user': requested_user,
                'user': request.user}
    return render(request, 'AddList/UserPage.html', context=context)