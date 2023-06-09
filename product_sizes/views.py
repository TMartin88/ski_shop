from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product, Category
from sizes.models import Size
from .models import ProductSize
from .forms import ProductSizeForm


def all_product_sizes(request):
    """ A view to show all product sizes, including sorting and search queries """

    product_sizes = ProductSize.objects.select_related('product', 'size', 'category')

    query = request.GET.get('q')
    categories = request.GET.getlist('category')
    sort = request.GET.get('sort', 'name')
    direction = request.GET.get('direction')

    if query:
        queries = Q(size__name__icontains=query) | Q(size__friendly_name__icontains=query) | Q(category__name__icontains=query)
        product_sizes = product_sizes.filter(queries)

    if categories:
        product_sizes = product_sizes.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if sort == 'name':
        sortkey = 'size__name'
    elif sort == 'category':
        sortkey = 'category__name'
    else:
        sortkey = 'product__name'

    if direction == 'desc':
        sortkey = f'-{sortkey}'

    product_sizes = product_sizes.order_by(sortkey)

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    context = {
        'product_sizes': product_sizes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'product_sizes/product_sizes.html', context)


@login_required
def add_product_size(request):
    """ Add a product size """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductSizeForm(request.POST)
        if form.is_valid():
            product_size = form.save()
            messages.success(request, 'Successfully added product size!')
            return redirect(reverse('product_sizes'))
        else:
            messages.error(request, 'Failed to add product size. Please ensure the form is valid.')
    else:
        form = ProductSizeForm()

    template = 'product_sizes/add_product_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


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
