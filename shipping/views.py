from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import ShippingMethod, ShippingCost
from .forms import ShippingMethodForm, ShippingCostForm


def all_shippingmethods(request):
    """ A view to show all shipping methods, including sorting and search queries """

    shippingmethods = ShippingMethod.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                sizes = sizes.annotate(lower_name=Lower('name'))
            if sortkey == 'description':
                sortkey = 'lower_description'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shippingmethod = shippingmethod.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('shippingmethods'))

            queries = Q(name__icontains=query) | \
                Q(friendly_name__icontains=query)

            shippingmethods = shippingmethods.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'shippingmethods': shippingmethods,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'shipping/shippingmethods.html', context)


@login_required
def add_shippingmethod(request):
    """ Add a shipping method to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ShippingMethodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Shipping Method!')
            return redirect(reverse('shippingmethods'))
        else:
            messages.error(
                request, 'Failed to add size. Please ensure the form is valid.'
                )
    else:
        form = ShippingMethodForm()

    template = 'shipping/add_shippingmethod.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_shippingmethod(request, shippingmethod_id):
    """ Edit a Shipping method in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shippingmethod = get_object_or_404(ShippingMethod, pk=shippingmethod_id)
    if request.method == 'POST':
        form = ShippingMethodForm(request.POST, instance=shippingmethod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Shipping Method!')
            return redirect(reverse('shippingmethods'))
        else:
            messages.error(
                request,
                'Failed to update size. Please ensure the form is valid.'
                )
    else:
        form = ShippingMethodForm(instance=shippingmethod)
        messages.info(request, f'You are editing {shippingmethod.name}')

    template = 'shipping/edit_shippingmethod.html'
    context = {
        'form': form,
        'shippingmethod': shippingmethod,
    }

    return render(request, template, context)


@login_required
def delete_shippingmethod(request, shippingmethod_id):
    """ Delete a Shipping Method from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shippingmethod = get_object_or_404(ShippingMethod, pk=shippingmethod_id)
    shippingmethod.delete()
    messages.success(request, 'Shipping Method deleted!')
    return redirect(reverse('shippingmethods'))


def all_shippingcosts(request):
    """ A view to show all shipping costs, including sorting and search queries """
    shippingcosts = ShippingCost.objects.all()
    # Your sorting and filtering logic for shipping costs (similar to the shipping methods view)
    context = {
        'shippingcosts': shippingcosts,
        # Any other context data you want to pass to the template
    }
    return render(request, 'shipping/shippingcosts.html', context)


@login_required
def add_shippingcost(request):
    """ Add a shipping cost """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ShippingCostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Shipping Cost!')
            return redirect(reverse('shippingcosts'))
        else:
            messages.error(
                request, 'Failed to add shipping cost. Please ensure the form is valid.'
            )
    else:
        form = ShippingCostForm()

    template = 'shipping/add_shippingcost.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_shippingcost(request, shippingcost_id):
    """ Edit a shipping cost """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shippingcost = get_object_or_404(ShippingCost, pk=shippingcost_id)
    if request.method == 'POST':
        form = ShippingCostForm(request.POST, instance=shippingcost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Shipping Cost!')
            return redirect(reverse('shippingcosts'))
        else:
            messages.error(
                request, 'Failed to update shipping cost. Please ensure the form is valid.'
            )
    else:
        form = ShippingCostForm(instance=shippingcost)

    template = 'shipping/edit_shippingcost.html'
    context = {
        'form': form,
        'shippingcost': shippingcost,
    }
    return render(request, template, context)


@login_required
def delete_shippingcost(request, shippingcost_id):
    """ Delete a shipping cost """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shippingcost = get_object_or_404(ShippingCost, pk=shippingcost_id)
    shippingcost.delete()
    messages.success(request, 'Shipping Cost deleted!')
    return redirect(reverse('shippingcosts'))
