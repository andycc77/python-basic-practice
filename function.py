def check_leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year & 4 == 0):
        return True, "這個是閏年"
    else:
        return False, "這個是平年"


year = int(input('請輸入年份'))

print(check_leap_year(year))
