from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import *


class IndexView(TemplateView):
    template_name = 'kakeibo/index.html'


class IcategoryIndexView(ListView):
    template_name = 'kakeibo/notyet.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.order_by('date')


class EcategoryIndexView(ListView):
    model = ECategory

    def get_queryset(self):
        return ECategory.objects.order_by('id')


class ECategoryCreateView(CreateView):
    template_name='kakeibo/ecategory/e'

class IncomeIndexView(ListView):
    template_name = 'kakeibo/notyet.html'
    context_object_name = 'expenses'
    
    def get_queryset(self):
        return Expense.objects.order_by('date')


class ExpenseIndexView(ListView):
    template_name = 'kakeibo/notyet.html'
    context_object_name = 'expenses'
    
    def get_queryset(self):
        return Expense.objects.order_by('date')
class DetailView(DetailView):
    model = Expense
    template_name='kakeibo/detail.html'
