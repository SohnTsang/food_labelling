from django.conf import settings
import os
import barcode, random
from barcode.writer import ImageWriter

def create_barcode_image(barcode_number, save_dir='barcodes'):
    barcode_class = barcode.get_barcode_class('code128')
    barcode_instance = barcode_class(barcode_number, writer=ImageWriter())

    # Ensure the directory exists
    barcode_dir = os.path.join(settings.MEDIA_ROOT, save_dir)
    if not os.path.exists(barcode_dir):
        os.makedirs(barcode_dir)

    # Save the barcode image
    filepath = barcode_instance.save(os.path.join(barcode_dir, barcode_number))

    # Return the relative path to be stored in the database
    return os.path.join(save_dir, os.path.basename(filepath))


def generate_barcode():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])  # Example: 12 digit barcode