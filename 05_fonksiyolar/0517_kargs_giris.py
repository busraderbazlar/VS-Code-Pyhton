# region kargs_giris
"""
Argüman olarak → int, float, string, list gönderebiliyorum, peki
Argüman olarak → dictionary gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek_1

def pDilleri(**kargs):
    print(type(kargs))
    for key, value in kargs.items():
        print(f"{key} {value}")



pDilleri(
    programlamaDili="python",
    seviye="yüksek",
    interpreter=True,
    veryison=3.64
)



def pDilleri(kargs):
        print(f"{kargs['programlamaDili']} \t\t{kargs['seviyesi']} \t\t {kargs['interpreter']} \t\t {kargs['version']}")

dilPython = {
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpreter" : True,
    "versiyon" : 3.64
}
dilCSharp = {
    "programlamaDili" : "c#",
    "seviye" : "yüksek",
    "interpreter": False,
    "versiyon" : 8.0
}

print("Prg.Dil\tSeviye\tInterp\tVersiyon")
print("-------\t-------\t-------\t-------")
pDilleri(dilPython)
pDilleri(dilCSharp)
