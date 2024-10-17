from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from store.models import Category, Product


# ეს არის იმისათვის რომ ფასები გაფილტროს ოპტიმალურად
class PriceRangeFilter(admin.SimpleListFilter):
    title = "Price Range"
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        return [
            ("100-1000", "range from 100 to 1000"),
            ("1000-2000", "range from 1000 to 2000"),
            ("2000-3000", "range from 2000 to 3000"),
            ("3000-10000", "range from 3000 to 10000"),
            ("10000+", "range from 100000"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "100-1000":
            return queryset.filter(
                product_price__gte=100,
                product_price__lte=500,
            )
        if self.value() == "1000-2000":
            return queryset.filter(
                product_price__gte=1000,
                product_price__lte=2000,
            )
        if self.value() == "2000-3000":
            return queryset.filter(
                product_price__gte=2000,
                product_price__lte=3000,
            )
        if self.value() == "3000-10000":
            return queryset.filter(
                product_price__gte=3000,
                product_price__lte=10000,
            )
        if self.value() == "10000+":
            return queryset.filter(
                product_price__gte=10000,
            )


# კატეგორიის ადმინისთვის ჯობს MPTT-ის ადმინი დავუტოვოთ და დავამატოთ რაღაცები.
@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    list_display=(
        'tree_actions',
        'indented_title',
    )
    list_display_links=(
        'indented_title',
    )
    list_filter = ('parent',)
    list_select_related = ('parent',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_quantity', 'get_total_price')
    list_filter = [PriceRangeFilter]
    search_fields = ('product_name', 'product_category__category_name')
    list_per_page = 10

    @admin.display(description="ჯამური ფასი")
    def get_total_price(self, obj):
        return obj.product_price*obj.product_quantity
