# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите каждый элемент построчно,
# поместив между ними 5 символов *.

heroes = input("Enter the character names in Ninja Turtles: ").split()

bad_guys = open('bad_guys.txt', 'w')
good_guys = open('good_guys.txt', 'w')
for i in heroes:
    if i in ("Leonardo", "Donatello", "Raphael", "Michelangelo"):
        good_guys.write(i + "\n")
    elif i in ("Shredder", "Bebop", "Rocksteady"):
        bad_guys.write(i + "\n")

bad_guys = open('bad_guys.txt', 'r')
good_guys = open('good_guys.txt', 'r')
Heroes = good_guys.read().strip()
Enemys = bad_guys.read().strip()
print(f'Heroes: {Heroes}')
print(f"Enemys: {Enemys}")

bad_guys.close()
good_guys.close()
