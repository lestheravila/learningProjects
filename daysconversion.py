from helper import validation




days = ''
while days != 'exit':
    days = input('enter days: ')
    days_unit = days.split(':')
    print(days_unit)
    days_unit_dictionary = {'days': days_unit[0], 'unit': days_unit[1]}
    print(days_unit_dictionary)
    validation(days_unit_dictionary)
    print('Type exit if you want to exit')