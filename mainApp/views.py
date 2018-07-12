from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F

from .models import Urls
from .forms import UrlsForm


class HomeView(View):
	def get(self, request, *args, **kwargs):
		obj = Urls.objects.all()
		# obj = Urls.objects.filter(author = request.user)
		
		query = request.GET.get("q")
		if query:
			obj = obj.filter(main_obj__icontains = query)
		paginator = Paginator(obj, 4)

		page = request.GET.get('page')
		try:
			obj_list = paginator.page(page)
		except PageNotAnInteger:
			obj_list = paginator.page(1)
		except EmptyPage:
			obj_list = paginator.page(paginator.num_pages)

		form = UrlsForm()
		context = {
			'form':form,
			'obj':obj,
			'obj_list':obj_list,
		}
		return render(request, 'mainApp/home.html', context)

	def  post(self, request, *args, **kwargs):
		form = UrlsForm(request.POST)
		context = {'form':form}
		template = 'mainApp/home.html'

		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = Urls.objects.get_or_create(url = new_url)
			obj.count +=1
			obj.save()
			context = {'obj':obj, 'created':created}
			if created:
				template = 'mainApp/success.html'
			else:
				template = 'mainApp/already-exists.html'
		
		return render(request, template, context)

class Links(View):
	def get(self, request, id_link = None, *args, **kwargs):
		args = get_object_or_404(Urls, short_link = id_link)
		return HttpResponseRedirect(args.url)