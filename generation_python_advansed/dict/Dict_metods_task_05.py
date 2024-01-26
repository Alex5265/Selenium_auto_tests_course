# Методы словарей
# Доступен список питомцев содержащие инфо о собаках и владельцах.
# Каждый элемент списка - кортеж (кличка, фамилия, имя, возраст).
# Необходимо преобразовать в словарь чтобы владелец был в кортеже, а питомец в списке.


pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}


for pet, *owner in pets:
    result.setdefault(tuple(owner), []).append(pet)

print(result)

