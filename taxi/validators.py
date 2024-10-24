import re
from django.core.exceptions import ValidationError


def validate_license_number(value):
  pattern = r'^[A-Z]{3}\d{5}$'
  if not re.match(pattern, value):
    raise ValidationError(
      "Le numéro de license doit comporter 3 lettres majuscules suivies de 5 chiffres."
    )
