import random
import string
#  print("Wendel Hector\n\n\n")
#  #Premye pati
# #nimero 1
# chen_karakte = input("Antre yon fraz avek majiskil: ")
# print("Chen nan an miniskil net:"+chen_karakte.lower())

# # #nimero 2
# chen = input("Antre yon chen karakte: ")

# b = chen.split()
# print(b)

# #nimero 3
# chen_ti = input("Antre yon chen: ")
# d = chen_ti.title()
# print(d)

# #nimero 4
# teks = input("Antre yon text: ")
# delimite = teks.split()
# nouvo = " "
# for mo in delimite:
#      premye = mo[0]
#      nouvo +=premye
# print("["+nouvo+"]")

# #nimero 5
# chen_karakte = input("Antre yon chen: ")
# ansyen = 'a'
# nouvo = '@'
# nouvo_chenn = " "
# for let in chen_karakte:
#     if let == ansyen:
#         nouvo_chenn += nouvo
#     else: nouvo_chenn += let
# print(nouvo_chenn)


# #nimero 6
# c_k = input ("Antre yon chenn karakte: ")
# n_c = c_k[:: -1].upper()
# print(n_c)

# #nimero 7
# antre = input("Antre yon chenn ki gn plizye <a> ladanl: ")
# karak = 'a'
# endis = -1
# endis = antre.find(karak)
# if endis != -1:
#     print(endis)
# else: print("karakte sa pa nan chenn nan")

# #nimero 8
# antre_chen = input("antre yon chen ki gen <a> ladanl: ")
# karak = 'a'
# som = 0
# for e, karakte in enumerate(antre_chen):
#     if karakte.lower() == karak:
#         som +=e
# print(som)

# #nimero 9
# Vf = input("Antre yon chen ki gn karakte <a> ladanl: ")
# lis = [ ]

# for w, ka in enumerate(Vf):
#     if ka == 'a':
#         lis.append(w)
# print(lis)

# #nimero 10
# fg = input(" Antre yon chen karakte: ")
# vb = fg.replace(" ","")
# kt = len(vb)
# print(vb,kt)


# #Pati 2:

# #nimero 1
# n = 1000
# lis_d = [ ]
# for i in range (n+1):
#     if i%2==0:
#         lis_d.append(i)
# print(lis_d)

# #nimero 2

# lis_a = [ ]
# n = int(input("konyen eleman wap antre: "))
# for i in range(n):
#     el = input(f"Antre eleman {i+1}: ")
#     lis_a.append(el)
#     lis_c = [str(eleman) for eleman in lis_a]
#     print(lis_c)

# #nimero 3
# lis_ch = [ ]
# d = input("Antre yon ansanm chen karakte: ")
# w=d.upper()
# s= w.split()
# for f in s:
#     lis_ch.append(f)
# print(lis_ch)

# #nimero 4
# lis_antye = [ ]
# nouvo_lis = [ ]
# q = int(input("Konbyen eleman wap antre nan lis la: "))
# for h in range(q):
#     tu = input(f"Antre eleman {h+1}: ")
#     lis_antye.append(tu)
    
# for a, div in enumerate(lis_antye):
#     if a % 3 == 0:
#         nouvo_lis.append(div)
# print(nouvo_lis)

# # #nimero 5
# lis_c = [1,2,3,4,5,6,7,8,9]

# nou_l = [tuple(lis_c[i:i+3]) for i in range(0, len(lis_c), 3)]
# print(nou_l)

# #nimero 6
# lis_doublon = [1,2,2,3,4,5,4,7,5,7,9,3,0]
# list_san_doublon = list(set(lis_doublon))
# print(f"Lis avek doublon: {lis_doublon}")
# print("\n")
# print(f"Lis san doublon: {list_san_doublon}")

# #nimero 7
# lis_1 = [1,2,3,4,5,6,7,8,9]
# lis_2 = [2,67,45,4,7,12,76,3,7,5]
# nouvo_l = [el for el in lis_1 if el in lis_2 ]
# print(f"Premye lis: {lis_1}")
# print(f"Dezyem lis: {lis_2}")
# print(f"Lis komen: {nouvo_l}")

# #nimero 8
# lis_1 = [1,2,3,4,5,6,7,8,9]
# lis_2 = [2,67,45,4,7,12,76,3,7,5]
# nouvo_l =  list(set(lis_1) ^ set(lis_2))
# print(f"Premye lis: {lis_1}")
# print(f"Dezyem lis: {lis_2}")
# print(f"Lis distenk lan: {nouvo_l}")

# #nimero 9
# dik = { 'kle1' : 23, 'kle2' : 45, 'kle3' : 78, 'kle4' : 98, 'kle5' : 90}

