import sys
from ascii_transform import AsciiTransform


def main():
    if not len(sys.argv) == 3:
        print "Usage: python comtrade_b2a.py filename_01.cfg filename_01.dat"
        sys.exit("Not enough input parameters. Need name of config file, followed by data file.")

    config_filename = sys.argv[1]
    data_filename = sys.argv[2]

    a = AsciiTransform(config_filename, data_filename)
    a.write_ascii()
    print "Finished transform."

if __name__ == "__main__":
    main()
