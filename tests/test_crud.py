from pathlib import Path
from api.urls import URL
from api.models import Photo, PhotoFields
from testdata.data_photos import DataPhotos


class TestCRUD:
    def test_list(self, api_client):
        response = api_client.get(f'{URL.API_DIR}{URL.LIST}')
        assert response.status_code == 200, 'Failed to read'

    def test_create(self, api_client, photo_cleanup):
        create_fail = api_client.post(f'{URL.API_DIR}{URL.CREATE}', data=DataPhotos.invalid_photo)
        assert create_fail.status_code == 400, 'Bad request is handled incorrectly'

        create = api_client.post(f'{URL.API_DIR}{URL.CREATE}', data=DataPhotos.valid_photo)
        assert create.status_code == 200, 'Failed to create'

    def test_update(self, api_client, photo_applied, photo_cleanup):
        url = f'{URL.API_DIR}{URL.UPDATE}{photo_applied.id}/'

        update_fail = api_client.post(url, data=DataPhotos.invalid_photo)
        assert update_fail.status_code == 400, 'Bad request is handled incorrectly'

        update = api_client.post(url, data=DataPhotos.valid_photo_2)
        new_photo = Photo.get_by_id(1)
        assert update.status_code == 200, 'Failed to update'
        assert all([
            new_photo.title == DataPhotos.valid_photo_2[PhotoFields.title],
            new_photo.albumId == DataPhotos.valid_photo_2[PhotoFields.albumId],
        ]), 'Photo\'s info has not changed on update'

    def test_delete(self, api_client, photo_applied):
        url = f'{URL.API_DIR}{URL.DELETE}{photo_applied.id}/'

        delete = api_client.delete(url)
        assert delete.status_code == 200, 'Failed to delete'
        assert Photo.get_by_id(photo_applied.id) is None, 'Photo is not deleted from Database'

        assert not Path(photo_applied.url).exists(), 'Photo is not deleted from storage system'

        delete_fail = api_client.delete(url)
        assert delete_fail.status_code == 404, 'ObjectDoesNotExist is handled incorrectly'
