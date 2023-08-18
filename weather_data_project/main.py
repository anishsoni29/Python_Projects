import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)


#A dataframe is a 2 dimensional data structure, like a table or spreadsheet.
#A series is like a column of info

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = int(sum(temp_list)/ len(temp_list))
# print (avg)

# print(data["temp"].mean())
# print(data["temp"].max())

print(data[data.temperature == data.temperature.max()])

