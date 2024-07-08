from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import TableType
from .forms import TableTypeForm


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
