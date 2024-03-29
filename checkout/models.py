import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


from decimal import Decimal
from shipping.models import ShippingCost, ShippingMethod


def calculate_shipping_cost(package_weight, country_code):
    try:
        shipping_cost = ShippingCost.objects.filter(
            country=country_code,
            weight_from__lte=package_weight,
            weight_to__gt=package_weight
        ).first()

        if shipping_cost:
            return shipping_cost.get_cost(), False  # Return shipping cost and a flag indicating no flat fee applied
        else:
            flat_fee = Decimal(settings.FLAT_DELIVERY_CHARGE)
            flat_fee_flag = True
            # Return the flat fee along with the flag indicating that flat fee is applied
            return flat_fee, flat_fee_flag
    except ShippingCost.DoesNotExist:
        flat_fee = Decimal(settings.FLAT_DELIVERY_CHARGE)
        flat_fee_flag = True
        # Return the flat fee along with the flag indicating that flat fee is applied
        return flat_fee, flat_fee_flag


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    flat_fee_applied = models.BooleanField(default=False)
    shipping_method = models.CharField(max_length=255, default='Standard Shipping')
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
        )

    def get_shipping_cost(self):
        package_weight = 5  # Replace this with the actual package weight.
        return calculate_shipping_cost(package_weight, self.country.code)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self, delivery_cost=None):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0

        if delivery_cost is not None:
            # If delivery_cost is provided as an argument, use it directly
            self.delivery_cost = delivery_cost

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            self.update_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    product_size = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )  # XS, S, M, L, XL or Product Size
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
