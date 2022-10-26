import shortuuid


class ImageStorage:
    @staticmethod
    def generate_url():
        return f'{shortuuid.uuid()}.png'
