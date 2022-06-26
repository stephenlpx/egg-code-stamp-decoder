
import csv

farming_method = {
    "0": "Organic",
    "1": "Free range",
    "2": "Barn",
    "3": "Cage"
}
print("")
print("Enter the code on the egg to find out more information")
code_input = input("Enter the code (example: 1UK54321) : ")

#create dictionary from the country codes file
with open("country-codes.txt") as data_file:
    data = csv.reader(data_file)
    for rows in data:
        dict = {rows[0]:rows[1] for rows in data}



method = code_input[0]
country_origin = code_input[1:3]
farm_id = code_input[3:8]

print("")
print(f"{farming_method[method]} egg\nCountry of Origin: {dict[country_origin]}\nFarm Id: {farm_id}")





