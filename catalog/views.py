from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Book,Author,BookInstance,Genre
from .forms import f
# Create your views here.
def index(request):
  n_b = Book.objects.count()
  n_i = BookInstance.objects.count()
  n_i_a = BookInstance.objects.filter(status__exact='a').count()
  n_a = Author.objects.count()
  c = {'n_b': n_b,'n_i': n_i, 'n_i_a':n_i_a,'n_a':n_a}
  return render(request, 'index.html',context = c)

class l(generic.ListView):
  model = Book

def author(request):
  n= Author.objects.all();
  ni = {'n' : n}
  return render(request,'au.html',context=ni);

class BookDetailView(generic.DetailView):
  model = Book

def a(request,pk=None):
  n = Author.objects.all()
  m = {'a':''}
  for i in n:
   if i.id == pk:
      m['a'] = i
  return render(request, 's.html' ,context=m)


def re(request):
 if request.method == 'POST':
    l = f(request.POST)
    if l.is_valid():
      return HttpResponse(request.POST['na'])
 else:
    l = f()
 return render(request,'f.html',{'f':l})
