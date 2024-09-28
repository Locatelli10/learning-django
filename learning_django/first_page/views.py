from django.shortcuts import render, HttpResponse, redirect
from first_page.models import Evento


# Create your views here.
def first_page(request):
    return HttpResponse ('My first page!')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)


#def index(request):
#    return redirect('/agenda')