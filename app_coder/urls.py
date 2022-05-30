from django.urls import path
from app_coder import views


app_name='app_coder'
urlpatterns = [
    # Django documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView
    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.
    path('', views.index, name="Index"),
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/detail', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete'),
    path('clients', views.ClientListView.as_view(), name='client-list'),
    path('client/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('client/<int:pk>/detail', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update', views.ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client-delete'),
    path('questions', views.questionform, name="question-form"),
    path('search', views.search, name='Search'),
]