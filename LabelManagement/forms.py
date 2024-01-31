from django import forms
from .models import LabelTemplate, LabelSize, ImportCountry, Nutrient, Company
from django.utils.translation import gettext_lazy as _


class LabelTemplateForm(forms.ModelForm):
    EXPIRY_CHOICES = [
        ('date', 'Select Date'),
        ('printed', 'Printed on the package'),
    ]

    expiry_choice = forms.ChoiceField(choices=EXPIRY_CHOICES, widget=forms.RadioSelect)

    company_name = forms.CharField(label=_("Company Name"), max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}), )
    company_address = forms.CharField(label=_("Company Address"), max_length=255, required=False,
                                   widget=forms.Textarea(attrs={'class': 'form-control small', 'rows': '1'}), )
    company_email = forms.CharField(label=_("Company Email"), max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}), )
    company_phone = forms.CharField(label=_("Company Phone"), max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'type':"tel"}), )

    manufacturer_name = forms.CharField(label=_("Manufacturer Name"), max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}), )
    manufacturer_address = forms.CharField(label=_("Company Address"), max_length=255, required=False,
                                   widget=forms.Textarea(attrs={'class': 'form-control small', 'rows': '1'}), )

    class Meta:
        model = LabelTemplate
        fields = ['product_name', 'ingredients', 'other_info', 'import_country', 'sizes', 'net_weight',
                  'expiry_date', 'instruction', 'country_of_origin', 'storage', 'company_name', 'company_address',
                  'company_email', 'company_phone',
                  'manufacturer_name', 'manufacturer_address']
        labels = {
            'product_name': _('Product Name'),
            'ingredients': _('Ingredients'),
            'other_info': _('Other_info'),
            'import_country': _('Import Country'),
            'net_weight': _('Net Weight'),
            'expiry_date': _('Expiry Date'),
            'instruction': _('Instruction'),
            'country_of_origin': _('Country of Origin'),
            'storage': _('Storage'),
            'company_name': _('Company Name'),
            'company_address': _('Company Address'),
            'company_email': _('Company Email'),
            'company_phone': _('Company Phone'),
            'manufacturer_name': _('Manufacturer Name'),
            'manufacturer_address:': _('Manufacturer Address'),
            'sizes': _('Sizes'),
            # ... other labels ...
        }

        queryset = {
            'sizes': LabelSize.objects.all()
        }

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separate items with commas'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'expiry_date': forms.DateInput(format='%Y-%m-%d',
                                           attrs={'class': 'form-control', 'type': 'date', 'id': "expiryDateInput"}),
            'instruction': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'storage': forms.TextInput(attrs={'class': 'form-control textarea-sm'}),
            'import_country': forms.Select(attrs={'class': 'form-control'}),
            'net_weight': forms.TextInput(
                attrs={'class': 'form-control', 'name': 'content_amount', 'id': "content_amount"}),
            'sizes': forms.CheckboxSelectMultiple(attrs={'class': ''}),

        }

    def __init__(self, *args, **kwargs):
        super(LabelTemplateForm, self).__init__(*args, **kwargs)
        self.fields['import_country'].empty_label = None

    def clean(self):
        cleaned_data = super().clean()
        expiry_choice = cleaned_data.get('expiry_choice')
        expiry_date = cleaned_data.get('expiry_date')

        if expiry_choice == 'printed':
            cleaned_data['expiry_date'] = 'Printed on the package'
        elif expiry_choice == 'date' and not expiry_date:
            self.add_error('expiry_date', 'Please select a date.')

        return cleaned_data
