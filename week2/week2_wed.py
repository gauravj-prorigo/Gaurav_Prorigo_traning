
class NumberCheck:
    def get_number(self):
        try:
            num = int(input("Enter an integer: "))
            print("You entered:", num)
        except ValueError:
            print("Invalid input! Please enter a number.")

obj = NumberCheck()
obj.get_number()
