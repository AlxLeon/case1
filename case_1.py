from datetime import datetime, date

def get_birthday():
    day = int(input("Введите день вашего рождения: "))
    month = int(input("Введите месяц вашего рождения (числом): "))
    year = int(input("Введите год вашего рождения: "))
    return day, month, year

def get_day_of_week(day, month, year):
    date = datetime(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_age(day, month, year):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

def draw_digit(digit):
    patterns = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "    *", " **  ", "**** "],
        '3': [" *** ", "*   *", "    *", "*   *", " *** "],
        '4': ["*   *", "*   *", " ****", "    *", "    *"],
        '5': ["**** ", "*    ", "**** ", "   * ", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["**** ", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }
    return patterns[str(digit)]

def draw_date(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    
    digits = list(day_str + month_str + year_str)
    lines = [''] * 5
    
    for digit in digits:
        pattern = draw_digit(int(digit))
        for i in range(5):
            lines[i] += pattern[i] + " "
    
    for line in lines:
        print(line)

# Основная программа
day, month, year = get_birthday()
print(f"Вы родились в {get_day_of_week(day, month, year)}")
print(f"{year} - этот год {'високосный' if is_leap_year(year) else 'не високосный'}")
print(f"Вам сейчас {calculate_age(day, month, year)} лет")
draw_date(day, month, year)
