
def z1():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                     "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                     "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(f"Ваш словарь: {countries_dict}")
    print(f"Столица Германии - {countries_dict['Германия']}")
    for i in sorted(countries_dict):
        print(i, "-", countries_dict[i])

def z2():
    alp = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    w = input(" Введите слово: ")
    s = 0
    for i in w:
        s+= alp[i.lower()]
    print("Сумма", s)

def z3():
    import random
    students = ["Петров", "Иванов", "Сидоров", "Радин", "Дружини"]
    languages = ["Английский", "Китайский", "Японский", "Русский", "Испанский", "Арабский", "Французкий", "Корейский", "Португальский", "Испанский"]
    dict = {}
    for student in students:
        lan = []
        for i in range(random.randint(1, 4)):
            lan.append(random.choice(languages))
        dict[student] = sorted(list(set(lan)))
    print(dict)
    china = []
    for student in students:
        print(f"{student} знает {len(dict[student])} языка")
        if "Китайский" in dict[student]:
            china.append(student)
    if len(china) > 0:
        print(f"{china} знает китайский")
    else:
        print("Никто не знает китайский")


z1(), z2(), z3()
