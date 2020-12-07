def copaste(source_path, copy_path):
    """
    The function receives a path to a file (as an absolute path) and copies it to a given folder.
    :param source_path:
    :param absolute source_path and copy_path without name of a copy_file
    :return: True/False
    """
    try:
        source = open(source_path, 'rb+')
        copy_path_file = source_path.split('/')[-1]
        copy = open(copy_path + '/' + copy_path_file , 'wb+')
        copy.write(source.read())
        source.close()
        copy.close()
        return True
    except:
        return False


def test_copaste():
    """
    testing the copaste function with *.txt and *.pdf
    """

    assert copaste(r'/home/gal/Documents/calculus.txt', r'/home/gal/Downloads')
    assert copaste(r'/home/gal/Documents/calculus.pdf', r'/home/gal/Downloads')
    print('testing the is_number function with *.txt and *.pdf is passed!')


def main():
    """
    Main function runs  functions of the module
    """

    test_copaste()


if __name__ == '__main__':
    main()
