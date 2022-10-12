from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_dashboard),
    path("car_book/", views.car_book),
    path("payment_method/", views.payment_method),
    path("payment_confirmation/", views.payment_confirmation),
    path("confirm_book/", views.confirm_book),
    path("provider_dashboard/", views.provider_dashboard),
    path("add_car/", views.add_car),
    path("insert_car/", views.insert_car),
    path("edit_car/<car_id>/", views.edit_car),
    path("edit_my_car/<car_id>/", views.edit_my_car),
    path("provider_account/<provider_id>/", views.provider_account),
    path("provider_account_edit/<provider_id>/", views.provider_account_edit),
    path("customer_account/<customer_id>/", views.customer_account),
    path("customer_account_edit/<customer_id>/", views.customer_account_edit),
    path("provider_car_details/<car_id>/", views.provider_car_details),
    path("contact/", views.contact),

]