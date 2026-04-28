from django.db import models

class Promotion(models.Model):
    """Model representing a promotion."""
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # product_set is the default name for the reverse relationship from Product to Promotion, 
    # we can change it with related_name- products

class Collection(models.Model):
    """Model representing a collection of products."""
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    # if we delete a product that is featured in a collection, we set the featured_product to null, 
    # we do not delete the collection, and we do not set the featured_product to another product, 
    # we just set it to null, and we do not want to have a reverse relationship from Product to Collection, 
    # so we set related_name to '+'

class Product(models.Model):
    """Model representing a product in the store."""
    title = models.CharField(max_length=255)
    # slug is a short label for something, containing only letters, numbers, 
    # underscores or hyphens, and is generally used in URLs
    slug = models.SlugField()
    description = models.TextField()
    #9999.99
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # if we delete collection we do not delete all products with protect
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    """Model representing a customer."""
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # gold, silver, bronze
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    """Model representing an order."""
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'


    PAYMENT_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    """Model representing an item in an order."""
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    """Model representing an address."""
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # onetomany relationship with customer, one customer can have many addresses

class Cart(models.Model):
    """Model representing a shopping cart."""
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    """Model representing an item in a shopping cart."""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # CASCADE means that if we delete a product, we also delete all cart items that reference that product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()