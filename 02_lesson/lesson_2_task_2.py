def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


year_now = 2025
result = is_year_leap(year_now)
print(f"год {year_now}: {result}")
