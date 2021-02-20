
NUMBERS = [12, 123, 234, 90, 1289, 1289, 82, 62, 78, 89, 50]

def pair_number(number):
    if number % 2 == 0:
        return True

pairs = list(filter(pair_number, NUMBERS))
pairs.sort()
print(pairs)