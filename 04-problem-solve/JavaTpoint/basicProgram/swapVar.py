class SwapValue():

    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val

    def tempApproach(self):
        temp = self.first_val
        self.first_val = self.second_val
        self.second_val = temp
    
    def commaApproach(self):
        self.first_val, self.second_val = self.second_val, self.first_val

    def arithmeticApproach(self):
        self.first_val = self.first_val + self.second_val
        self.second_val = self.first_val - self.second_val
        self.first_val = self.first_val - self.second_val

if __name__== '__main__':
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))
    values = SwapValue(first_val, second_val)
    #values.tempApproach()
    print("Temporary Approach")
    print(values.first_val,values.second_val)
    #values.commaApproach()
    print("Comma Approach")
    print(values.first_val,values.second_val)
    values.arithmeticApproach()
    print("Arithmatic Approach")
    print(values.first_val,values.second_val)

