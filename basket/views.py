from django.shortcuts import render, redirect


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)
    color = request.POST.get('product_color', None)
    basket = request.session.get('basket', {})

    if size or color:
        item = basket.get(item_id, {'items_by_size': {}, 'items_by_color': {}})
        item_by_size = item['items_by_size']
        item_by_color = item['items_by_color']
        if color in item_by_color and size in item_by_size:
            item_by_color[color][size] = item_by_color[color].get(size, 0) + quantity
            item_by_size[size][color] = item_by_size[size].get(color, 0) + quantity
        elif color in item_by_color:
            item_by_color[color][size] = quantity
            item_by_size[size] = {color: quantity}
        elif size in item_by_size:
            item_by_size[size][color] = quantity
            item_by_color[color] = {size: quantity}
        else:
            item_by_color[color] = {size: quantity}
            item_by_size[size] = {color: quantity}
        basket[item_id] = item
    else:
        basket[item_id] = basket.get(item_id, 0) + quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
