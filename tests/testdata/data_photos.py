from api.models import PhotoFields


class DataPhotos:
    valid_photo = {
        PhotoFields.title: 'TestImage',
        PhotoFields.albumId: 1234567,
        PhotoFields.url: 'https://upload.wikimedia.org/wikipedia/commons/b/bd/Web_Page.png'
    }

    valid_photo_info = {
        PhotoFields.width: 1050,
        PhotoFields.height: 624,
        PhotoFields.dominant_color: '#ffffff'
    }

    valid_photo_2 = {
        PhotoFields.title: 'SecondTestImage',
        PhotoFields.albumId: 7654321,
        PhotoFields.url: 'https://via.placeholder.com/600/f66b97'
    }

    # Incomplete and URL has no images
    invalid_photo = {
        PhotoFields.title: 'TestImage',
        PhotoFields.url: 'https://www.longestjokeintheworld.com/'
    }

    test_image_1 = 'tests/testdata/image_800_600_000000.png'
    test_image_1_info = {PhotoFields.width: 800, PhotoFields.height: 600, PhotoFields.dominant_color: '#000000'}

    test_image_2 = 'tests/testdata/image_500_400_22b14c.png'
    test_image_2_info = {PhotoFields.width: 500, PhotoFields.height: 400, PhotoFields.dominant_color: '#22b14c'}
