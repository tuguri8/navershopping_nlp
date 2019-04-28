#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from konlpy.tag import Twitter

def get_noun(text):
    nouns = Twitter().nouns(text)
    return [n for n in nouns]

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_nlp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()