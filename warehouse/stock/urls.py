from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from stock import views

urlpatterns = [
    path('stock/', views.StockList.as_view()),
    path('stock/<str:pk>/', views.StockDetail.as_view()),
    re_path(r'stock/(?P<pk>[\w-]+)/(?P<quantity>[\d-]+)/',
            views.update_quantity),
]

urlpatterns = format_suffix_patterns(urlpatterns)
