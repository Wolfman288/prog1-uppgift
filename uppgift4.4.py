meter = int(input('Släpp bollen från: '))

centimeter = 100 * meter
studs = 0

while centimeter > 1:
    centimeter = centimeter * 0.7
    studs += 1

print(f'studs: {studs}')