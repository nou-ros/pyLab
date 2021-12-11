class LeapYearCheck():
    def __init__(self, year):
        self.year = year
    
    def leap_year(self):
        if self.year%4 == 0 and (self.year%100 != 0 or self.year%400 == 0):
            return 1
        else:
            return 0

if __name__ =="__main__":
    
    year = LeapYearCheck(int(input("Enter a year: ")))
    res = year.leap_year()
    if res:
        print("Leap Year!")
    else:
        print("Not a leap year")
