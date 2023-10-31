from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.deconstruct import deconstructible


from django.core.validators import RegexValidator


def validate_english(value):
    # regex = r'^[A-Za-z]+$'
    # validator = RegexValidator(regex=regex, message='Field must contain only English characters')
    # validator(value)
    pass


def validate_bulgarian(value):
    # regex = r'^[А-Яа-я]+$'
    # validator = RegexValidator(regex=regex, message='Field must contain only Bulgarian characters')
    # validator(value)
    pass


# URL check


def validate_url(value):
    validator = URLValidator()
    try:
        validator(value)
    except ValidationError:
        raise ValidationError("This is not a valid URL.")


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError("Value must contain only letters")
    # valid case
    #
    # if not all(ch.isalpha() for ch in value):
    #     raise ValidationError('Value must contain only letters')


class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(self.max_size))


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f"Date must be greater than {self.min_date}")


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if self.max_date < value:
            raise ValidationError(f"Date must be earlier than {self.max_date}")


# Add a Validator to ensure that the name_eng field is not empty.
# Add a Validator to ensure that the profile_pic field is a valid URL.
# Add a validator to check if field is in english for story and name
# Add a validator to check if field is in bulgarian for story and name
