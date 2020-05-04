import csv
import glob
import os
import pandas
import sys

print("***NAPOMENA***\n\n\nProgram je interaktivan, posle svakog unosa se postavlja pitanje za dalji korak.\n")
print("Na pitanja na koja su odgovori da ili ne, ukoliko je odgovor da moze da se odgovori sa 1, da ili Da.")
print("Ukoliko je odgovor ne, moze da se odgovori sa 2, ne ili Ne.\n")
print("Prvo se unosi putanja gde ce se sacuvati novi izvestaj, a zatim i njegovo ime.")
print("Zatim se unose izvestaji od kojih se pravi novi izvestaj. Potrebno je uneti punu putanju izvestaja.")
print("Nakon toga, program ce izlastiti listu svih imena koji se pojavljuju u unetim izvestajima")
print("i pita se da se unesu imena za novi izvestaj.\n")
print("Na kraju se postavlja pitanje sta uraditi sa odabranim imenina. Postoje dve opcije.")
print("Prva je da se izlistaju svi dogadjaji za izabrana imena, a druga samo poslednji\n\n\n\n")




#Korisnik unosi putanju gde zeli da cuva novi izvestaj i kako ce se izvestaj zvati
final_report_path = input("Unesite putanju gde želite da bude kreiran novi izveštaj:\n")
final_report_name = input("Unesite ime novog izveštaja: ")
final_report_full_path = final_report_path + final_report_name + ".csv"
final_report_full_path_test = final_report_path + final_report_name + "_test" + ".csv"
"""
final_report_path - putanja gde ce se naci novi izvestaj; korisnik unosi
final_report_name - ime novog izvestaja; korisnik unosi
final_report_full_path - puno ime izvestaja; spaja putanju, ime i dodaje csv ekstenziju na kraju
final_report_full_path_test - isto kao gornja promenljiva, samo jos dodaje i test; potrebna zbog logike programa
"""




#Korisnik unosi izvestaje koje zeli da obradi
file_list = []
checker1 = 1
while checker1 < 2:
    report_path = input("Unesite punu putanju izveštaja koji želite da obradite:\n")
    file_list.append(report_path)
    more_reports = input("Da li želite da unesete još izveštaja?\n1.Da\n2.Ne\n")
    if (more_reports == "2" or more_reports == "Ne" or more_reports == "ne"):
        checker1 = 2
    elif (more_reports == "1" or more_reports == "Da" or more_reports == "da"):
        checker1 = 1
#print(file_list)
"""
file_list - lista putanji izvestaja od koje se pravi novi izvestaj; unosi korisnik
checker1 - provera za while petlju
report_path - putanja izvestaja koja se koristi za novi izvestaj; dodaje se u file_list; korisnik unosi
more_reports - pita se korisnik da li zeli da unese jos izvestaja
"""




#Spajanje izvestaja u jedan csv file
file_list_csv = []
for filename in file_list:
    read_as_csv = pandas.read_csv(filename, header=None)
    file_list_csv.append(read_as_csv)
concatFL = pandas.concat(file_list_csv,axis=0)
concatFL.to_csv(final_report_full_path_test,index=None)
"""
file_list_csv - lista izvestaja od koje se pravi novi izvestaj otvoreni u csv formatu
read_as_csv - promenljiva koja cita izvestaj u csv formatu
concatFL - uneti izvestaji spojeni u jedan csv file
"""




#Određivanje broja kolona i redova u spojenom csv file-u
with open(final_report_full_path_test, "r") as csvfile:
    reader = csv.reader(csvfile)
    field = {}
    c1 = 0
    for row in reader:
        field[c1] = row
        number_of_columns = len(field[0])
        number_of_rows_temp = len(field)
        c1 = c1+1
#print(field)
"""
field -
reader - promenljiva za citanje csv file-a
number_of_columns - broj kolona spojenog csv file-a
number_of_rows_temp - broj redova spojenog csv fila-a; ima jedan red viska (to je prvi red)
"""




#Pravljenje matrice od csv file-a
with open(final_report_full_path_test, "r") as csvfile:
    reader = csv.reader(csvfile)

    matrix_help = [[0 for i in range(number_of_columns)] for j in range(number_of_rows_temp)]
    c2 = 0
    for row in reader:
        for j in range(number_of_columns):
            matrix_help[c2][j] = row[j]
        c2 = c2+1
#print(matrix_help)
"""
reader - promenljiva za citanje csv file-a
matrix_help - privremena matrica; prvi red je visak
"""




#Pravljenje matrice sa izbacenim prvim redom
number_of_rows = number_of_rows_temp-1

matrix = [[0 for i in range(number_of_columns)] for j in range(number_of_rows)]
c3 = 0
for i in range(1,number_of_rows_temp):
    matrix[c3] = matrix_help[i]
    c3 = c3+1
#print(matrix)
""" 
number_of_rows - broj redova finalne matrice 
matrix - finalna matrica spojenog csv file-a
"""        



       
#Predstavljane korisniku listu imena koju moze da izabere:
        
#Pravljenje liste svih username-ova (biće i ponovljenih
c4 = 0
array_of_usernames = []
for i in range(number_of_rows):
    array_of_usernames.append(matrix[c4][0])
    c4 = c4+1
#print(array_of_usernames)
"""
array_of_usernames - lista svih username-ova koji se pojavljaju u izvestaju; ponajvljaju se
"""




