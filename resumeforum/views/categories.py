from django.views import generic

from resumeforum.models import Category


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = '_categories.html'