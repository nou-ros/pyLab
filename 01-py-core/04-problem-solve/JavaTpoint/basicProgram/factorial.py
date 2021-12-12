class Factorial():
    def loop_fact(self, num):
        fact = 1
        for i in range(1, num+1):
            fact *= i 
        return fact
    
    def recur_fact(self, num):
        if num < 1:
            return 1
        else:
            return num * self.recur_fact(num-1)

if __name__ == "__main__":
    fact = Factorial()
    result = fact.loop_fact(5)
    print(result)
    facto = Factorial()
    res = fact.recur_fact(5)
    print(res)
    
