class OperatingSystem:
    multiTasking = True
    name = "MacOS"
class Apple:
    website = 'www.apple.com'
    name = "Apple"
class MacOS(OperatingSystem, Apple):
    def __init__(self):
        if self.multiTasking is True:
        # The class MacOS has inherited 'multitasking' attribute from the class OperatingSystem and 'website' attribute from the class 'Apple' 
            print("MacOS is a multitasking operating system. Visit {} for more details".format(self.website))
            print("Name: ", self.name)
            
mac = MacOS()

# Multilevel
class Apple:
    website = 'www.apple.com'

class MacBook(Apple):
    deviceType = 'notebook computer'

class MacBookPro(MacBook):
    def __init__(self):
    # This class inherits deviceType from the base class MacBook. It also inherits website from base class of MacBook, which is Apple.
        print("This is a {}. Visit {} for more details".format(self.deviceType, self.website))
 
macBook = MacBookPro()