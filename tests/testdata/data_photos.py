class DataPhotos:
    valid_photo = {
        'title': 'TestImage',
        'albumId': 1234567,
        'url': 'https://upload.wikimedia.org/wikipedia/commons/b/bd/Web_Page.png'
    }

    valid_photo_info = {
        'width': 1050,
        'height': 624,
        'color': '#ffffff'
    }

    valid_photo_2 = {
        'title': 'SecondTestImage',
        'albumId': 7654321,
        'url': 'https://via.placeholder.com/600/f66b97'
    }

    # Incomplete and URL has no images
    invalid_photo = {
        'title': 'TestImage',
        'url': 'https://www.longestjokeintheworld.com/'
    }

    test_image_1 = 'tests/testdata/image_800_600_000000.png'
    test_image_1_info = {'width': 800, 'height': 600, 'color': '#000000'}

    test_image_2 = 'tests/testdata/image_500_400_22b14c.png'
    test_image_2_info = {'width': 500, 'height': 400, 'color': '#22b14c'}
