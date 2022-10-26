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
