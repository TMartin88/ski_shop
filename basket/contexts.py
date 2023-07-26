from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

from checkout.models import calculate_shipping_cost

from django.contrib import messages


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    package_weight = 0  # Initialize the package weight
    basket = request.session.get('basket', {})

    # Get the user (if logged in)
    user = request.user

    # Initialize country code with 'Ireland' as default
    country_code = 'Ireland'

    # Get the value of 'flat_fee_applied' with a default value of False if not present
    flat_fee_applied = False

    # Check if the user is logged in and has a profile with a country code
    if user.is_authenticated:
        # Assuming the user's profile model has a 'country' field with the country code
        # Replace 'Profile' with the actual name of your profile model
        if hasattr(user, 'userprofile') and hasattr(user.userprofile, 'default_country'):
            country_code = user.userprofile.default_country.code

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            package_weight += item_data * product.package_weight  # Update package weight
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                package_weight += quantity * product.package_weight  # Update package weight
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total == 0:
        # Empty basket, no delivery charge
        delivery = 0
        free_delivery_delta = 0
    else:
        if total < settings.FREE_DELIVERY_THRESHOLD:
            # delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            # Calculate the shipping cost based on the package weight and country code
            delivery, flat_fee_applied = calculate_shipping_cost(package_weight, country_code)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
            # Check if a flat fee is applied and add a message if so
            if flat_fee_applied:
                messages.add_message(request, 20, "Flat Delivery Charge is applied because either you are not logged in or we have no normal delivery to your country.")
        else:
            delivery = 0
            free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'package_weight': package_weight,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'flat_fee_applied': flat_fee_applied,  # Add flat_fee_applied to the context
    }

    return context
