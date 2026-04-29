from django.shortcuts import render
from store.models import Product, Customer, Order, Collection, OrderItem
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    
    #query_set = Product.objects.all()
    #query_set.filter().filter().order_by()[:5]
    #product = Product.objects.get(pk=1) # return one object with primary key 1
    # if there is no product with pk=1, it will raise an exception, use try except to handle it 
    """try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass""" 
    #product = Product.objects.filter(pk=0).first() # return the first object with primary key 0, 
    # if there is no product with pk=0, it will return None 
    #exists = Product.objects.filter(pk=0).exists() # return True if there is a product with pk=0, 
    # otherwise return False
    #queryset = Product.objects.filter(unit_price=20) # key value
    #queryset = Product.objects.filter(unit_price__gt=20) # greater than 20
    #queryset = Product.objects.filter(unit_price__gte=20) # greater than or equal to 20
    #queryset = Product.objects.filter(unit_price__lt=20) # less than
    #queryset = Product.objects.filter(unit_price__range=(20, 30)) # between 20 and 30
    #queryset = Product.objects.filter(collection__id=1) # filter by collection id
    # queryset = Product.objects.filter(collection__id__range=(1, 5)) # filter by collection id between 1 and 5
    # queryset = Product.objects.filter(collection__title='Video Games') # filter by collection title
    #queryset = Product.objects.filter(title__icontains='coffee') # filter by title contains 'coffee', case insensitive
    # queryset = Product.objects.filter(title__istartswith='coffee') # filter by title starts with 'coffee', case insensitive
    #queryset = Product.objects.filter(title__iendswith='coffee') # filter by title ends
    #queryset = Product.objects.filter(last_update__year=2021) # filter by last update year
    # queryset = Product.objects.filter(description__isnull=True) # filter by description is null
    # ex: Customers with .com accounts
    #queryset = Customer.objects.filter(email__iendswith='.com')
    # Collections that don’t have a featured product
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # Products with low inventory (less than 10)
    #queryset = Product.objects.filter(inventory__lt=10)
    #Orders placed by customer with id = 1
    #queryset = Order.objects.filter(customer__id=1)
    # Order items for products in collection 3
    queryset = OrderItem.objects.filter(product__collection__id=3)
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
