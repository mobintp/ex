from django.shortcuts import render
from .models import Article
# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = { "year": year, "month": month, "articles_list": a_list}
    return render(request, "news/month_archive.html", context)