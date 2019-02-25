import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Hasło musi zawierać przynajmniej jedną cyfrę 0-9."),
                code='password_no_number',
            )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Hasło musi zawierać przynajmniej jedną wielką literę."),
                code='password_no_upper',
            )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Hasło musi zawierać przynajmniej jedną małą literę."),
                code='password_no_lower',
            )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|~!@#$%^&*_=;:\',<>./?]', password):
            raise ValidationError(
                _("Hasło musi zawierać przynajmniej jeden znak specjalny z podanych: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )
