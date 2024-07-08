from django.urls import path
from . import views

urlpatterns = [
    path("add_type/", views.add_table_type_view, name="add_table_type"),
    path("edit_type/<int:pk>/", views.edit_table_type_view, name="edit_table_type"),
]
