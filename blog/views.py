from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from blog.models import Article


def home(request):
    postList = Article.objects.filter(visible='1')
    paginator = Paginator(postList, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context={
        "articles": articles,
        "text":  "Главная страница блога",

    }

    return render(request, "base/homesite.html",context)
def single(request,id=None):
    article = get_object_or_404(Article, id=id)

    context = {
        "article": article,
    }
    return render(request,"base/singleread.html",context)
def add_form(request):

    return render(request,"base/add_site.html")

# Create your views here.
