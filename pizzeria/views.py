from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product, Category
from rest_framework import generics
from cart.forms import AddToCartForm
from rest_framework.views import APIView


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



class ProductDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request: Request, pk):

        self.product = get_object_or_404(Product, id=pk)
        ingredients = self.product.ingredients

        form = AddToCartForm(initial={'product': self.product})

        if ingredients:
            ingredient_list = ingredients.split(',')

            formatted_ingredient_list = []

            for ingredient in ingredient_list:
                formatted_ingredient_list.append(ingredient.strip())
        else:
            formatted_ingredient_list = []

        return Response({'product': self.product, 'ingredients': formatted_ingredient_list, 'form': form}, template_name = 'product-detail.html')
#
# class ProductDetail(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     renderer_classes = [TemplateHTMLRenderer]
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         ingredients = self.object.ingredients
#
        # form = AddToCartForm(initial={'product': self.object})
        #
        # if ingredients:
        #     ingredient_list = ingredients.split(',')
        #
        #     formatted_ingredient_list = []
        #
        #     for ingredient in ingredient_list:
        #         formatted_ingredient_list.append(ingredient.strip())
        # else:
        #     formatted_ingredient_list = []
#
#         return Response({'product': self.object, 'ingredients': formatted_ingredient_list, 'form': form}, template_name = 'product-detail.html')
#
#     def post(self, request, *args, **kwargs):
#
#         self.object = self.get_object()
#         ingredients = self.object.ingredients
#
#         form = AddToCartForm(initial={'product': self.object})
#         if form.is_valid():
#             form.save()
#
#         if ingredients:
#             ingredient_list = ingredients.split(',')
#
#             formatted_ingredient_list = []
#
#             for ingredient in ingredient_list:
#                 formatted_ingredient_list.append(ingredient.strip())
#         else:
#             formatted_ingredient_list = []
#
#         return Response({'product': self.object, 'ingredients': formatted_ingredient_list, 'form': form},
#                         template_name='product-detail.html')
#
#
