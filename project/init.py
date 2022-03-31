import project
import make_xlsx

with open("in.txt") as file:
    number_of_fractions = int(file.readline())
    number_of_floors = int(file.readline())
    maximum_value = int(file.readline())

result = project.main(number_of_fractions, number_of_floors, maximum_value)
print(result)
make_xlsx.create_table(result)

