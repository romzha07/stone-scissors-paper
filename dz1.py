import random

def game():
    if frop == 'да' or frop == 'Да': 
      a = int(input('Введи число от 1 до 3\n'))
      if a == 1 or a == 2 or a == 3:
        b = int(random.randint(1,3))
        print('Число компьютера: ' + str(b) + '\nТвоё число: '+ str(a) )
        if a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3:
           print('Ничья')
        elif a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
           print('Ты выйграл!!!')
        elif a == 3 and b == 1 or a == 2 and b == 1 or a == 3 and b == 2:    
           print('Ты проиграл(')
      else:
        print('Введи число нормально!!!')
        game()
    else:
      print('Как хочешь(')    
       
    


print('''Правила игры камень, ножницы, бумага:
 1) 1 - это камень, 2 - это ножницы, 3 - это бумага.
 2) Ты вводишь число от 1 до 3, после чего компьютер тоже выдаёт число от 1 до 3.
 3) Цифра 1 выигрывает цифру 2, цифра 2 выигрывает цифру 3, а цифра 3 выигрывает цифру 1.''')

frop = str(input('Ты понял правила, и готов играть?\n'))
game()
while True:
   c = input('Хочешь поиграть ещё?[да/нет]\n')
   if c == 'да' or c == 'Да':
     game()
   elif c == 'нет' or c == 'Нет':
       break
   else:
     print('Ответь нормально!!!')
     continue  