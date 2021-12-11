class Converter():
    def __init__(self, temp):
        self.__freezing_point = 32
        self.__devision = 5/9
        self.temp = temp

    def far_to_cel(self):
        cel = (self.temp - self.__freezing_point) * self.__devision
        return round(cel, 2)
    
    def cel_to_far(self):
        far = self.temp * (1/self.__devision) + self.__freezing_point
        return round(far, 2)


if __name__ == "__main__":
    value = Converter(234)
    print(value.far_to_cel())