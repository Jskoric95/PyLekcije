print("Dobrodošli u fizzbuzz igru!")

end = input("Molim Vas unesite broj od 1 do 100: ")
end = int(end)  # convert string into number

for broj in range(1, end+1):
    if broj % 3 == 0 and broj % 5 == 0:
        print("fizzbuzz")
    elif broj % 3 == 0:
        print("fizz")
    elif broj % 5 == 0:
        print("buzz")
    else:
        print(broj)