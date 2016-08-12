from config_parser import ConfigParser
from data_parser import DataParser
import os.path
import struct


class AsciiTransform:
    CHANNEL_BYTES = 2
    ORDINAL_BYTES = 4
    TIMESTAMP_BYTES = 4

    def __init__(self, config_filename, data_filename):
        """
        :param config_filename: A string, and file must exist in the config directory.
        :param data_filename: A string, and file must exist in the data directory.
        """
        self.config_object = ConfigParser(config_filename)
        self.data_object = DataParser(data_filename)

        self.bytestring_length = (self.config_object.get_channel_count() * AsciiTransform.CHANNEL_BYTES) + \
                                 AsciiTransform.ORDINAL_BYTES + \
                                 AsciiTransform.TIMESTAMP_BYTES

        assert self.data_object.get_number_of_bytes() == self.bytestring_length * self.config_object.get_row_count(), \
            "Number of bytes does not channel count, and number of rows of data based on the config file."

    def write_ascii(self):
        """
        Writes a file in the output directory with .ascii appended to the data file name.
        """
        output_filename = ".".join([self.data_object.filename, 'ascii'])

        with open(os.path.join(DataParser.DATA_DIR, self.data_object.filename), "rb") as input_file, \
                open(os.path.join(DataParser.OUTPUT_DIR, output_filename), "w") as output_file:
            data = input_file.read(self.bytestring_length)
            input_file.seek(0)

            unpack_format = "".join(['I', 'I', 'h'*self.config_object.get_channel_count()])

            while data != "":
                data = input_file.read(self.bytestring_length)
                if len(data) == self.bytestring_length:
                    value = ",".join(map(str, struct.unpack(unpack_format, data)))
                    output_file.write(value + "\n")
