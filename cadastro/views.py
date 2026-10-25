from django.shortcuts import render
from .models import Cadastro
from django.core.paginator import Paginator


def home(request):
    # pk breaks ties so pagination never repeats or skips rows.
    cadastros_list = Cadastro.objects.order_by("associado", "pk")

    paginator = Paginator(cadastros_list, 15)
    # get_page() shows page 1 for a missing or invalid number, the last page if too high.
    cadastros = paginator.get_page(request.GET.get("page"))

    return render(request, "cadastro/home.html", {"cadastros": cadastros})
