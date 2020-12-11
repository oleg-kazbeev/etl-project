import sys

from terminal_parser import TerminalParser


def main():
    terminal_command = sys.argv[1:]

    parser = TerminalParser()
    parser.add_argument('-i', '--input', default=[], nargs='+')
    parser.add_argument('-o', '--output', default=[], nargs='+')

    input_files = parser.get_list_of_input_files(terminal_command)
    output_files = parser.get_list_of_output_files(terminal_command)


if __name__ == '__main__':
    main()
