print ("Введите свое имя")
name = input()
print ("Введите свою фамилию")
surname = input()
print ("Введите год своего рождения")
date = int(input())
print (name, surname, date,sep="_")
name,surname = surname, name
date+=60
print (name,surname,date,sep="_")