# lis1 = list (dik.keys())
# lis2 = list (dik.values())
# print(f"diksyone a se : {dik}")
# print(f"Lis kle yo se : {lis1}")
# print(f"Lis vale yo se : {lis2}")

# #nimero 10
# lis1 = [1,2,3,2,4,5,6,4]
# lis2 = [1,8,9,56,34,3,4]
# lis3 = [90,3,76,5,1,0,89]
# nou_l = set(lis1 + lis2 + lis3)
# print(f"Premye lis la se: {lis1}")
# print(f"Dezyem lis la se: {lis2}")
# print(f"Twazyem lis la se: {lis3}")
# print(f"Lis reyini an se: {nou_l}")

# #pati 3
# #nimero 1
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}

# vale_yo = [ ]
# for cle in diksyo:
#     vale = diksyo[cle]
#     vale_yo.append(vale)
# print(f"Diksyone a se: {diksyo}")
# print(f"Vale yo se: {vale_yo}")

# #nimero 2
# chenn = input("Antre yon teks: ")

# if isinstance(chenn, str) and chenn.startswith("{") and chenn.endswith("}"):
#     print("Wi li genyen devan ak deye")
# else:
#     print("Li pa genyenl")

# #nimero 3
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# for kle in diksyo.keys():
#     print(kle)

# #nimero 4
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# for v in diksyo.values():
#         print(v)

# #nimero 5
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# diksyo_kopi = {}
# for kle , vale in diksyo.items():
#     diksyo_kopi[kle]= vale
# print(f"diksyone original la se: {diksyo}")
# print(f"diksyone kopi a se: {diksyo_kopi}")

# #nimero 6
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# for k , v in diksyo.items():
#     if isinstance(v, str):
#         diksyo[k]= f"_{v}_"
# print(diksyo)

# #nimero 7
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# n_dik = {}
# for kle, vale in diksyo.items():
#     if isinstance(vale, int):
#         n_dik[kle] = vale
# print(n_dik)

# #nimero 8
# diksyo = { 'kle1' : 'vale', 'kle2' : 45, 'kle3' : 'waww', 'kle4' : 'wendel', 'kle5' : 90}
# nou_d = []
# for kl, vl in diksyo.items():
#     nou_d.append((kl, vl))
# print(nou_d)

# #nimero 9
# tipl = [('kle1', 'vale'), ('kle2', 45), ('kle3', 'waww'), ('kle4', 'wendel'), ('kle5', 90)]
# dik = {}
# for kle, vale in tipl:
#     dik[kle] = vale
# print(dik)

# # nimero 10
dick_1 = {'kle1':'rele','kle2':23,'kle3':'koi','kle4':34,'kle5':'waw'}
dick_2 = {'kle1':'poukoi','kle2':45,'kle9':'atansyon','kle8':67,'kle5':'dako'}
dick_3 = {}
for el in dick_1:
    if el in dick_2:
        dick_3[el]=dick_1[el]+dick_2[el]
    else:
        dick_3[el] = dick_1[el]
for el in dick_2:
    if el not in dick_3:
        dick_3[el] =dick_2[el]
print(dick_3)

# #Pati 4

# #nimero 1

# def enves(mo):
#     return print(mo[::-1])
# d = input("Antre yon mo: ")
# enves(d)

# #nimero 2
# def code():
#     al = string.ascii_lowercase
#     c = " "
#     w = int(input("Antre kantite let kod la ap gnyen: "))
#     while w <1:
#         input("li pa sipoze pi piti ke 1")
#     j = 0
#     while j < w:
#         c += al[random.randint(0,25)]
#         j+=1
#     print(c)

# code()

#nimero 3
# def code_san_repetisyon():
#     al = string.ascii_lowercase
#     c = ""
#     w = int(input("Antre kantite let kod la ap gnyen: "))
#     while w <1 or w>26:
#         w = int(input("li pa sipoze pi piti ke 1, ni depase 26: "))
#     j=0  
#     while j < w:
#         d_c = al[random.randint(0,25)]
#         if d_c not in c:
#             c+=d_c
#             j+=1
#     print(c)

# code_san_repetisyon()

# #nimero 4
# def alnimerik():
#     al = string.ascii_lowercase+string.digits
#     c = ""
#     w = int(input("Antre kantite let kod la ap gnyen: "))
#     while w <1 or w>36:
#         w = int(input("li pa sipoze pi piti ke 1, ni depase 26: "))
#     j=0  
#     while j < w:
#         d_c = al[random.randint(0,35)]
#         if d_c not in c:
#             c+=d_c
#             j+=1
#     print(c)

# alnimerik()

#nimero 5



# #nimero
# def vigil():
#     m=input("Antre mo a: ")
#     new=""
#     for el in m:
#         new+=f"{el},"
#     print(new)

# vigil()

#nimero 7






            



    
















