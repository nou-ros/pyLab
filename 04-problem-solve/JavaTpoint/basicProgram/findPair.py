class Pairs():

    def __init__(self, nums=None, target=0):
        self._target = target
        self.__low = 0
        self.__high = len(nums) - 1
        if nums is None:
            self._nums = []
        else:
            self._nums = nums
    
    def findPair(self):
        self._nums.sort()
        while self.__low<self.__high:
            if self._nums[self.__low] + self._nums[self.__high] == self._target:
                print(f'Pair found: {self._nums[self.__low]}, {self._nums[self.__high]}')
                #return
            if self._nums[self.__low] + self._nums[self.__high] < self._target:
                self.__low = self.__low + 1
            else:
                self.__high = self.__high - 1
        return 0

class Pairs2(Pairs):

    def __init__(self, nums, target):
        super().__init__(nums, target)
        self.__pairedValue = {}
        self.__flags = 0
        
    def findPair2(self):
        for i, e in enumerate(self._nums):
            if self._target - e in self.__pairedValue:
                print(f'Pair found, {self._nums[self.__pairedValue.get(self._target-e)]}, {self._nums[i]}')
                self.__flags+=1
            self.__pairedValue[e] = i
        if self.__flags==0:
            print('pair not found')
            return 


if __name__ == '__main__':
    nums = [8,7,2,5,3,1]
    target = 10
    # fp = Pairs(nums, target)
    # print(fp._Pairs__low)
    # fp.findPair()
    fp = Pairs2(nums, target)
    fp.findPair2()
