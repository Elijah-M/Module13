class NumberGuesser:
    """This class adds guessed numbers into a list"""
    def __init__(self, guessed_list):
        self.guessed_list = guessed_list

    def add_guess(self, num):
        """
        This function appends a number onto the guessed_list list
        :param num:
        :return:
        """
        self.guessed_list = []

        self.guessed_list.append(num)


# Driver
x = []
add_num = NumberGuesser(x)
print(add_num.guessed_list)
