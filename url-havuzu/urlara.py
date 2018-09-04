
#   URL Kontürolü yapmadan önce urlhavuzu.txt isimli
#   dosyanın güncel olduğuna dikkat ediniz.

"""
    urlara.py v0.1

    Eklenmek istenen URL adresinin havuzda var yada
    yok olduğunu anlamak icin basit bir arac. Amacı
    eş URL ekleme sorununu ortadan kaldırmak. Ekleme
    yapılacak URL havuzda mevcut degilse havuza eklenir.
"""


from sys import argv
from time import strftime

def ara(url):
    durum = str()
    with open('urlhavuz.txt','r') as dosya:
        for i in dosya.readlines():
            if i.split(',')[1] == url+'\n':
                durum = False

    if durum != False:
        with open('urlhavuz.txt','a') as dosya:
            tarih = strftime('%d/%m/%Y')+','
            dosya.write(tarih+url+'\n'); print('<url eklendi>')
    
ara(argv[1])


"""
    Kullanım sekilleri:

    >_ python urlara.py url_adresi

    >_ python /dosya/dizini/urlara.py url_adresi

    Seklinde URL adresleri kontrol edilebilir yada
    havuza URL eklenebilir.
"""
