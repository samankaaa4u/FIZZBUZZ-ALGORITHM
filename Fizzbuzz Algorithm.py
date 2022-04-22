class Fizzbuz:
    def fizzbuz(self):
        for num in range(6):
            if num % 3 == 0 and num % 5 == 0:
                print("fizzbuzz")
                continue
            elif num % 3 == 0:
                print("fizz")
                continue
            elif num % 5 == 0:
                print("buzz")
                continue
            print(num)

test = Fizzbuz()
result = test.fizzbuz()