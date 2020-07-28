import requests
web = 'https://www.detik.com/'

try:
    respon = requests.get(web)
    if respon.status_code == 200:
        print('Success', respon)
        print('Isi web', respon.text)
    else:
        print('ada kesalahan dalam membuka situs')
except:
    print('alamat kurang tepat')