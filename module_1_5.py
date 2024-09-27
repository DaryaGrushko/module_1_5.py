immutable_var = ('Darya', 'Grushko', 'Sarov', True, 2024, [0,1])
print('Кортеж : ', immutable_var)
#immutable_var[0] = 100 # кортежи нельзя менять
mutable_list = ['Sasha', 'Ivanov', 'Sochi', False, 2000, [10,1]]
print('Список : ', mutable_list)
mutable_list[0] = 1
mutable_list[1] = 'Rita'
print('Список измененный : ', mutable_list)