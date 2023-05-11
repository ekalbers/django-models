from django.views.generic import ListView, DetailView, TemplateView
from .models import Snack


class SnacksListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks_list'


class SnacksDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        pass


