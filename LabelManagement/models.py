from django.contrib.auth.models import User
from django.db import models


class ImportCountry(models.Model):
    country_id = models.AutoField(primary_key=True)  # Primary key
    name = models.CharField(max_length=100)  # e.g., 'Japan'
    code = models.CharField(max_length=2)  # e.g., 'JP' for Japan

    def __str__(self):
        return self.name

# Model for Label Templates
class LabelSize(models.Model):
    size_name = models.CharField(max_length=50, unique=True)  # e.g., "Custom", "Standard"
    dimensions = models.CharField(max_length=100)  # e.g., "10x15 cm"

    def __str__(self):
        return f"{self.size_name} ({self.dimensions})"


class Nutrient(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'Calories'
    amount = models.CharField(max_length=50)  # e.g., 10.95g

    def __str__(self):
        return f"{self.name}: {self.amount}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class LabelTemplate(models.Model):
    template_id = models.AutoField(primary_key=True) # A unique identifier for each template
    product_name = models.CharField(max_length=255) # The name of the product
    ingredients = models.TextField() # A text field for ingredients
    other_info = models.TextField(blank=True, null=True) # Additional information if needed
    creation_date = models.DateTimeField(auto_now_add=True) # Date of creation or last update
    import_country = models.ForeignKey(ImportCountry, on_delete=models.CASCADE) #Country of Origin
    sizes = models.ManyToManyField(LabelSize)
    net_weight = models.CharField(max_length=50, blank=True, null=True)  # String field for net_weight
    expiry_date = models.CharField(max_length=100, blank=True, null=True)  # String field for expiry date
    instruction = models.CharField(max_length=255, blank=True, null=True)  # String field for instruction
    companies = models.ManyToManyField(Company, blank=True)
    nutrients = models.ManyToManyField(Nutrient, blank=True, null=True)
    #need to add the below to the model
    #country of origin
    #barcode
    #manufacturer = name & address
    #Storage



    def __str__(self):
        return self.product_name

# Model for Regulatory Requirements
class RegulatoryRequirement(models.Model):
    import_country = models.ForeignKey(ImportCountry, on_delete=models.CASCADE, null=True)
    mandatory_info = models.TextField() # Mandatory information required on the label
    label_sizes = models.ManyToManyField(LabelSize)
    font_requirements = models.CharField(max_length=255) # Details about required fonts
    language = models.CharField(max_length=100) # Primary language for the label
    additional_requirements = models.TextField(blank=True, null=True) # Other specific requirements
    last_updated = models.DateTimeField(auto_now=True) # Last update of regulatory information

    def __str__(self):
        return self.import_country.name



