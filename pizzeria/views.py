from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product, Category
from rest_framework import generics


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    category_queryset = Category.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):

        products_from_categories = {}

        for category in self.category_queryset:
            new_category = Product.objects.filter(category = category.title)
            products_from_categories[category.title] = new_category
        return Response({'products': products_from_categories},
                        template_name='product-list.html' )


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        ingredients = self.object.ingredients

        if ingredients:
            ingredient_list = ingredients.split(',')

            formatted_ingredient_list = []

            for ingredient in ingredient_list:
                formatted_ingredient_list.append(ingredient.strip())
        else:
            formatted_ingredient_list = []

        return Response({'product': self.object, 'ingredients': formatted_ingredient_list}, template_name = 'product-detail.html')

