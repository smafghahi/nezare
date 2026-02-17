from django.db import models


class BrokerageClient(models.Model):
    bourse_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client Profile: {self.bourse_code}"


class Order(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    ORDER_TYPES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]
    
    client = models.ForeignKey(BrokerageClient, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_executed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_type} {self.quantity} of {self.symbol}"


class Trade(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    executed_quantity = models.IntegerField()
    executed_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trade: {self.executed_quantity} @ {self.executed_price}"
