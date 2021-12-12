class Disarium():
    length = 0

    def __calculate_length(self, numb):
        digits = 0
        while(numb!=0):
            digits += 1
            numb = numb//10
        Disarium.length = digits
        return Disarium.length

    def check_disarium(self, value):
        rem=total=0
        num_len = self.__calculate_length(value)
        while(value>0):
            rem = value%10
            total += int(rem**num_len)
            value = value//10
            num_len -= 1
        
        return total
        '''
        if total == self.number:
            print('Disarium')
        else:
            print("not disarium")
        ''' 
    def range_disarium(self, start, end):
        for i in range(start, end):
            res = self.check_disarium(i)
            if(res == i):
                print(i);

if __name__ == '__main__':
    num = Disarium()
    num.range_disarium(1,101)

