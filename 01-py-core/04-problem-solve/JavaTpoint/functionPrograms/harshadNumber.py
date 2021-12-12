class HarshadNumber():

    def __init__(self):
        self.number = int(input("enter a number: "))

    def __sum_of_digits(self):
        num = self.number
        rem = total = 0
        while(num!=0):
            rem = num%10
            num = num//10
            total += rem
        return total

    def check_harshad(self):
        num = self.number
        if(num%self.__sum_of_digits()==0):
            print("Harshad number")
        else:
            print("Not harshad number")

if __name__ == "__main__":
     hnum = HarshadNumber()
     hnum.check_harshad()
