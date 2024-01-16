from .models import CustomTranslation
#from google.cloud import translate
#rom pydeepl import translate
#from deep_translator import GoogleTranslator
import re

def replace_special_characters(input_texts):
    # Define a regular expression pattern to match special characters
    special_char_pattern = r'[\r\n\t]+'
    cleaned_text = ', '.join(input_texts)

    cleaned_text = re.sub(special_char_pattern, ', ', cleaned_text)


    return cleaned_text


def translate_text(input_texts, target_language):

    translated_texts = []
    input_texts = replace_special_characters(input_texts).split(", ")
    if input_texts != ['']:
        for input_text in input_texts:
            # Try to get the translation from your custom model
            try:
                translation_entry = CustomTranslation.objects.get(japanese_text=input_text.strip())
                if input_text == '':
                    translated_text = ''
                else:
                    translated_text = getattr(translation_entry, f'{target_language}_translation')

                if translated_text:
                    translated_texts.append(translated_text)
                    continue

            except CustomTranslation.DoesNotExist:
                translated_texts.append(input_text)

                pass

            # If not found, use the external API (Uncomment and use the relevant API)
            # translated_text = translate_with_external_api(input_text, target_language)
            # translated_texts.append(translated_text)

            # Join the translated texts with a comma

        return ', '.join(translated_texts)
    else:
        return ''

    # If not found, use the external API
    # return translate_with_external_api(input_text, target_language)

"""
def translate_with_external_api(input_text, target_language):
    # Implement external API translation here
    #client = translate.Client() - google
    #translation = client.translate(input_text, target_language=target_language) - google


    # Extract the translated text
    #translated_text = translation["translatedText"] - google
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(input_text)

    return translated_text

"""