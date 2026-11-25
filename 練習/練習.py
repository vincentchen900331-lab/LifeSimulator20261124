def death_reason(age):
    if age <= 20:
        natural_rate = 1
    elif age > 20 and age <= 30:
        natural_rate = (age - 20) * 0.4 + 1
    elif age > 30 and age <= 40:
        natural_rate = (age - 30) * 1 + 5
    elif age > 40 and age <= 50:
        natural_rate = (age - 40) * 1 + 15
    elif age > 50 and age <= 60:
        natural_rate = (age - 50) * 2 + 25
    elif age > 60 and age <= 70:
        natural_rate = (age - 60) * 2 + 45
    elif age > 70 and age <= 80:
        natural_rate = (age - 70) * 2 + 65
    elif age > 80 and age <= 90:
        natural_rate = (age - 80) * 1 + 85
    else:
        natural_rate = 95
    return natural_rate

print(f"{death_reason(25):.0f}")
print(death_reason(45))
print(death_reason(65))
print(death_reason(95))