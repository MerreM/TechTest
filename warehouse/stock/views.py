from stock.serializers import StockSerializer
from stock.models import Stock

from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class StockFilter(filters.FilterSet):
    min_quantity = filters.NumberFilter(
        field_name="quantity", lookup_expr='gte')
    max_quantity = filters.NumberFilter(
        field_name="quantity", lookup_expr='lte')
    in_stock = filters.NumberFilter(
        field_name="quantity", lookup_expr="gt")

    class Meta:
        model = Stock
        fields = ["sku", "name", "quantity", "price"]


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockFilter


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def update_quantity(request, pk, quantity):
    # import pdb; pdb.set_trace()
    stock = get_object_or_404(Stock, sku=pk)
    quantity = int(quantity)
    stock.quantity += quantity
    stock.save()
    serializer = StockSerializer(stock)
    return Response(data=serializer.data)
