import os
import sys

ARG_FILE_NAME = 1
# constant for converting meter --> feet
M_F = 3.28084


def convertor(input_filename):
    """
    receives a path of a csv file assumed to have one filled column, every cell
    includes length in meters. Create csv file in the same folder, named input_filename_new with 2 columns:
    length in metres + length in feet
    :param input_filename: .csv file
    :return: .csv file
    """
    try:
        text = open(input_filename, "r")
    except FileNotFoundError:
        print("File not found", input_filename, ":(")
        sys.exit(0)
    dir_name = os.path.dirname(input_filename)
    file_name = os.path.splitext(os.path.basename(input_filename))[0]
    output_file_name = os.path.join(dir_name, (file_name + '_new.csv'))
    output_list = []
    for n, line in enumerate(text):
        try:
            element_metres = float(line.strip())
        except ValueError:
            if ',' in line:
                print("More then one column in file", n, ':', line.strip())
                sys.exit(0)
            if line.strip() == '':
                print('The line', n, 'is empty')
                sys.exit(0)
            print("Impossible to cast", line.strip(), "in float. At line = ", n)
            sys.exit(0)
        element_feet = element_metres * M_F
        output_list.append(line.strip() + ',' + str(element_feet) + '\n')
    if not output_list:
        print('Your file is empty')
        sys.exit(0)
    try:
        output_file = open(output_file_name, "w")
    except IOError as ioe:
        print("Problem to write into file", output_file_name)
        print('Got an Exception', ioe)
        sys.exit(0)
    for element in output_list:
        output_file.write(element)
    output_file.close()


def main():
    if len(sys.argv) < ARG_FILE_NAME + 1:
        print('you forgot to input the filename')
        sys.exit(0)
    input_filename = sys.argv[ARG_FILE_NAME]

    if not input_filename:
        print("please enter the name of file")
        sys.exit(1)

    return convertor(input_filename)


if __name__ == '__main__':
    main()
