from django.shortcuts import render
from .forms import NewNews 
from index.models import News
# Create your views here.
def new_news(request):
	if request.method=="POST":
		form=NewNews(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
	else:
		form=NewNews()
		context={"form":form}
		return render(request, 'info/new_news.html', context)

def articles(request):
	news=News.objects.order_by('published_date')
	context={"news":news}
	return render(request, 'info/article_list.html', context)