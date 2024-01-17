from django import forms
from .models import LabelTemplate, LabelSize, Country, Nutrient
from django.utils.translation import gettext_lazy as _


class LabelTemplateForm(forms.ModelForm):
    """
    sizes = forms.ModelMultipleChoiceField(
        queryset=LabelSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    """

    class Meta:
        model = LabelTemplate
        fields = ['product_name', 'ingredients', 'other_info', 'country', 'sizes', 'content',
                  'expiry_date', 'instruction', 'company_name', 'company_address']
        labels = {
            'product_name': _('Product Name'),
            'ingredients': _('Ingredients'),
            'other_info': _('Other_info'),
            'country': _('Export Country'),
            'content': _('Content'),
            'expiry_date': _('Expiry Date'),
            'instruction': _('Instruction'),
            'company_name': _('Company Name'),
            'company_address': _('Company Address'),
            # ... other labels ...
        }

        queryset = {
            'sizes': LabelSize.objects.all()
        }


        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separate items with commas'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'instruction': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'company_name': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'company_address': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'sizes': forms.CheckboxSelectMultiple(attrs={'class': 'sizes'}),
        }


'''
class NutrientForm(forms.ModelForm):
    class Meta:
        model = Nutrient
        fields = ['name', 'amount']
'''