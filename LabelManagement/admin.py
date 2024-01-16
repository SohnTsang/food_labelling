from django.contrib import admin
from .models import LabelTemplate, RegulatoryRequirement, LabelSize, Country, Nutrient

# Register your models here.
admin.site.register(LabelTemplate)
admin.site.register(RegulatoryRequirement)
admin.site.register(LabelSize)
admin.site.register(Country)
admin.site.register(Nutrient)

