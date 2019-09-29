import operator
action = {
"+": operator.add,
"-": operator.sub,
"/": operator.truediv,
"*": operator.mul,
"**": pow
}
try:
  first_num = int(input("Введите первое число(int): "))
  second_num = int(input("Введите второе число(int): "))
except ValueError:
  raise Warning("Я просил ввести число")
try:
  act = input("""Что сделать с этими числами?\n
  + сложить\n
  - вычесть\n
  / разделить\n
  * перемножить\n
  ** возвести в степень\n""")
  answer = action[act](first_num, second_num)
except KeyError:
  raise Warning("Неправильно указанно действие")
except ZeroDivisionError:
  raise Warning("На 0 делить нельзя")
print(f"Ответ - {answer}")
