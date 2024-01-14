from django.shortcuts import render, redirect
from .forms import LabelTemplateForm
from .models import LabelTemplate
from CustomTranslation.utils import translate_text  # Import your translation function


def create_label_template(request):
    if request.method == 'POST':
        form = LabelTemplateForm(request.POST)
        if form.is_valid():
            label_template = form.save(commit=False)
            ingredients = form.cleaned_data['ingredients']
            nutrients = form.cleaned_data['nutrients']
            # Convert comma-separated strings to lists
            label_template.ingredients = ingredients.split(',')
            label_template.nutrients = nutrients.split(',')

            # Save the basic data
            label_template.save()

            form.save_m2m()


            label_sizes_names = [f'{size.size_name} ({size.dimensions})' for size in label_template.sizes.all()]

            selected_country = label_template.country
            country_code = selected_country.code
            country_code = country_code.lower()
            # Process and translate data
            translated_ingredients = translate_text(label_template.ingredients, country_code)  # Assuming English translation
            translated_nutrients = translate_text(label_template.nutrients, country_code)

            label_data = {
                'label': {
                    'product_name': label_template.product_name,
                    'translated_ingredients': translated_ingredients,
                    'translated_nutrients': translated_nutrients,
                    'other_info': label_template.other_info,
                    'country': label_template.country.name,
                    'label_sizes': ', '.join(label_sizes_names),
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
