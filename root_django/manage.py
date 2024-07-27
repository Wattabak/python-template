#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os

from project.manage import main

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.project.settings")

    main()
