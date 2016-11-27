import os
import sys, inspect
import django
from viewer_generator import generate_file as gf_viewer
from urler_generator import generate_file as gf_urler
from serializer_generator import generate_file as gf_serializer
from django.contrib.gis.db.models.fields import GeometryField

from django.conf import settings



def generator_all_files(app_name):
    gf_viewer(app_name)
    gf_urler(app_name)
    gf_serializer(app_name)

if __name__ == "__main__":
    if (len( sys.argv))!= 3:
        print('Usage: python generator_files.py django_project_name django_app_name')
        exit()

    prj_name = sys.argv[1]
    app_name = sys.argv[2]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", prj_name + ".settings")
    settings.configure()
    django.setup()
    generator_all_files(app_name)
    print('views.py, urls.py and serialzers.py  have been generated')