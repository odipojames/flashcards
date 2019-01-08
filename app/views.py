from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *



# Create your views here.
def index(request):

    card = Card.objects.all()
    print(Card) 
    return render(request,'index.html', {"card":card})

def card(request,card_id):
    try:
        card = Card.objects.get(id = card_id)
    except Card.DoesNotExist:
        raise Http404()
    return render(request,"card.html", {"card":card})

# @login_required(login_url='/accounts/login/')
def new_card(request):
    current_user = request.user
    if request.method == 'card':
        form = NewCardForm(request.card, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.editor = current_user
            card.save()
        return redirect('index')

    else:
        form = NewCardForm()
    return render(request, 'new_card.html', {"form": form}) 

