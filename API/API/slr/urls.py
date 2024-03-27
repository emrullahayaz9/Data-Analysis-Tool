from django.urls import path
from . import views
urlpatterns = [
   path("show/<str:username>", views.show_all_csv_files),
   path("show/detail/<str:username>/<str:csv_file_name>", views.show_csv_data),
   path("show/analysis/<str:username>/<str:csv_file_name>", views.simple_linear_regression_algorithm),
   path("<str:username>", views.upload_csv),
]
