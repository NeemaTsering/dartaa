from django.shortcuts import render, get_object_or_404
from .models import News
from django.utils import timezone

# Create your views here.

def index(request):
	news=News.objects.order_by('published_date')
	context={'news':news}
	return render(request, 'index/front_page.html', context)

def news_detail(request, pk):
	news=get_object_or_404(News,pk=pk)
	context={'news':news}
	return render(request, 'index/news_detail.html', context)