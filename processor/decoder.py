import base64

class Base64:
    def __init__(self, data):
        try:

            d, data = data.split((':'))
            self.file, data = data.split('/', 1)
            self.file_type, data = data.split(';', 1)
            self.file_encoding, data = data.split(',', 1)
        except:
            print('Could not obtain file type and encoding format from the data')
        self.raw_data = data
        self.decoded_data = ''
        self.image_url = ''

    def decode(self):
        self.decoded_data = ''
        try:
            self.decoded_data = base64.b64decode(self.raw_data)
        except:
            print('Failed to decode the data, please ensure your str uses base64 encoding scheme')
    def saveImage(self):
        self.image_url = f"output_image.{self.file_type}"
        with open(f"{self.image_url}", 'wb') as f:
            f.write(self.decoded_data)



