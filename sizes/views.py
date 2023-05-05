from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Size
from .forms import SizeForm


def all_sizes(request):
    """ A view to show all sizes, including sorting and search queries """

    sizes = Size.objects.all()
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
                sizes = sizes.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            sizes = sizes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            sizes = sizes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('sizes'))

            queries = Q(name__icontains=query) | \
                Q(friendly_name__icontains=query)

            sizes = sizes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'sizes': sizes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'sizes/sizes.html', context)


@login_required
def add_size(request):
    """ Add a size to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            size = form.save()
            messages.success(request, 'Successfully added size!')
            return redirect(reverse('size_detail', args=[size.id]))
        else:
            messages.error(
                request, 'Failed to add size. Please ensure the form is valid.'
                )
    else:
        form = SizeForm()

    template = 'sizes/add_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_size(request, size_id):
    """ Edit a size in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    size = get_object_or_404(Size, pk=size_id)
    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated size!')
            return redirect(reverse('size_detail', args=[size.id]))
        else:
            messages.error(
                request,
                'Failed to update size. Please ensure the form is valid.'
                )
    else:
        form = SizeForm(instance=size)
        messages.info(request, f'You are editing {size.name}')

    template = 'sizes/edit_size.html'
    context = {
        'form': form,
        'size': size,
    }

    return render(request, template, context)


@login_required
def delete_size(request, size_id):
    """ Delete a size from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    size = get_object_or_404(Size, pk=size_id)
    size.delete()
    messages.success(request, 'Size deleted!')
    return redirect(reverse('sizes'))
