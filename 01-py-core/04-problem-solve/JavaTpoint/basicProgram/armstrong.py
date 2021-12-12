class Armstrong():
    def __init__(self):
        self.num = int(input("Enter a number: "))
    
    def __multiply_items(self, item):
        return item**self.__count_number()

    def __count_number(self):
        digit = 0
        number = self.num
        while(number!=0):
            digit+=1 
            number=number//10;
        return digit

    def check_armstrong(self):
        numb = self.num
        su = 0 
        while(numb!=0):
            rem = numb%10
            numb = numb//10
            su += self.__multiply_items(rem)
        if (su==self.num):
            return True
        return False

if __name__ == "__main__":
    arm = Armstrong()
    val = arm.check_armstrong()
    if val:
        print("Armstrong")
    else:
        print("Not Armstrong")
