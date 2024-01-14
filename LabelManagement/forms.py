from django import forms
from .models import LabelTemplate, LabelSize, Country
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
        fields = ['product_name', 'ingredients', 'nutrients', 'other_info', 'country', 'sizes']
        labels = {
            'product_name': _('Product Name'),
            'ingredients': _('Ingredients'),
            'nutrients': _('Nutrients'),
            'other_info': _('Other_info'),
            'country': _('Country of Origin'),
            'sizes': _('Sizes'),
            # ... other labels ...
        }

        queryset = {
            'sizes': LabelSize.objects.all()
        }

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separate items with commas'}),
            'nutrients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separate items with commas'}),
            'other_info': forms.Textarea(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'sizes': forms.CheckboxSelectMultiple(attrs={'class': 'sizes'})
        }

        required = {
            'sizes': True
        }