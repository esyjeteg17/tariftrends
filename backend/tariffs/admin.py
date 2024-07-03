from .models import Tariff, ModemTariff, HomephoneTariff, TVTariff, InternetTariff, SmartTariff
from django.contrib import admin

admin.site.register(Tariff)
admin.site.register(ModemTariff)
admin.site.register(HomephoneTariff)
admin.site.register(TVTariff)
admin.site.register(InternetTariff)
admin.site.register(SmartTariff)


