

from django.shortcuts import render, redirect
from .forms import LabelTemplateForm
from .models import LabelTemplate, Nutrient
from CustomTranslation.utils import translate_text  # Import your translation function


def create_label_template(request):
    if request.method == 'POST':
        form = LabelTemplateForm(request.POST)
        if form.is_valid():
            label_template = form.save(commit=False)
            ingredients = form.cleaned_data['ingredients']
            ##nutrients = form.cleaned_data['nutrients']
            # Convert comma-separated strings to lists
            label_template.ingredients = ingredients.split(',')
            # Save the basic data
            label_template.save()
            form.save_m2m()

            country_to_language = {
                'sg': 'en',  # Singapore to English
                'th': 'th',
                'kr': 'kr',
                'cn': 'cn',
                # Add more mappings as needed
            }

            selected_country_code = label_template.country.code
            converted_country_code = country_to_language.get(selected_country_code.lower(), 'en')
            print(selected_country_code.lower())
            names = request.POST.getlist('nutrient_name[]')
            amounts = request.POST.getlist('nutrient_amount[]')
            nutrients_data = []
            translated_ingredients = translate_text(label_template.ingredients,
                                                    converted_country_code)  # Assuming English translation

            translated_nutrient_names = translate_text(names, converted_country_code)
            translated_nutrient_names_list = translated_nutrient_names.split(', ')

            for name, amount in zip(translated_nutrient_names_list, amounts):
                if name:  # Ensure both name and amount are provided
                    nutrient = Nutrient.objects.create(name=name, amount=amount)

                    label_template.nutrients.add(nutrient)
                    nutrients_data.append({'name': name, 'amount': amount})
                else:
                    nutrients_data = ''

            label_sizes_names = [f'{size.size_name} ({size.dimensions})' for size in label_template.sizes.all()]



            # Process and translate data



            label_data = {
                'label': {
                    'product_name': label_template.product_name,
                    'translated_ingredients': translated_ingredients,
                    'other_info': label_template.other_info,
                    'country': label_template.country.name,
                    'label_sizes': ', '.join(label_sizes_names),
                    'content': label_template.content,
                    'expiry_date': label_template.expiry_date,
                    'instruction': label_template.instruction,
                    'company_name': label_template.company_name,
                    'company_address': label_template.company_address,
                    'nutrients': nutrients_data
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
