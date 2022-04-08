from django.urls import path


from handler.views import StockView

urlpatterns = [
    path('',StockView.as_view())
]