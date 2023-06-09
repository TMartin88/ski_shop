from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product
from sizes.models import Size
from .models import ProductSize
from .forms import ProductSizeForm


def all_product_sizes(request):
    product_sizes = ProductSize.objects.select_related('product', 'size').all()
    return render(request, 'product_sizes/list.html', {'product_sizes': product_sizes})


@login_required
def add_product_size(request):
    form = ProductSizeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_sizes:list')

    return render(request, 'product_sizes/form.html', {'form': form})


@login_required
def edit_product_size(request, product_size_id):
    product_size = get_object_or_404(ProductSize, pk=pk)
    form = ProductSizeForm(request.POST or None, instance=product_size)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_sizes:list')

    return render(request, 'product_sizes/form.html', {'form': form})


@login_required
def delete_product_size(request, product_size_id):
    product_size = get_object_or_404(ProductSize, pk=pk)

    if request.method == 'POST':
        product_size.delete()
        return redirect('product_sizes:list')

    return render(request, 'product_sizes/delete.html', {'product_size': product_size})
