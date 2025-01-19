
def celsius_to_fahrenheit(celsius):
    """converts celsius to fahrenheit."""
    fahrenheit=(celsius * 9/5) +32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """converts fahrenheit to celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


#Get input from the user
temp =float(input("enter temperature:"))
unit =input("enter unit (C or F):")

#perform the conversion
if unit == "C":
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}℃ is equal to {converted_temp}℉")
elif unit == "F":
     converted_temp = fahrenheit_to_celsius(temp)
     print(f"{temp}℉ is equal to {converted_temp}℃ ")
else:
    print("Invalid unit entered.")
                  
                  
        
