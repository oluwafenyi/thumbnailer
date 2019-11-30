import os
from zipfile import ZipFile

from PIL import Image
from django.conf import settings

from celery import shared_task


@shared_task
def remove_archive(zip_file):
    os.remove(os.path.abspath(os.path.join(settings.BASE_DIR, 'media',
                              'images', zip_file)))


@shared_task
def make_thumbnails(filepath, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    _, f = os.path.split(filepath)
    file_name, extension = os.path.splitext(f)

    zip_file = f'{file_name}.zip'
    archive_path = f'{settings.MEDIA_URL}images/{zip_file}'
    results = {'archive path': archive_path}
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

        remove_archive.apply_async((zip_file,), countdown=180)

    except IOError as e:
        print(e)

    return results
