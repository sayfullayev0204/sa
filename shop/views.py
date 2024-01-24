from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Product,Category
from .forms import *
from django.db.models import Q
from hitcount.views import HitCountDetailView,HitCountMixin
from hitcount.utils import get_hitcount_model

def home(request):

    object_list = Product.objects.all()
    object_list1 = Category.objects.all()
    context = {'object_list': object_list , 'object_list1': object_list1}
    return render(request, 'home.html', context)



class ListView(ListView):
    template_name = 'list.html'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(HitCountDetailView):
    model = Product
    template_name = 'detail.html'
    count_hit = True
    def get(self, request, *args, **kwargs):
        print("ArticleDetailView is called!")
        return super().get(request, *args, **kwargs)


class DeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'  # corrected typo in the template name
    success_url = reverse_lazy('home')

def Create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'new.html', {'form': form})

class ListView(ListView):
    
    template_name = 'list.html' 
    def get_queryset(self): 
        queryset = Product.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset=queryset.filter(Q(nomi__contains=q) )
        return queryset

def category_list(request):
    
    categories = Category.objects.all()
    return render(request, 'lists.html', {'categories': categories})