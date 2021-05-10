
def days_to_ unit(num_days, conversion_unit):
    if conversion_unit == 'hours':
        return f'{num_days} days are {int(num_days) * 24} hours'
    elif conversion_unit == 'minutes':
        return f'{num_days} days are {int(num_days) * 24 * 60} minutes'
    elif conversion_unit == 'seconds':
        return f'{num_days} days are {int(num_days) * 24 * 60 * 60} seconds'
    else:
        return 'Unsupported units'



def validation(days_unit_dictionary):
    try:
        user_input = int(days_unit_dictionary['days'])
        if user_input > 0:
            days_value = days_to_unit(user_input, days_unit_dictionary['unit'])
            print(days_value)
        elif user_input == 0:
            print('You entered a 0, please input positive number.')
        else:
            print('invalid input')
    except ValueError:
        print('please input a valid number!')

