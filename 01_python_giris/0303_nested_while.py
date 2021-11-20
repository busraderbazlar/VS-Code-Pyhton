#region nested_if
# iç içe döngü - iç içe loop
#matrix 7x5[satır, sütün]
#endregion

i,j=0,0 #i dışardaki döngü j içerdeki döngü

while i<10:
    while j<10:
        j+=1
        print(i,"",j)
    i+=1
    j=0
    print() 
#print alt satırın başlangıcı