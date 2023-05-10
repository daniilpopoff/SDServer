from django.contrib import admin
from servers.models.adventages import Adventage
from servers.models.carusel import Carusel
from servers.models.discounts import Discount, One_discount
from servers.models.numbers import sthWith4

admin.site.register(Adventage)
admin.site.register(Carusel)
admin.site.register(Discount)
admin.site.register(One_discount)
admin.site.register(sthWith4)