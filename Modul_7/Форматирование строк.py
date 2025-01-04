# Использование %
team1_num = 5
team2_num = 6
# Использование format
score_1 = 40
score_2 = 42
# Использование f-строк
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print('В команде мастера кода участников: %s!' % team1_time)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда Волшебники данных решили задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print('Победа команды Мастера кода!'
      if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time)
      else 'Победа команды Волшебники Данных' if score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time)
      else 'Ничья!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!')


