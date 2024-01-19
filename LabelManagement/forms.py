from django import forms
from .models import LabelTemplate, LabelSize, ImportCountry, Nutrient, Company
from django.utils.translation import gettext_lazy as _


class LabelTemplateForm(forms.ModelForm):

    company_name = forms.CharField(label=_("Company Name"), max_length=255, required=False)
    company_address = forms.CharField(label=_("Company Address"), max_length=255, required=False)
    company_email = forms.EmailField(label=_("Company Email"), required=False)
    company_phone = forms.CharField(label=_("Company Phone"), max_length=30, required=False)

    class Meta:
        model = LabelTemplate
        fields = ['product_name', 'ingredients', 'other_info', 'import_country', 'sizes', 'net_weight',
                  'expiry_date', 'instruction', 'company_name', 'company_address', 'company_email', 'company_phone']
        labels = {
            'product_name': _('Product Name'),
            'ingredients': _('Ingredients'),
            'other_info': _('Other_info'),
            'import_country': _('Import Country'),
            'net_weight': _('Net Weight'),
            'expiry_date': _('Expiry Date'),
            'instruction': _('Instruction'),
            'company_name': _('Company Name'),
            'company_address': _('Company Address'),
            'company_email': _('Company Email'),
            'company_phone': _('Company Phone'),
            # ... other labels ...
        }

        queryset = {
            'sizes': LabelSize.objects.all()
        }


        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separate items with commas'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'net_weight': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'instruction': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'import_country': forms.Select(attrs={'class': 'form-control'}),
            'sizes': forms.CheckboxSelectMultiple(attrs={'class': 'sizes'}),
        }

    def __init__(self, *args, **kwargs):
        super(LabelTemplateForm, self).__init__(*args, **kwargs)
        self.fields['import_country'].empty_label = None