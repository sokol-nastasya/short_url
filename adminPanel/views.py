from django.shortcuts import render, get_object_or_404, redirect
from mainApp.models import Urls
from mainApp.forms import UrlsFormNew

def adminPanel(request):
	obj = Urls.objects.all()
	context = {'obj':obj, }
	return render(request, 'adminPanel/adminPanel.html', context)

def details(request, pk):
	obj = Urls.objects.get(id=pk)
	context = {'obj':obj}
	return render(request, 'adminPanel/details.html', context)

def delete(request, pk):
	object = get_object_or_404(Urls, pk=pk)
	object.delete()
	return redirect('/')

def editUrl(request, url_id):
	obj = get_object_or_404(Urls, id=url_id)
	if request.method == 'POST':
		form = UrlsFormNew(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.save()
			return redirect('/', id=url_id)
	else:
		form = UrlsFormNew(instance=obj)
	return render(request, 'adminPanel/editUrl.html', {'form':form})

