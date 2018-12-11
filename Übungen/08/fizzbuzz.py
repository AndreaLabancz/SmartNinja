fizzbuzz_input = raw_input("Please enter a whole number between 1 and 100: ")

fizzbuzz_input = int(fizzbuzz_input)

for number in range(1, fizzbuzz_input+1):
   if number % 3 == 0 and number % 5 == 0:
        print "fizzbuzz"
   elif number % 3 == 0:
        print "fizz"
   elif number % 5 == 0:
        print "buzz"
   else:
    print number
