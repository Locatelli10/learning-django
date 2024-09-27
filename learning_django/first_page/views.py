from django.shortcuts import render, HttpResponse

# Create your views here.
def first_page(request):
    return HttpResponse ('My first page!')