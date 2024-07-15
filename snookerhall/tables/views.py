from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import TableType, Table
from .forms import TableTypeForm, TableForm


def add_table_type_view(request):
    table_types = TableType.objects.all()
    if request.method == "POST":
        form = TableTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Table added successfully")
            return redirect("home")
        else:
            messages.error(
                request, "There was a problem adding the table, please try again."
            )
    else:
        form = TableTypeForm()

    context = {
        "form": form,
        "table_types": table_types,
    }
    return render(request, "tables/add_table_type.html", context)


def edit_table_type_view(request, pk):
    table_type = get_object_or_404(TableType, pk=pk)
    if request.method == "POST":
        form = TableTypeForm(request.POST, instance=table_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Table type updated successfully")
            return redirect("add_table_type")
        else:
            messages.error(
                request,
                "There was a problem updating the table type, please try again.",
            )
    else:
        form = TableTypeForm(instance=table_type)

    context = {
        "form": form,
        "table_type": table_type,
    }
    return render(request, "tables/edit_table_type.html", context)


def delete_table_type(request, pk):
    table_type = get_object_or_404(TableType, pk=pk)
    if request.method == "POST":
        table_type.delete()
        messages.success(request, "Table Type deleted successfully")
        return redirect("add_table_type")
    return render(request, "tables/delete_table_type.html", {"table_type": table_type})


def add_table(request):
    tables = Table.objects.all()
    if request.method == "POST":
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Table added successfully")
            return redirect("add_table")
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error)
    else:
        form = TableForm()

    context = {
        "form": form,
        "tables": tables,
    }
    return render(request, "tables/add_table.html", context)


def edit_table(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            messages.success(request, "Table updated successfully")
            return redirect("add_table")
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error)
    else:
        form = TableForm(instance=table)

    context = {
        "form": form,
        "table": table,
    }
    return render(request, "tables/edit_table.html", context)


def delete_table(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == "POST":
        table.delete()
        messages.success(request, "Table deleted successfully")
        return redirect("add_table")
    return render(request, "tables/delete_table.html", {"table": table})


def tables_view(request):
    table_types = TableType.objects.all()
    tables_by_type = {}

    for table_type in table_types:
        tables = Table.objects.filter(table_type=table_type)
        tables_by_type[table_type] = tables

    context = {"tables_by_type": tables_by_type}
    return render(request, "tables/tables_view.html", context)
