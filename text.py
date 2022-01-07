"""###############################################################
# Bu program:
# - Inline iç-içe for ile [[1, 2, 3], [4, 'X', 6], [7, 8, 9]] çok boyutlu liste oluşturur
# - Randrange fonksiyonu için random modülü ekler
# - For döngüsü ile board'u ekrana basar
# - Digit olarak seçilen karelerin (1, 2, 3, 4,  6 ...) 
# - Matrise dönüştülmesini sağlar 1 → [0][0], 2 → [0][1], 3 → [0][2], 4 → [1][0], 6 → [1][2] gibi 
# - Belirli aralıkta değer girdirmeyi başarır 
# - break-continue doğru anda kullanmayı bilir
#
# Öğrenci:
# 1. Randrange fonksiyonu için kütüphaneleri import edecek.
# 2. Oyunun Başlangıcında ve Oyunun Herhangi Bir Anında Board'u Görüntüleyecek
# 3. Oyuncu Kare Seçecek → O
# 4. Seçili Olmayan Kareleri Belirleyecek
# 5. Kazananı Belirleyecek
# 6. PC Kare Seçecek → X
# 7. Main Block Tasarlayacak
###############################################################

# 1 → Randrange fonksiyonu için kütüphaneleri import edelim.
import random 

# 2 → Oyunun Başlangıcında ve Oyunun Herhangi Bir Anında Board'u Görüntüleyelim
def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


# 3 → Oyuncu Kare Seçiyor → O
def EnterMove(board):
    ok = False
    while not ok:
        move = int(input("Lütfen Kare Seçin [1-9]: "))
        ok = 1 <= move <= 9
        if not ok:
            print("[1-9] Arası Kare Seçmediniz. Lütfen Tekrar Giriniz!")
            continue
        move = move - 1 	# bu üç satır çok önemli. seçili digit değerine sahip kareyi
        row = move // 3 	# [row][col] değerine dönüştürmeliyiz. Örn
        col = move % 3		# 1 → [0][0], 2 → [0][1], 3 → [0][2], 4 → [1][0], 6 → [1][2] gibi 
        sign = board[row][col]  # seçili kareyi oku
        ok = sign not in ['O', 'X']
        if not ok:  # seçili kare dolu ise tekrar denenmeli
            print("Seçili Kare. Lütfen Tekrar Giriniz!")
            continue
    board[row][col] = 'O'   	# seçili kareyi '0' olarak set et

# 4 → Seçili Olmayan Kareleri Belirleme
def MakeListOfFreeFields(board):
    free = []  # boş liste tanımlanıyor
    for row in range(3):  # rows
        for col in range(3):  # columns
            if board[row][col] not in ['O', 'X']:  # boş kare mi?
                # evet ise append et
                free.append((row,col))
    return free

# 5 → Kazananı Belirleyelim
# 5 → Kazananı Belirleyelim
def VictoryFor(board, sgn):
    if sgn == "X":  # X için mi board'u kontrol edecek?
        who = 'me'  # PC
    elif sgn == "O":  # O için mi board'u kontrol edecek?
        who = 'you'  # Kullanıcı
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if board[0][0] and board[0][1] and board[0][2] or board[1][0] and board[1][1] and board[1][2] or board[2][0] and board[2][1] and board[2][2] == sgn:  # satırları kontrol edelim
            return who
        if board[0][0] and board[1][0] and board[2][0] or board[0][1] and board[1][1] and board[2][1] or board[0][2] and board[1][2] and board[2][2] == sgn: # sütunları kontrol edelim
            return who
        if board[0,0] and board[1,1] and board[2,2] != sgn:  # 1. köşegeni kontrol edelim
            cross1 = False
        if [0,2] and board[1,1] and board[2,0] != sgn:  # 2. köşegeni kontrol edelim
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def MakeListOfFreeFields(board):
    free = []  # boş liste tanımlanıyor
    for row in range(3):  # rows
        for col in range(3):  # columns
            if board[row][col] not in ['O', 'X']:  # boş kare mi?
                # evet ise append et
                free.append((row,col))
    return free
board = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]

def DrawMove(board):
    free = MakeListOfFreeFields(board)  # boş olan karelerden bir liste tanımlayalım
    cnt = len(free)
    if  cnt > 0:  # list boş değil ise, 'X' i set edeceğimiz kareyi random seçelim
        this = random.randrange(cnt)
        this = this-1 
        row, col = this // 3, this % 3
        print(row,col)
        board[row][col] = "X"
        print(board[row][col]) 




# 7 → main

board = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
#print(board) #[[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
board[1][1] = 'X'  # ortadaki kareyi 'X' olarak set et
#print(board) #[[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
free = MakeListOfFreeFields(board)
humanturn = True  # sıra kim de? önce oyuncu başlayacak
while len(free):
    DisplayBoard(board)
    if humanturn:
        EnterMove(board)
        victor = VictoryFor(board, 'O')
    else:
        DrawMove(board)
        victor = VictoryFor(board, 'X')
    if victor != None:
        humanturn = False
        free = MakeListOfFreeFields(board)
        continue

DisplayBoard(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")"""

sgn= "X"
board = [["X", 2, "X"], [4, "X" , 6], ["X", 8, 9]]
for rc in range(3):
    if board[0][2] == board[1][1] == board[2][0] == sgn :
        print(board[0][2] and board[1][1] and board[2][0])

"""    if board[0][0] != board[1][1] != board[2][2] != sgn:
        print(board[0][0] , board[1][1] ,board[2][2])"""

#if board[rc][0] and board[rc][1] and board[rc][2] == sgn:
#if board[rc][0] == board[rc][1] == board[rc][2] == sgn: