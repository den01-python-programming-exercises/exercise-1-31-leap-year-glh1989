def main():
    number = int(input("Give a year "))
      
    if (number % 4 == 0):
        print("The year is a leap year")
    elif (number % 100 == 0 and number % 400 == 0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")


if __name__ == '__main__':
        main()