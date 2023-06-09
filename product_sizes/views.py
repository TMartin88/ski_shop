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

    product_sizes = Size.objects.filter(category__product__isnull=False)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                product_sizes = product_sizes.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            product_sizes = product_sizes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            product_sizes = product_sizes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return HttpResponseRedirect(request.path_info)

            queries = Q(name__icontains=query) | Q(friendly_name__icontains=query)
            product_sizes = product_sizes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'product_sizes': product_sizes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'product_sizes/product_sizes.html', context)


@login_required
def add_product_size(request):
    form = ProductSizeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_sizes:list')

    return render(request, 'product_sizes/product_sizes.html', context)


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
