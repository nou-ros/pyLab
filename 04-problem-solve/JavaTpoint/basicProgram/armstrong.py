class Armstrong():
    def __init__(self):
        self.num = int(input("Enter a number: "))
    
    def __multiply_items(self, item):
        return item**3

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
