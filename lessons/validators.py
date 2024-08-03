from rest_framework.serializers import ValidationError

acceptable_url = 'youtube.com'


def validate_acceptable_url(value):
    if value not in acceptable_url:
        raise ValidationError('Используемая ссылка недопустима')
