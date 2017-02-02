import os
import sys, inspect





def main(argv):

    if (len(argv)) != 3:
        print('Usage: python generator_files.py django_project_name django_app_name')
        exit()
    else:
        print('-------------------------------------------------------------------------------------------------------')
        print('Gerando arquivos urls.py,views.py serializaers.py na pasta raiz do projeto:')
        print('-------------------------------------------------------------------------------------------------------')

    prj_name = argv[1]
    app_name = argv[2]

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", prj_name  + ".settings")

    import django
    from urler_project_generator import generate_file as gf_prj_urler
    from viewer_generator import generate_file as gf_viewer
    from urler_generator import generate_file as gf_urler
    from serializer_generator import generate_file as gf_serializer
    from django.contrib.gis.db.models.fields import GeometryField
    from django.conf import settings
    django.setup()
    file_url_prj = prj_name + '/urls.py'
    gf_prj_urler(app_name, default_name=file_url_prj)
    file_view = app_name + '/views.py'
    gf_viewer(app_name, default_name=file_view)
    file_url_app = app_name + '/urls.py'
    gf_urler(app_name, default_name=file_url_app)
    file_serializer_app = app_name + '/serializers.py'
    gf_serializer(app_name, default_name=file_serializer_app)
    print('views.py, urls.py and serialzers.py  have been generated')


if __name__ == "__main__":
    main(sys.argv)