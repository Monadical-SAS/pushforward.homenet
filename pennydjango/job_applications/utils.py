import os
import random

from django.core.exceptions import ValidationError


def validate_file_extension(file):
    try:
        file_extension = os.path.splitext(file.name)[1]
        if file_extension != '.pdf':
            raise ValidationError(
                 ('Invalid file extension'),
            )
    except TypeError:
        pass


def resume_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return '/'.join([f"{randomstr}{file_extension}"])