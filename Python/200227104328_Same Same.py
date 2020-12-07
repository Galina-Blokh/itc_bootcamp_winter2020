def same_same(input_list):
    """
      A new function named 'samesame' that sums the members of a list, but can work with different types as well
    – that is, not only numbers
     :return:  sum, for any incoming instance
    """
    sum_of_list = input_list[0]
    try:
        for i in range(1, len(input_list)):
            sum_of_list += input_list[i]
        return sum_of_list
    except:
        print("you have different type elements. Imposible to sum")

def main():
    """ main() calls the above functions with interesting inputs,
            using test() to check if each result is correct or not. """
    example_list1 = [2, 4, 5]
    example_list2 = ['a', 'b', 'c']
    example_list3 = [[1, 2], [3, 4]]
   

    assert same_same(example_list1) == 11
    assert same_same(example_list2) == 'abc'
    assert same_same(example_list3) == [1, 2, 3, 4]



if __name__ == "__main__":
    main()
