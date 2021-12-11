class CheckPrime:
    def __init__(self, number):
        self.number = number

    def check(self):
        for i in range(2, self.number):
            if self.number%i!=0:
                return 1
        return 0


if __name__ == "__main__":
    num = CheckPrime(int(input("Enter a number: ")))
    res = num.check()
    if res:
        print("composite")
    else:
        print("prime")
