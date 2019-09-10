from django.shortcuts import render
from .models import Cadastro
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def home(request):
    cadastros_list = Cadastro.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(cadastros_list, 15)
    try:
        cadastros = paginator.page(page)
    except PageNotAnInteger:
        cadastros = paginator.page(1)
    except EmptyPage:
        cadastros = paginator.page(paginator.num_pages)

    return render(request, "cadastro/home.html", {"cadastros": cadastros})
