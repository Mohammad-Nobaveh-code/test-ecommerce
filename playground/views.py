from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from tags.models import TaggedItem
from store.models import Product, Customer, Collection, Order, OrderItem


# def say_hello(request):
#     query_set = Order.objects.select_related('customer').prefetch_related(
#         'orderitem_set__product').order_by('-placed_at')[:5]
#     return render(request, 'hello.html', {'name': 'Mohammad', 'orders': list(query_set)})


# def say_hello(request):
#     queryset = Product.objects.filter(
#         id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
#     return render(request, 'hello.html', {'result': queryset})


def say_hello(request):
    # queryset = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' ')
    #                     ,F('last_name'),
    #                     function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '),
    #                     'last_name')
    # )
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects \
    .select_related('tag') \
    .filter(
        content_type = content_type,
        object_id = 1
    )
    return render(request, 'hello.html', {'name': 'Mohammad'})
