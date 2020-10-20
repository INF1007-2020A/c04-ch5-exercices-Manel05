#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for i in prefixes :
        names.append(i + suffixe)

    return names


def prime_integer_summation() -> int:
    nombre = 6
    my_list = [2, 3, 5]
    while len(my_list) < 100 :
        prime = True
        for i in range (2, nombre//2) : #s'il y a pas de diviseurs avant la moitiee il y a pas de diviseurs
            if nombre % i == 0 and prime == True :
                prime = False
        if prime == True :
            my_list.append(nombre)
        nombre +=1
    return sum(my_list)


def factorial(number: int) -> int:
    factorielle = 1
    for i in range(2,number+1) :
        factorielle = factorielle * i
    return factorielle


def use_continue() -> None:
    for i in range(10) :
        if i == 5 :
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accepted = []
    for sub_group in groups :
        if len(sub_group) > 10 or len(sub_group) <= 3 :
            accepted.append(False)
            continue
        if 25 in sub_group :
            accepted.append(True)
            continue
        if 50 in sub_group :
            is_50 = True
        else:
            is_50 = False
        ok = True
        for age in sub_group :
            if age < 18 :
                ok = False
                break
            elif age > 70 :
                if is_50 == True :
                    ok = False
                    break
        accepted.append(ok)


    return accepted


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
