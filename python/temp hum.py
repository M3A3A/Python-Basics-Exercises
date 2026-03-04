temp = int(input("Enter The Tempreture : "))
hum = int(input("Enter The Humidty :"))

if temp <= 22 :
    print("Heater On ; Cooler Off")
elif temp >= 27 :
    print("Cooler On ; Heater Off")
if hum <= 30 : 
    print("HF Is On ; Fan Is Off")
elif hum >= 35 :
    print("Fan Is On ; HF Is Off")