class LcmAndHcf():

    def __init__(self):
        self.first_num = int(input("Enter first number: "))
        self.second_num = int(input("Enter second number: "))


    def calculate_lcm(self):
        if self.first_num > self.second_num:
            greater = self.first_num
        else:
            greater = self.second_num

        while(True):
            if((greater%self.first_num==0) and (greater%self.second_num==0)):
                lcm = greater
                break
            greater += 1
        return lcm
    
    def calculate_hcf(self):
        if self.first_num > self.second_num:
            smaller = self.second_num
        else:
            smaller = self.first_num
        for i in range(1, smaller+1):
            if((self.first_num%i==0) and (self.second_num%i==0)):
                hcf = i    
        return hcf

if __name__ == "__main__":
    value = LcmAndHcf()
    print(f'Lcm is: {value.calculate_lcm()}')
    print(f'hcf is: {value.calculate_hcf()}')

