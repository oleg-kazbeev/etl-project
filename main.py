import sys

from terminal_parser import TerminalParser
from data_parser import DataParser


def main():
    terminal_command = sys.argv[1:]

    terminal_parser = TerminalParser()
    terminal_parser.add_argument('-i', '--input', default=[], nargs='+')
    terminal_parser.add_argument('-o', '--output', default=[], nargs='+')

    input_files = terminal_parser.get_list_of_input_files(terminal_command)
    output_files = terminal_parser.get_list_of_output_files(terminal_command)

    for file_name in input_files:
        data_parser = DataParser(file_name)
        file_extension = data_parser.extract_extension_from_filename()
        print(file_extension)


if __name__ == '__main__':
    main()
