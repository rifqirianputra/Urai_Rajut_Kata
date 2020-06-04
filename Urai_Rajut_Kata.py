# WORKING CODE!!!!


def urai(kata):
    length = len(kata) # konversi jumlah huruf jadi angka untuk perintah iterasi
    for i in range(0,length): # agar rangenya jadi (0,x) x= panjang kata yang masuk perintah
        for j in range(i+1): #for inside for loop, agar variabel i diulang, namun pada pengulangan berikutnya, variabel i + 1
            print(kata[j], end="") #end untuk join iterasi yang kepisah2
    return kata

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

def rajut (kata):
    for i in kata[::-1]:
        print(i)
        # if i == :
        #     break

#NOT WORKING CODE
#Sengaja tidak saya hapus untuk referensi just in case code yang lama lebih mendekati benar ketimbang yang baru

# kata = "Code"
# listkata = list(kata)
# list1 = []
# print(listkata)


# def urai (x):

# for i in listkata():
#     print(i)
#     lengthkata = len(kata)


# kata = "code"
# listkata = list(kata)
# list1=[]
# for i in listkata:  #BROKEN CODE.. JANGAN DIAPUS BUAT REFERENSI, JUST IN CASE
#     length = len(listkata) # konversi jumlah huruf jadi angka untuk perintah iterasi
#     list1 = listkata.append[0+length] #NOT WORKING

#nanti DEF disini
# for i in listkata:
#     length = len(listkata)
#     for i in listkata:
#         print(j, end="") ### nggak jadi.. cuma ngulang #codecodecodecode

# length = len(kata) # konversi jumlah huruf jadi angka untuk perintah iterasi
# for i in range(length):  #### udah mulai bener, tinggal ganti angka jadi huruf.. JANGAN DIHAPUS BUAT REFERENSI!!!
#     for j in range(i+1):
#         print(j)

#INI WORKING CODE, TINGGAL CONVERT JADI DEF FUNCTION
# length = len(kata) # konversi jumlah huruf jadi angka untuk perintah iterasi
# for i in range(0,length): # agar rangenya jadi (0,x) x= panjang kata yang masuk perintah
#     for j in range(i+1): #for inside for loop, agar variabel i diulang, namun pada pengulangan berikutnya, variabel i + 1
#         print(kata[j], end="")

#dibuat DEF tidak jalan.. sepertinya ada error.. namun karena waktu tinggal sedikit, saya terpaksa tidak buat dalam bentuk DEF
# def urai(kata):
#     kata = 'code'
#     length = len(kata) # konversi jumlah huruf jadi angka untuk perintah iterasi
#     for i in range(0,length): # agar rangenya jadi (0,x) x= panjang kata yang masuk perintah
#         for j in range(i+1): #for inside for loop, agar variabel i diulang, namun pada pengulangan berikutnya, variabel i + 1
#             print(kata[j], end="") #end untuk join iterasi yang kepisah2