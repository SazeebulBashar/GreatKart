from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('place-order/', views.place_order, name="place_order"),
    path('payments/<int:order_id>', views.payments, name="payments"),
]
