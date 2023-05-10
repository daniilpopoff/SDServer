from django.views.generic import TemplateView
from servers.models.adventages import Adventage
from servers.models.carusel import Carusel
from servers.models.discounts import Discount, One_discount
from servers.models.numbers import sthWith4

class IndexTemplateView(TemplateView):
    # I want to insert the ORDER model in this class also
    model = Adventage
    context_object_name = "product"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adventage'] = Adventage.objects.all()  # or whatever
        context['carusel'] = Carusel.objects.all()  # or whatever
        context['discount'] = Discount.objects.all().first()
        context['one_discount'] = Discount.objects.all().first().one_discount_set.all()
        context['sthWith4'] = sthWith4.objects.all()
        return context