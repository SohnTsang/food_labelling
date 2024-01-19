

from django.shortcuts import render, redirect
from .forms import LabelTemplateForm
from .models import LabelTemplate, Nutrient, Company
from CustomTranslation.utils import translate_text  # Import your translation function


def create_label_template(request):
    if request.method == 'POST':
        form = LabelTemplateForm(request.POST)
        if form.is_valid():
            label_template = form.save(commit=False)
            ingredients = form.cleaned_data['ingredients']

            # Convert comma-separated strings to lists
            label_template.ingredients = ingredients.split(',')
            amount = request.POST.get('content_amount', '')
            unit = request.POST.get('content_unit', '')
            label_template.net_weight = f'{amount} {unit}'
            # Save the basic data
            label_template.save()
            form.save_m2m()

            company_name = form.cleaned_data.get('company_name')
            company_address = form.cleaned_data.get('company_address')
            company_email = form.cleaned_data.get('company_email')
            company_phone = form.cleaned_data.get('company_phone')

            if company_name:  # Check if company name is provided
                company, created = Company.objects.get_or_create(
                    name=company_name,
                    defaults={'address': company_address, 'email': company_email, 'phone': company_phone}
                )
                label_template.companies.add(company)

            country_to_language = {
                'sg': 'en',  # Singapore to English
                'th': 'th',
                'kr': 'kr',
                'cn': 'cn',
                # Add more mappings as needed
            }

            selected_country_code = label_template.import_country.code
            converted_country_code = country_to_language.get(selected_country_code.lower(), 'en')

            nutrient_names = request.POST.getlist('nutrient_name[]')
            nutrient_amounts = request.POST.getlist('nutrient_amount[]')
            nutrient_unit = request.POST.getlist('nutrient_unit[]')

            nutrients_data = []
            translated_ingredients = translate_text(label_template.ingredients,
                                                    converted_country_code)  # Assuming English translation

            translated_nutrient_names = translate_text(nutrient_names, converted_country_code)
            translated_nutrient_names_list = translated_nutrient_names.split(', ')

            for name, amount, unit in zip(translated_nutrient_names_list, nutrient_amounts, nutrient_unit):
                if name:  # Ensure both name and amount are provided
                    nutrient = Nutrient.objects.create(name=name, amount=amount)
                    label_template.nutrients.add(nutrient)
                    nutrients_data.append({'name': name, 'amount': amount, 'unit': unit})
                else:
                    nutrients_data = ''

            label_sizes_names = [f'{size.size_name} ({size.dimensions})' for size in label_template.sizes.all()]



            # Process and translate data



            label_data = {
                'label': {
                    'product_name': label_template.product_name,
                    'translated_ingredients': translated_ingredients,
                    'other_info': label_template.other_info,
                    'import_country': label_template.import_country.name,
                    'label_sizes': ', '.join(label_sizes_names),
                    'net_weight': label_template.net_weight,
                    'expiry_date': label_template.expiry_date,
                    'instruction': label_template.instruction,
                    'nutrients': nutrients_data,
                    'company_name': company_name,
                    'company_address': company_address,
                    'company_email': company_email,
                    'company_phone': company_phone,
                }
            }

            request.session['label_data'] = label_data

            # Pass translated data to the result page
            return redirect('result_page')
    else:
        form = LabelTemplateForm()

    return render(request, 'label_template_form.html', {'form': form})


def result_page(request):
    label_data = request.session.get('label_data', {})
    return render(request, 'result_page.html', label_data)
