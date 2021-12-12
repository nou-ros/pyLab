class HappyNumber():
    
    def check_happy_number(self, num):
        rem = total = 0
        while(num>0):
            rem = num%10
            total = total + (rem*rem)
            num = num//10
        return total

    def range_happy_number(self):
        for i in range(1,101):
            res = i
            while(res!=1 and res!=4):
                res = self.check_happy_number(res)
            if (res==1):
                print(i, end=" ")

if __name__ == "__main__":
    hp = HappyNumber()
    hp.range_happy_number()
