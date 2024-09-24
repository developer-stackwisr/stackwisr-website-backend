from django.core.exceptions import ValidationError

def validate_image(image):
  valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'avif']
  extension = image.name.split('.')[-1].lower()
  if extension not in valid_extensions:
    raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}.')
