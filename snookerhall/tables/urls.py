from django.urls import path
from . import views

urlpatterns = [
    path("add_type/", views.add_table_type_view, name="add_table_type"),
    path("edit_type/<int:pk>/", views.edit_table_type_view, name="edit_table_type"),
    path("add_table/", views.add_table, name="add_table"),
    path("edit_table/<int:pk>/", views.edit_table, name="edit_table"),
    path("delete_table/<int:pk>/", views.delete_table, name="delete_table"),
    path("", views.tables_view, name="tables_view"),
]
