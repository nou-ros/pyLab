# print(__name__)
print(f'Fist module\'s name is: {__name__}')

def main():
    print('Run directly. I am first module main')

if __name__ == '__main__':
    main()
else:
    print('Run from import')