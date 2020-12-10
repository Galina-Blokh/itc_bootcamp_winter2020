def input_validator(user_input, status=False):
    """
     checking if the input is valid to calculate prod
    :return:  true/false
    """
    while not status:
        for elem in user_input.split():
            if not is_number(elem):
                status = False
                return status
            else:
                status = True
    return status


def is_number(elem):
    """
    check if the element is a number
    :param elem:
    :return: True/false
    """
    try:
        float(elem)
        return True
    except:
        return False


def test_input_validator():
    """
    testing the input_validator function
    """
    assert not input_validator('1 a b')
    assert not input_validator('[1] a b')
    assert not input_validator('1 2 a 5')
    assert input_validator('1 2 3')
    assert input_validator('1 0 3')
    assert input_validator('1 2 -1')
    print('test_input_validator passed!!')


def test_is_number():
    """
    testing the is_number function
    """
    assert not is_number('.')
    assert not is_number('')
    assert not is_number('[1]')
    assert not is_number('a')
    assert is_number('1')
    assert is_number('1.0')
    assert is_number('-1')
    print('test_input_is_number passed!!')


def main():
    """
    Main function of the module, tests  functions of the module
    """
    test_is_number()
    test_input_validator()


if __name__ == '__main__':
    main()
