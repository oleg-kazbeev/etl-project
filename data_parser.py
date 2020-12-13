import os


class DataParser:
    def __init__(self, filename):
        self.file_extension = ''
        self.filename = filename

    def extract_extension_from_filename(self):
        _, self.file_extension = os.path.splitext(self.filename)
        return self.file_extension
