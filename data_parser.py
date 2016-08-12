import os.path
import struct


class DataParser:
    DATA_DIR = "data"
    OUTPUT_DIR = "output"

    def __init__(self, data_filename):
        """
        :param data_filename: Name of the data file as a string. File must exist in the data directory.
        """
        self.filename = data_filename
        assert os.path.isfile(os.path.join(DataParser.DATA_DIR, self.filename))

    def get_number_of_bytes(self):
        """
        :return: Number of bytes in the data file as an int.
        """
        with open(os.path.join(DataParser.DATA_DIR, self.filename), "rb") as f:
            return len(f.read())

