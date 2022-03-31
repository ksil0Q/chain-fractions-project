import project
import make_xlsx
import re


with open("in.txt") as file:
    number_of_fractions = int(re.findall(r"\d+", file.readline())[0])
    number_of_floors = int(re.findall(r"\d+", file.readline())[0])
    maximum_value = int(re.findall(r"\d+", file.readline())[0])


result = project.main(number_of_fractions, number_of_floors, maximum_value)
make_xlsx.create_table(result)
