from django.http import JsonResponse
from .models import Order


def index(request):
    orders = Order.objects.all()
    order_list = []
    for order in orders:
        order_dict = {
            "შეკვეთის ID": order.id,
            "შეკვეთის თარიღი": order.order_date,
            "შეკვეთის სტატუსი": order.order_status,
            "პროდუქტის ID": order.product_id
        }
        order_list.append(order_dict)
        order_dict = {}
    return JsonResponse(
        order_list,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )


def individual_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_dict = {
        "შეკვეთის ID": order.id,
        "შეკვეთის თარიღი": order.order_date,
        "შეკვეთის სტატუსი": order.order_status,
        "პროდუქტის ID": order.product_id,
        "პროდუქტის რაოდენობა": order.product_quantity,
        "შეკვეთის მისამართი": order.order_address,

    }
    return JsonResponse(order_dict, json_dumps_params={'ensure_ascii': False})
