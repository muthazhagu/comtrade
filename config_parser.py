import os.path
import sys


class ConfigParser:
    CONFIG_DIR = "config"
    NUMBER_OF_DEFAULT_LINES = 8

    def __init__(self, config_filename):
        """
        :param config_filename: Name of the config file as a string. File must exist in the config directory.
        """
        self.filename = config_filename
        assert os.path.isfile(os.path.join(ConfigParser.CONFIG_DIR, self.filename))
        self._verify_file_format()

    def _verify_file_format(self):
        """
        Verify that the config file is in the right format.
        :return:
        """
        config = self.get_config()
        assert config[-1].strip() in ["ASCII", "BINARY"], "Please check if the config file is in the right format."

        channel_count = self.get_channel_count()
        assert len(config) == channel_count + ConfigParser.NUMBER_OF_DEFAULT_LINES

    def get_config(self):
        """
        Return the contents of the config file as a list.
        :return: A list of strings like ["abc\n", "efg\n"]
        """
        try:
            with open(os.path.join(ConfigParser.CONFIG_DIR, self.filename), "rU") as f:
                config = f.readlines()
        except IOError:
            sys.exit("Could not open config file. Please check that it is in the right location.")

        return config

    def get_channel_count(self):
        """
        Return the total number of channels as an int, and assert that the channel count is correct.
        :return: Total number of channels as an int.
        """
        config = self.get_config()
        total_channels, analog, digital = config[1].strip().split(",")
        total_channels, analog, digital = int(total_channels.strip()), int(analog.strip()[0:-1]), \
                                          int(digital.strip()[0:-1])

        assert total_channels == analog + digital, "Channel count did not match. Please check configuration file."

        return total_channels

    def get_row_count(self):
        """
        :return: Number of rows as an int.
        """
        return int(self.get_config()[-4].split(",")[1].strip())

