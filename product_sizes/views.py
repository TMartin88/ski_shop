from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product, Category
from sizes.models import Size
from .models import ProductSize
from .forms import ProductSizeEditForm, ProductSizeAddForm
from django.http import JsonResponse


def all_product_sizes(request):
    product_sizes = ProductSize.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'product__name'
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
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect('all_product_sizes')

            queries = Q(
                product__name__icontains=query) | \
                Q(size__name__icontains=query) | \
                Q(category__name__icontains=query)

            product_sizes = product_sizes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'product_sizes': product_sizes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'product_sizes/all_product_sizes.html', context)


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
            return redirect(reverse('all_product_sizes'))
        else:
            # Print form errors for debugging
            print(form.errors)
            messages.error(
                request,
                'Failed to add product size. Please ensure the form is valid.'
                )
    else:
        form = ProductSizeAddForm()

    template = 'product_sizes/add_product_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def get_filtered_products(request):
    category_id = request.GET.get('category')
    products = Product.objects.filter(
        category_id=category_id).values('id', 'name')

    return JsonResponse({'products': list(products)})


def get_filtered_sizes(request):
    category_id = request.GET.get('category')

    sizes = Size.objects.filter(category_id=category_id).values('id', 'name')

    return JsonResponse({'sizes': list(sizes)})


@login_required
def edit_product_size(request, product_size_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_size = get_object_or_404(ProductSize, pk=product_size_id)
    category_name = product_size.category.name
    product_name = product_size.product.name

    if request.method == 'POST':
        if product_size_id:
            form = ProductSizeEditForm(request.POST, instance=product_size)
        else:
            form = ProductSizeAddForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product size!')
            return redirect(reverse('all_product_sizes'))
        else:
            messages.error(
                request,
                'Failed to update product size.  '
                'Please ensure the form is valid.'
                )
    else:
        if product_size_id:
            form = ProductSizeEditForm(instance=product_size)
        else:
            form = ProductSizeAddForm()
        messages.info(
            request,
            f'You are editing {product_name} - '
            '{product_size.size} - {category_name}'
            )

    template = 'product_sizes/edit_product_size.html'
    context = {
        'form': form,
        'product_size': product_size,
        'category_name': category_name,
        'product_name': product_name,
    }

    return render(request, template, context)


@login_required
def delete_product_size(request, product_size_id):
    """ Delete a product size from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_size = get_object_or_404(ProductSize, pk=product_size_id)
    product_size.delete()
    messages.success(request, 'Product Size deleted!')
    return redirect(reverse('all_product_sizes'))
