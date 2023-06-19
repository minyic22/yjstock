from django.urls import path

from stock import views

urlpatterns = [
    path('time_series/<str:symbol>/<str:function>/', views.get_time_series),
    path('search/<str:user_input>/', views.ticker_search),
    path('<str:symbol>', views.test),
    path('test/', views.test)
]
