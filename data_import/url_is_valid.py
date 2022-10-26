from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def url_is_valid(url: str):
    try:
        URLValidator()(url)
        return True
    except ValidationError:
        return False
