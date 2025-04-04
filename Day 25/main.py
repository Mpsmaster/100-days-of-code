# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)
import csv
import pandas

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# data_temp = data["temp"]
# data_temp_list = data["temp"].to_list() 
# data_temp_avarage = sum(data_temp_list) / len(data_temp_list)
# print(int(data_temp_avarage))
# temp_max = data_temp.max()
# max_row = data[data_temp == temp_max] 
# print(max_row)
# monday = data[data.day == "Monday"]
# celsius = monday.temp[0]
# celsius = (celsius * 9/5) + 32
# print(celsius)    
data = pandas.read_csv("Central_Park.csv")
print(data)
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()

gray = fur_color_list.count("Gray")
cinnamon = fur_color_list.count("Cinnamon")
black = fur_color_list.count("Black")
print(f"Gray: {gray}")
print(f"Cinnamon: {cinnamon}")
print(f"Black: {black}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")