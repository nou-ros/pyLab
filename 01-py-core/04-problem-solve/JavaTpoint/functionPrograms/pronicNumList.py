class PronicList():

    def __check_pronic(self, num):
        for i in range(1,num):
            if (i*(i+1))==num:
                val = i*(i+1)
                return val
        return 0

    def pronic_list(self):
        for i in range(1,100):
            res = self.__check_pronic(i)
            if res: 
                print(res)

if __name__ == "__main__":
    pronic = PronicList()
    pronic.pronic_list()
