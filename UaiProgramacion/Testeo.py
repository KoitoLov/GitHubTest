# lista_num = [2, 1, 3, 7]
# otro_contador = 0
# otros_primos = 0
# # for i in lista_num:

# #     if (lista_num.index(i) + 1) == len(lista_num):
# #         break
# #     siguiente = (lista_num[(lista_num.index(i) + 1)])
# #     string_siguiente = str(i) + str(siguiente)

# #     print(string_siguiente)

# #     numero_siguiente = int(string_siguiente)
# finished = False

# for i in lista_num:
#     for e in range(10):
#         if e != 0:
#             if (lista_num.index(i) + 1) == len(lista_num):
#                 finished = True
#                 break

#             siguiente = (lista_num[(lista_num.index(i) + 1)])
#             string_siguiente = str(i) + str(siguiente)
#             numero_siguiente = int(string_siguiente)

#             if numero_siguiente % e == 0:
#                 otro_contador += 1

#     print(otro_contador, numero_siguiente)
#     if otro_contador <= 2 and finished == False:
#         otros_primos += 1
#         otro_contador = 0
#     else:
#         otro_contador = 0
#         continue





# print("otro contador:", otro_contador)
# print("primos:", otros_primos)

lista = [1, 2, 3 ,4]
print(lista[-1])