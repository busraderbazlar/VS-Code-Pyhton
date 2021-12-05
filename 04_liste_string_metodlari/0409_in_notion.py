"""#asıl arama elemanları in / not in

miniMiniBirler =["buse","ender","büşra","enderr","selin","ece","ege"]
isim = "buse"
if isim in miniMiniBirler:
    print(f"{isim} liste içinde var")
    print(f"{miniMiniBirler.index(isim)}. indexli eleman")
else:
    print(f"{isim} liste içinde yok")

if not isim in miniMiniBirler:
    print(f"{isim} liste içinde yok")
    print(miniMiniBirler.index(isim))
else:
    print(f"{isim} liste içinde var")"""