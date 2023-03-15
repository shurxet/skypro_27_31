from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

MIN_USER_AGE = 9
PROHIBITED_DOMAINS = ["rambler.ru"]


def check_birth_date(value):
    years = relativedelta(date.today(), value).years
    if years < MIN_USER_AGE:
        raise ValidationError(
            f"Users under the age of {MIN_USER_AGE} are prohibited from registering on this resource"
        )


def check_email(value):
    email_domen = value.split("@")[-1]
    if email_domen in PROHIBITED_DOMAINS:
        raise ValidationError(f"It is forbidden to register with an email domen {email_domen}")
