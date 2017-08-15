import os
import sys, inspect
import django

from django.contrib.gis.db.models.fields import GeometryField

def is_spatial(model_class):

    for field in model_class._meta.get_fields():
        if isinstance(field, GeometryField):
            return True

    return False
def generate_snippets_to_serializer(model_class_name, model_class):
    arr = []
    if is_spatial(model_class):
        class_name = 'Serializer(GeoFeatureModelSerializer)'
    else:
        class_name = 'Serializer(ModelSerializer)'
    arr.append('class ' +model_class_name + class_name+':\n')
    arr.append((' ' * 4) + 'class Meta:\n')
    arr.append((' ' * 8) + 'model = ' +model_class_name + '\n')
    identifier = None
    geom = None
    fields = model_class._meta.get_fields()
    arr.append((' ' * 8) + 'fields = [')
    for i, field in enumerate(fields):
        arr.append("'" + field.name + "'")
        if i < len(fields) - 1:
            arr.append(',')
        else:
            arr.append(']\n')
        if field.primary_key:
            identifier = field.name
        if isinstance(field, GeometryField):
            geom = field.name
    if geom is not None:
        arr.append((' ' * 8) + "geo_field = '" + geom + "'\n")
    arr.append((' ' * 8) + "identifier = '" + identifier + "'\n")
    arr.append((' ' * 8) + "identifiers = '[" + identifier + "]'\n\n\n")
    return arr

def generate_file(package_name, default_name= '\serializers.py'):
    classes_from = inspect.getmembers(sys.modules[package_name + '.models'], inspect.isclass)
    with open(default_name, 'w+') as sr:
        sr.write("from "+package_name+".models import *\n")
        if is_spatial(classes_from[0][1]):
            sr.write("from rest_framework_gis.serializers import GeoFeatureModelSerializer\n\n")
        else:
            sr.write("from rest_framework.serializers import ModelSerializer\n\n")
        for model_class_arr in classes_from:
            for snippet in generate_snippets_to_serializer(model_class_arr[0], model_class_arr[1]):
                sr.write(snippet)
        sr.write('\n\n')
        sr.write('serializers_dict = {}')
        sr.close()

if __name__ == "__main__":
    if (len(sys.argv)) != 3:
        print('Usage: python serializer_generator.py django_project_name django_app_name')
        exit()
    prj_name = sys.argv[1]
    app_name = sys.argv[2]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", prj_name + ".settings")
    django.setup()
    generate_file(app_name)
    print('serializers.py  has been generated')