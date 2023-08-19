#Counting letter in each word and storing it in a dictionary

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)

#Converting a list of Celsius temperatures into Fahrenheit

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
}
            #New Key   #New Value
weather_f = {day : (temp_c*9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)