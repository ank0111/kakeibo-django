from django.urls import path
from . import views

app_name = 'kakeibo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('icategory', views.IcategoryIndexView.as_view(), name='icategory'),
    path('ecategory', views.EcategoryIndexView.as_view(), name='ecategory'),
    path('income', views.IncomeIndexView.as_view(), name='income'),
    path('expense', views.ExpenseIndexView.as_view(), name='expense'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]