'''
memanggil fungsi yang ada di directory lain tulis naman variable lalu
klik alt+enter -> import the name pilih file
'''
from geometry.persegi import luas_persegi, info as infopersegi
from geometry.segitiga import luas_segitiga, info as infosegitiga
# read : dari package geometry pilih modul segitiga import fungsi luas_segitiga


print(infosegitiga())
print('hitung luas segitiga',luas_segitiga(20,2))
print(infopersegi())
print('hitung luas persegi', luas_persegi(5))