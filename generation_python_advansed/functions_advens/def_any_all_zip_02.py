# Используя параллельную итерацию сразу по трем спискам
# countries, capitals и population выведите информацию о стране в формате:




countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]


# с помощью зип соединяем 3 списка и тут же циклом фор разбиваем их
for cap,count,pop in zip(capitals,countries,population):
    print(f'{cap} is the capital of {count}, population equal {pop} people.')




