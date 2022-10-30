def triertableau(tableau):
    i = 0
    while i < len(tableau) - 1:
        if tableau[i + 1] < tableau[i]:
            tabp1 = tableau[i + 1]
            tab = tableau[i]
            tableau[i] = tabp1
            tableau[i + 1] = tab
            i = -1
        i += 1
    print('Tableau trié :', tableau)
    return tableau


def supprimerdoublon(tableau):
    i = 0
    while i < len(tableau):
        valeurcible = tableau[i]
        j = i + 1
        while j <= len(tableau) - 1:
            if tableau[j] == valeurcible:
                del tableau[j]
                j -= 1
            j += 1
        i += 1
    print('Tableau sans doublon :', tableau)
    return tableau


def fusionertableau(tableau, tableau2):
    for i in tableau2:
        tableau.append(i)
    print('Tableau fusionné : ', tableau)
    return tableau


tableau = [8, 3, 2, 7, 9, 11, 10, 18, 4.1, 4, 8, 3, 150, 110, -4, 33, 26, 98, 178, 150, 10086, 4, 11, 9, 68, 63, 34, 45,
           45, 45, 68, 10086, 10086]
print('\nTableau initial :', tableau, '\n')

tableau = triertableau(tableau)
tableau = supprimerdoublon(tableau)

tableau2 = [4, 8, 2, 90, 45, 180, 126, 76, 1769, 546, 150, 63, 45, 98, -189, 22, 110, 4.1]
print('\nNouveau tableau : ', tableau2)
print('Ancier tableau : ', tableau)
tableau3 = fusionertableau(tableau, tableau2)
tableau3 = triertableau(tableau3)
tableau3 = supprimerdoublon(tableau3)
