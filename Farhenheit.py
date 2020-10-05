choice = input("Vill du konvertera Fahrenheit[F] eller Celcius[C]?")

converted = 0

if choice == "F":
f = float(input('Temperatur i Fahrenheit? '))
converted = (temp - 32) * 5 / 9
elif:
temp = float(input('Temperatur i Celcius? '))
converted = temp * 9 / 5 + 32

print(f'Det är {converted:.1f} grader')

#c = (f - 32) * 5 / 9
#c = f * 9 / 5 + 32