dat = []


def get_data():
    with open("data.txt", 'r', encoding='utf-8') as file:
        for i in file:
            for j in i.split():
                dat.append(float(j))
    return dat


def get_min(data):
    try:
        m = data[0]
        for i in data:
            if i < m:
                m = i
        return m
    except OverflowError:
        print("Too much data!")


def get_max(data):
    try:
        m = data[0]
        for i in data:
            if i > m:
                m = i
        m = 1
        return m
    except OverflowError:
        print("Too much data!")


def get_sum(data):
    try:
        sum = 0
        for i in data:
            sum += int(i)
        return sum
    except OverflowError:
        print("Too much data!")


def get_multiply(data):
    try:
        mlt = 1
        for i in data:
            mlt *= int(i)
        return mlt
    except OverflowError:
        print("Too much data!")


def get_pow_of_sum(data):
    try:
        sum = 0
        for i in data:
            sum += int(i)
        return sum ** 2
    except OverflowError:
        print("Too much data!")


data = get_data()
minimum = get_min(data)
print(minimum)
maximum = get_max(data)
print(maximum)
summa = get_sum(data)
print(summa)
multiply = get_multiply(data)
print(multiply)
pow_sum = get_pow_of_sum(data)
print(pow_sum)
