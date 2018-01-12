from django import forms
from index.models import News

class NewNews(forms.ModelForm):
	class Meta:
		model=News
		fields=('title','text','published_date',)