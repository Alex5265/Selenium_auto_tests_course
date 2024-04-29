from collections import ChainMap
from random import randint

def get_damage(unit, damage):
    damage = damage - unit['armor']
    if damage > 0:
        unit['HP'] -= damage

rome_soldiers = {
    'country': 'Rome',
    'HP'     : 100,
    'armor'  : 10,
    'damage' : 25,
    'type'   : 'пехота',
    'coords' : None
    }

archer = {
    'HP'    : 50,
    'armor' : 10,
    'damage': 100,
    'type'  : 'лучник'
    }

heavy_soldier = {
    'HP'    : 150,
    'armor' : 30,
    'damage': 50,
    'type'  : 'бронированный пехотинец'
    }

light_soldier = ChainMap({}, rome_soldiers)
archer1 = ChainMap({}, archer, rome_soldiers)
heavy_soldier1 = ChainMap({}, heavy_soldier, rome_soldiers)
heavy_soldier2 = ChainMap({}, heavy_soldier, rome_soldiers)

print('light_soldier :', light_soldier, end='\n\n')
print('archer1 :', archer1, end='\n\n')
print('heavy_soldier1 :', heavy_soldier1, end='\n\n')
print('heavy_soldier2 :', heavy_soldier2, end='\n\n')

print('наносим 50 единиц урона юнитам archer1 и heavy_soldier1:', end='\n\n')
get_damage(archer1, 50)
get_damage(heavy_soldier1, 50)

print('light_soldier :',  *light_soldier.items(), end='\n\n')
print('archer1 :',        *archer1.items(), end='\n\n')
print('heavy_soldier1 :', *heavy_soldier1.items(), end='\n\n')
print('heavy_soldier2 :', *heavy_soldier2.items(), end='\n\n')

print('ещё раз наносим 50 единиц урона юниту heavy_soldier1:', end='\n\n')
get_damage(heavy_soldier1, 50)

print('heavy_soldier1 :', *heavy_soldier1.items(), end='\n\n')



create_light_soldier = lambda: ChainMap({}, rome_soldiers)
create_archer        = lambda: ChainMap({}, archer, rome_soldiers)
create_heavy_soldier = lambda: ChainMap({}, heavy_soldier, rome_soldiers)

# теперь в вышеуказанных переменных будет храниться объект-функция, которая при вызове вернёт новый
# объект ChainMap со своим отдельным словарём "верхнего слоя", т.е. нового уникального солдата
# достаточно вызвать эти функции нужное количество раз в циклах и вуаля:

army = []
army.extend([create_light_soldier() for _ in range(10)])
army.extend([create_archer() for _ in range(5)])
army.extend([create_heavy_soldier() for _ in range(5)])

for soldier in army:
    damage = randint(0, 50)
    get_damage(soldier, damage)
    print(id(soldier), soldier['HP'])