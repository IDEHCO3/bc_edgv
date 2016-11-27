import os
import sys, inspect
import django
import re

def convert_camel_case_to_hifen(camel_case_string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', camel_case_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

def generate_snippets_to_view(model_class_name):
    serializer_class_snippet = (' ' * 4) + 'serializer_class = ' + model_class_name + 'Serializer\n'
    context_name = convert_camel_case_to_hifen(model_class_name)
    context = convert_camel_case_to_hifen((' ' * 4) + 'contextclassname = ' + "'" + context_name + "-list'\n")
    arr = []
    arr.append('class ' + model_class_name + 'List(HandleFunctionsList):\n')
    arr.append((' ' * 4) + 'queryset = ' + model_class_name + '.objects.all()' + '\n')
    arr.append(serializer_class_snippet)
    arr.append(context)
    arr.append('\n')
    arr.append('class ' + model_class_name + 'Detail(HandleFunctionDetail):\n')
    arr.append(serializer_class_snippet)
    arr.append(context)
    return arr

def imports_str_as_array(a_name):
    arr = []
    arr.append("from " + a_name + ".utils import *\n")
    arr.append("from " + a_name + ".models import *\n")
    arr.append("from " + a_name + ".serializers import *\n\n")
    return arr

def generate_file(package_name, default_name='views.py'):
    classes_from = inspect.getmembers(sys.modules[package_name + '.models'], inspect.isclass)
    with open(default_name, 'w+') as sr:
        for import_str in imports_str_as_array(package_name):
            sr.write(import_str)
        for model_class_arr in classes_from:
            for str in generate_snippets_to_view(model_class_arr[0]):
                sr.write(str)
            sr.write('\n')
        sr.close()

if __name__ == "__main__":
    if (len( sys.argv))!= 3:
        print('Usage: python viewer_generator.py django_project_name django_app_name')
        exit()

    prj_name = sys.argv[1]
    app_name = sys.argv[2]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", prj_name + ".settings")
    django.setup()
    generate_file(app_name)
    print('views.py  has been generated')