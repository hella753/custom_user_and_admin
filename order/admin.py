from django.contrib import admin
from order.models import Order, UserCart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_date', 'product', 'get_total_price')
    list_filter = ('order_status',)
    list_select_related = ('product',)
    search_fields = ('product__product_name', 'id')
    list_per_page = 10

    @admin.display(description="ჯამური ფასი")
    def get_total_price(self, obj):
        return obj.product_quantity*obj.product.product_price


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_select_related = ('user',)
    search_fields = ('user__username',)
    list_per_page = 10


