class FiboSeries():
    def __init__(self, num):
        self.num = num

    def _fibo_series(self):
        start = 0
        end = 1
        temp = 0
        print(start, end, end=" ")
        while(self.num>end):
            temp = start
            start = end
            end = temp + start
            print(end, end=" ")


if __name__ == "__main__":
    fib = FiboSeries(5)
    fib._fibo_series()
