from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm


def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'requests/create_request.html', {'form': form})

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests/request_list.html', {'requests': requests})