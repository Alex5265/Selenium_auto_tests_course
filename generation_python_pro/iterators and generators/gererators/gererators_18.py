# Вам доступен именованный кортеж Person, который содержит данные о человеке.
# Первым элементом именованного кортежа является имя и фамилия человека,
# вторым — национальность, третьим — пол, четвертым — год рождения,
# пятым — год смерти. Если человек жив, год смерти считается равным
# 0
# 0. Также доступен список persons, содержащий эти кортежи.
#
# Дополните приведенный ниже код с использованием конвейеров генераторов,
# чтобы он вывел имя и фамилию самого молодого живого мужчины (male) из Швеции (Swedish).


from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]


country = (i for i in persons if i.nationality == 'Swedish')
gender = (i for i in country if i.sex == 'male')
alife = (i for i in gender if i.death == 0)
young = max(alife, key=lambda x: x.birth).name

print(young)



























