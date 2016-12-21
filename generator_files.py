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
    from viewer_generator import generate_file as gf_viewer
    from urler_generator import generate_file as gf_urler
    from serializer_generator import generate_file as gf_serializer
    from django.contrib.gis.db.models.fields import GeometryField
    from django.conf import settings
    django.setup()

    gf_viewer(app_name)
    gf_urler(app_name)
    gf_serializer(app_name)
    print('views.py, urls.py and serialzers.py  have been generated')


if __name__ == "__main__":
    main(sys.argv)