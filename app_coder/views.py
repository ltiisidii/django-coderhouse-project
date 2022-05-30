from django.shortcuts import  render
from django.http import HttpResponse
from django.views.generic import edit
from app_coder.forms import ProductForm, ClientForm, QuestionForm
from app_coder.models import Product, Client, Question
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.forms.models import model_to_dict

###################### Home ###################### 

def index(request):
    return render(request, "app_coder/index.html")

###################### Product ###################### 

class ProductListView(ListView):
    model = Product
    template_name= "app_coder/product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name= "app_coder/product_detail.html"

class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('app_coder:product-list')
    fields = ["nameprod", "price"]

class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy('app_coder:product-list')
    fields = ["nameprod", "price"]

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('app_coder:product-list')

###################### Clients ###################### 

class ClientListView(ListView):
    model = Client
    template_name= "app_coder/client_list.html"

class ClientDetailView(DetailView):
    model = Client
    template_name= "app_coder/client_detail.html"    

class ClientCreateView(CreateView):
    model = Client
    success_url = reverse_lazy('app_coder:client-list')
    fields = ["name", "last_name", "email"]

class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy('app_coder:client-list')
    fields = ["name", "last_name", "email"]

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('app_coder:client-list')

###################### Question ###################### 

def questionform(request):
    if request.method == 'POST':
        questions_form = QuestionForm(request.POST)
        print(questions_form)
        if  questions_form.is_valid:
            information = questions_form.cleaned_data
            questions = questions(name=information['nombre'], consulta=information['consulta'], phone=information['telefono'], email=information['email'])
            questions.save()
            return render(request, 'app_coder/index.html')
    else:
        questions_form= QuestionForm()
    return render(request, 'app_coder/question_form.html', {'questions_form': questions_form})

###################### Search ###################### 

def search(request):
    context_dict = dict() # evita que se rompa el search cuando se hace una busqueda vacia
    if request.GET['product_text_search']:
        print(request.__dict__)
        search_param = request.GET['text_search']
        products = Product.objects.filter(nameprod__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['product_price_search']:
        search_param = request.GET['product_price_search']
        products = Product.objects.filter(price__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['product_all_search']:
        search_param = request.GET['product_all_search']
        query = Q(nameprod__contains=search_param)
        query.add(Q(price__contains=search_param), Q.OR)
        products = Product.objects.filter(query)
        context_dict = {
            'products': products
        }
    elif request.GET['client_text_search']:
        search_param = request.GET['client_text_search']
        clients = Client.objects.filter(name__contains=search_param)
        context_dict = {
            'clients': clients
        }
    elif request.GET['client_last_name_search']:
        search_param = request.GET['client_last_name_search']
        clients = Client.objects.filter(last_name__contains=search_param)
        context_dict = {
            'clients': clients
        }
    elif request.GET['client_email_search']:
        search_param = request.GET['client_email_search']
        clients = Client.objects.filter(email__contains=search_param)
        context_dict = {
            'clients': clients
        }
    elif request.GET['client_all_search']:
        search_param = request.GET['client_all_search']
        query = Q(name__contains=search_param)
        query.add(Q(last_name__contains=search_param), Q.OR)
        query.add(Q(email__contains=search_param), Q.OR)
        clients = Client.objects.filter(query)
        context_dict = {
            'clients': clients
        }    
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/index.html",
    )