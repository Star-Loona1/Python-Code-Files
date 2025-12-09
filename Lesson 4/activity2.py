print("Enter marks got in 4 subjects: ")
maths = int(input("Maths: "))
science =int(input("Science: "))
hindi = int(input("Hindi: "))
english = int(input("English: "))

sum = maths+science+hindi+english
print("The sum of maths, science, hindi and english: ", sum)

perc = (sum/400)*100
print("Percentage Mark = ")
print(perc)