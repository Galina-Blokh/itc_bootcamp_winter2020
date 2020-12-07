from datetime import timedelta, datetime


def day_calculator(num_of_days):
    """
     print date in iso format, like so:
     day_calculator(5)
    2019-10-15T18:43:03.213555
    :param num_of_days: int
    :return: the date and time in number of days from now,
    """
    today = datetime.now()
    delta_day = (today - timedelta(days=num_of_days))
    print(delta_day.isoformat())







def main():
    """
    Main function of the module, tests  functions of the module
    """
    day_calculator(5)



if __name__ == '__main__':
    main()
