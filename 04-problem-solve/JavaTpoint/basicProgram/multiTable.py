class MultiTable():
    def __init__(self):
        self.num = int(input("Enter a number: "))

    def multi_table(self):
        for count in range(1, 11):
            print(self.num, 'X', count,'=',self.num*count)


if __name__ == "__main__":
    numb = MultiTable()
    numb.multi_table()
