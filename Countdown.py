from datetime import datetime


def countdown_goal():
    user_input = input('Enter your goal with a date deadline(goal:mm/dd/yyyy)\n')

    input_list = user_input.split(':')

    goal = input_list[0]
    deadline = input_list[1]

    deadline_date = datetime.strptime(deadline, '%m/%d/%Y')
    date_today = datetime.today()
    countdown = deadline_date - date_today

    print(f'Time remaining for you goal: {goal} is {countdown.days} days')


countdown_goal()


