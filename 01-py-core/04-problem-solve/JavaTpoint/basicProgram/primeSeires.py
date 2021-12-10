class PrimeSeries():
    
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def prime_series(self):
        for num in range(self.low, self.high):
            if num > 1:
                for i in range(2,num):
                    if(num%i)==0:
                        break
                else:
                    print(num)


if __name__ == "__main__":
    numb = PrimeSeries(10,50)
    numb.prime_series()
