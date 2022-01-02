from django.contrib import admin

from .models import OrderItem
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk',
                    'user',
                    'ordered',
                    'payed',
                    'payment_date',
                    ]
    
    search_fields = [
        'user__username',
        'order_id'
    ]


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