#Izdvajanje iz liste ponovljenih username-ova (svaki se pojavljuje samo jednom)
usernames = []
for i in array_of_usernames:
    if i not in usernames:
        usernames.append(i)        
#print(usernames)
"""
usernames - lista svih username-ova koji se pojavljaju u izvestaju; ne ponavljaju se
"""




#Odabir željenih imena za izveštaj
c5 = 1
print("Dostupna imena: ")
for i in usernames:
    print(str(c5) + ". " + str(usernames[c5-1]))
    c5 = c5+1




#Određivanje broj ponavljanja izabranih imena u izveštaju, zbog nove matrice

#Pravljenje niza odbranih imena
checker2 = 1
user_choise_array = []
while checker2 < 2:
    users_choise = input("Unesite željeno ime koje želite da se pojavi u novom izveštaju:\n")
    user_choise_array.append(users_choise)
    more_names = input("Da li želite da unesete još neko ime?\n1.Da\n2.Ne\n")

    if (more_names == "2" or more_names == "Ne" or more_names == "ne"):
        checker2 = 2
    elif (more_names == "1" or more_names == "Da" or more_names == "da"):
        checker2 = 1
#print(user_choise_array)
"""
checker2 - provera za while petlju
user_choise_array - lista imena koju je korisnik izabrao 
users_choise - korisnikov unos 
more_names - korisnik se pita da li zeli jos neko ime da unese
"""




#Odredjevanje broj ponavljanja svakog imena u spojenom csv file-u
number_of_rows_for_new_matrix = 0
number_of_repeating_array = []
c6 = 0
for i in user_choise_array:
    for j in array_of_usernames:
        if(i == j):
            c6 = c6+1
            number_of_rows_for_new_matrix = number_of_rows_for_new_matrix+1
    number_of_repeating_array.append(c6)
    c6 = 0
print(number_of_repeating_array)
"""
number_of_rows_for_new_matrix -
number_of_repeating_array - niz broja ponavljanja svakog od izabranih imena
"""




#Sortiranje ove matrice




#Pravljenje matrice za prvi slucaj - za sve dogadjaje za izabrana imena
matrix_new = [[0 for i in range(number_of_columns)] for j in range(number_of_rows_for_new_matrix)]
c7 = 0
c8 = 0
for j in range(len(user_choise_array)):
    for i in range(number_of_rows):
        if(user_choise_array[c8] == matrix[i][0]):
            matrix_new[c7] = matrix[i]
            c7 = c7+1
    c8 = c8+1
print(matrix_new)
"""
matrix_new -
"""



 
#Pravljenje matrice za drugi slucaj - samo poslenji dogadjaji za odabrana imena
matrix_sort = [[0 for i in range(number_of_columns)] for j in range(number_of_rows_for_new_matrix)]
c9 = 0

for i in range(len(user_choise_array)):
    c10 = 0
    matrix_sort_help = [[0 for i in range(number_of_columns)] for j in range(number_of_repeating_array[i])]
    name = user_choise_array[i]

    
    for j in range(number_of_rows_for_new_matrix):
        if name == matrix_new[j][0]:
            matrix_sort_help[c10] = matrix_new[j]
            c10 = c10+1

    #Konvertovanje kolone u kojoj su vrednosti u int-ove
    for p in range(number_of_repeating_array[i]):
        t = int(matrix_sort_help[p][1])
        matrix_sort_help[p][1] = t

    #Selection sort algoritam
    for q in range(number_of_repeating_array[i]):
        min_idx = q
        for r in range(q+1, number_of_repeating_array[i]):
            if matrix_sort_help[min_idx][1] > matrix_sort_help[r][1]:
                min_idx = r
        matrix_sort_help[q], matrix_sort_help[min_idx] = matrix_sort_help[min_idx],  matrix_sort_help[q]

    #Popunjavanje sortirane matrice                  
    for m in range(number_of_repeating_array[i]):
        matrix_sort[c9] = matrix_sort_help[m]
        c9 = c9+1
print(matrix_sort)




#Izdvajanje poslednjeg 
matrix_last_appearance = [[0 for i in range(number_of_columns)] for j in range(len(user_choise_array))]

c10 = -1
for i in range(len(user_choise_array)):
    c10 = c10+number_of_repeating_array[i]
    matrix_last_appearance[i] = matrix_sort[c10]
print(matrix_last_appearance)



#Deo u kojem se korisniku postavlja izbor sta zeli da dobije u novom izvestaju
#Prva opcija je da u novom izvestaju budu svi dogadjaji vezani za izabrana imena
#Druga opcija je da u novom izvestaju budu samo poslednji dogadjaji vezani za izabrana imena
print("\n1. Svi događaji vezani za izabrano ime(imena)")
print("2. Poslednji događaji vezani za izabrana ime(imena)")
users_choise2 = input("Odaberite željenu akciju: ")

if (users_choise2 == "1"):
    with open(final_report_full_path, "w", newline= '') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(number_of_rows_for_new_matrix):
            writer.writerow(matrix_sort[i])    
elif (users_choise2 == "2"):
    with open(final_report_full_path, "w", newline= '') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(user_choise_array)):
            writer.writerow(matrix_last_appearance[i])

os.remove(final_report_full_path_test)











































