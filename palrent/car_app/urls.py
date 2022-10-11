from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_dashboard),
    path("search/", views.search),
    path("search_result/", views.search_result),
    path("car_select/<car_id>/", views.car_select),
    path("car_details/<car_id>/", views.car_details),
    path("car_book/", views.car_book),
    path("payment_method/", views.payment_method),
    path("payment_confirmation/", views.payment_confirmation),
    path("confirm_book/", views.confirm_book),
    path("provider_dashboard/", views.provider_dashboard),
    path("add_car/", views.add_car),
    path("insert_car/", views.insert_car),
    path("edit_car/<car_id>/", views.edit_car),
    path("edit_my_car/<car_id>/", views.edit_my_car),

]