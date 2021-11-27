from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# TODO update aadhar number validation
def validate_aadhar_number(value):
    if value:
        aadhar_regex = RegexValidator(
            regex=r'^[0-9]{9}$',
            message=""
        )
        aadhar_regex(value)


def validate_dob(value):
    if value and value > date.today():
        raise ValidationError(f'{value} must be less then today')


def validate_phone_number(value):
    if value:
        phone_regex = RegexValidator(
            regex=r'^[1-9][0-9]{9}$',
            message="Phone number must be entered in the format: '999999999'."
        )
        phone_regex(value)


def validate_email_id(value):
    if value:
        email_regex = RegexValidator(
            regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            message="Email is not in correct format"
        )
        email_regex

def validate_copyright(value):
    if value:
        copyright_regex = RegexValidator(
            regex=r'^[2][0][1-9]{2}$',
            message="Copyright year must be later than 2019."
        )
        copyright_regex(value)

def validate_pincode(value):
    if value:
        copyright_regex = RegexValidator(
            regex=r'^[1-9][0-9]{5}$',
            message="Pincode must not start with 0 and must be of 6 characters."
        )
        copyright_regex(value)
