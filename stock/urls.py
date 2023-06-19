from django.urls import path

from stock import views

urlpatterns = [
    path('search/<str:user_input>/', views.ticker_search),
    path('data/<str:symbol>/<str:function>/', views.get_stock_data),
    # path('<str:symbol>/', views.test),
]
