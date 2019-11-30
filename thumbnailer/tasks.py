import os
from zipfile import ZipFile

from PIL import Image
from django.conf import settings

from celery import shared_task


@shared_task
def make_thumbnails(filepath, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, f = os.path.split(filepath)
    file_name, extension = os.path.splitext(f)

    zip_file = f'{file_name}.zip'
    results = {'archive path': f'{settings.MEDIA_URL}images/{zip_file}'}
    try:
        image = Image.open(filepath)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(f)
        os.remove(filepath)

        for w, h in thumbnails:
            image_copy = image.copy()
            image_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{extension}'
            image_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            os.remove(thumbnail_file)

        image.close()
        zipper.close()

    except IOError as e:
        print(e)

    return results
