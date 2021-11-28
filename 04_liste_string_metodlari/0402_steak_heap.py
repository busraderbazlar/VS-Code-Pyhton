# listler → referans tiptedir. o yüzden adres ile işlem yapılır.
list1 = [1, 2]
list2 = [3, 4]
list1 = list2
list2[0] = 2
print(list1) #list2 adresine git
#listler hafızanın heap bölgesinde çalışır ve listler orada saklanır.