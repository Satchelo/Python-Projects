"""
Project Owner: Onur YAŞAR
Start Date: 22/06/2022 17:40
Last Modified Date: 22/06/2022 00:30
"""

# print("MERHABA \nONUR YAŞAR")
# print("merhaba benim adım \tONUR")  
# print("merhaba benim adım {ad}, yaşım {yas}  ".format(ad="ONUR REİS", yas= 23))
# onur_yasar=5
# print(onur_yasar)
# print(3+9) 
# print(8%3)
# print(type(15))
# strvar="python"     
# print(strvar)
# print(strvar[2:5:2])
# a="onuryasar1907"
# print(a)
# print(a[0:5])
# print(len(a))
# print(len(strvar))
# print(strvar+" öğren!")
# strvar= strvar+ " oğren!"
# print(strvar.upper())
# print(strvar.lower())
# print(strvar.split("o"))
# print(strvar.split("o", 1))
# print("onur".center(5))
# print(strvar.upper())
# print(strvar.isupper())
# print(strvar.join([" 123", "onur", "ali"]))
# print(a.isdigit())
# recep= "ALİ"
# print(recep.isdigit())
# print(recep.isupper())

# onurreis = [4,2,3,1,7,6,5]
# onurreis.append("onur") # Add data to list
# print(onurreis)
# onurreis.append("onur") # Add data to list
# print(onurreis)


# onurreis.insert(3, "reco") # Add data to specific index
# print(onurreis)

# onurreis.remove("onur") # Remove data from list
# print(onurreis)
# onurreis.append(10)
# print(onurreis)
# onurreis.pop() # Remove last element
# print(onurreis)

# onurreis.remove("onur") # Remove data from list
# print(onurreis)
# onurreis.remove("reco") # Remove data from list
# print(onurreis)
# onurreis.sort() #Sort the list
# print(onurreis)

# onurreis.sort(reverse=True) #Sort the list
# print(onurreis)

# gdgfgdfdg = "Onur"
# print(gdgfgdfdg)


# b= "Onur was a good man but he had a problem. he was trusting to everyone. If I could go back in time. I could say: Onur fuck your life"
# print(b.upper())
# b= b.upper()
# print(b.isupper())

# print("ONUR IS A JUNIOR PYTHON DEVELOPER")

"""23/06/2022"""
# a = True
# print(type(a))
# yas1 = 18
# yas2 = 20
# print(yas1 == 18)
# print(yas1 != 18)
# print(not yas2 > 18)

# list1 = ['a','b', 'c', 'd', 'e']
# list1.append('onur')
# print(list1)
# print(list1 + ['yasar'])
# print(list1.append('fb'))
# print(list1 + ['3'])
# list1.pop(0)
# print(list1)
# list1 [0] = "123"
# print(list1)    
# list1index = list1.index('e')
# print(list1index)    

# tup = ('a','b', 'c', 'd', 'e', 'a')  #valu of tube is a constant digit
# tupcount = tup.count('a')  
# print(tupcount)

# dict1 = {
#     'name' : 'onur',
#     'age' : 23,
#     'city' : 'istanbul'
# }
# print(dict1)

# dict2 = {
#     'name' : 'onur',
#     'age' : 23,
#     'city' : {
#         'born_city' : 'istanbul',
#         'live_city' : 'aydın'
#     }
# }
# print(dict2)
# print(dict2['city'])
# print(dict2['city']['live_city'])
# ct = dict2.get('city').get('live_city')
# print(ct)
# ky = dict1.keys()
# print(ky)
# vl = dict1.values()
# print(vl)
# it = dict1.items()
# print(it)
""" QUIZ 1 """

# print(5*4)
# print(5%4)
# print(type(2.3 + 4.7))

# st = 'yakın kampüs'
# print(st[10])
# print(st.index('ü'))
# print(st.upper().lower())
# print(st.split('a', 1))

# a = True
# b = False
# c ='true'
# print(a != b)

# lt = [1, 'a', 2, 3, True, 4, 5, 'true', '1']
# print(lt[-1])
# lt.reverse()
# print(lt)

""" IF SORGULARI """

# hava_durumu = 'yagışlı'
# if hava_durumu == 'yagışlı' :
#     print('şemsiyeni al!')
# elif hava_durumu == 'karlı':
#     print('Atkını al!')
# else: 
#     print('Sorun yok')


# yas = 15
# if yas > 18:
#     print('HOŞGELDİNİZ')
# else:
#     print('SEN BURAYA GİREMEZSİN')

# lt = ['a', 'b', 'c']
# hedef_harf = 'd'
# if hedef_harf in lt:
#     print('buldum')
# else:
#     lt.append(hedef_harf)
#     print('GÜNCEL LİSTE {}'.format(lt))

# hedef_harf = 'a'

# if (hedef_harf in lt) and (hedef_harf == lt[0]):
#     print('buldum ve ilk eleman konumunda')
# elif hedef_harf in lt:
#         print('buldum ama ilk eleman konumunda değil')
# else:
#     lt.append(hedef_harf)
#     print('GÜNCEL LİSTE {}'.format(lt))

""" 4/07/2022  FOR LOOP """

yorum_bırakanlar = ["Onur Yaşar", "Emre Uluışık", "Emre Savaş", "Eray Bayrak"]
# for kullanıcı in yorum_bırakanlar:
#     print (kullanıcı)

# kullanıcı_sayısı = 0
# for kullanıcı in yorum_bırakanlar:
#     kullanıcı_sayısı = kullanıcı_sayısı + 1
#     print(kullanıcı_sayısı, kullanıcı)

# ad, soyad = yorum_bırakanlar[0].split()[0], yorum_bırakanlar[0].split()[1]
# print(ad)
# print(soyad)

# kullanıcı_sayısı = 0
# for kullanıcı in yorum_bırakanlar:
#     kullanıcı_sayısı = kullanıcı_sayısı + 1
#     ad, soyad = kullanıcı.split()[0], kullanıcı.split()[1]
#     print('{0}. kullanıcının adı {1} ve soyadı {2}'.format(kullanıcı_sayısı, ad, soyad))

# moderator = "Emre Savaş"
# moderator_sayısı = 0
# kullanıcı_sayısı = 0
# for kullanıcı in yorum_bırakanlar:
#     ad, soyad = kullanıcı.split()[0], kullanıcı.split()[1]
#     if kullanıcı == moderator :
#         moderator_sayısı += 1
#         print('{0}. moderatorün adı {1} ve soyadı {2}'.format(moderator_sayısı, ad, soyad))
#     else:
#         kullanıcı_sayısı += 1
#         print('{0}. kullanıcının adı {1} ve soyadı {2}'.format(kullanıcı_sayısı, ad, soyad))

# kl1 = {
#     'name' : 'onur',
#     'age' : 23,
#     'city' : 'istanbul'
# }
# a = kl1.items()
# print(a)
# for k, v in a :
#     print('key: {} \t value: {}'.format(k, v))

# sayı = 6
# sonuç = 1
# while sayı > 0:
#     sonuç = sayı * sonuç
#     sayı -= 1
# print(sonuç)

# """ 05/07/2022 """

# print(range(10))
# print(list(range(6,10,2)))
# print([*range(10)])

# harfler = ['a', 'b', 'c']
# for index, harf in enumerate(harfler):
#     print('{}. harf = {}'.format(index+1, harf))

# for  harf in enumerate(harfler):
#     print(harf)

# ülkeler = ['tr', 'fr', 'de']
# sıralama = range(1,4)
# for ülke in zip(ülkeler, sıralama):
#     print(ülke)

# harfler1 = ['a', 'b', 'c', 'd', 'e']*10
# for index, harf in enumerate(harfler1):
#     if harf == 'c':
#      print('{} harfi {}. indexte!'.format(harf, index))
#      break

# for sayı in range(1,12):
#     if sayı%2 == 0 :
#         continue
#     print(sayı)

# for sayı in range(1,12):
#     if sayı%2 != 0 :
#         pass
#     else:
#         print(sayı)

# """ QUIZ 2 """

# kullanıcı1 = {
#     'ad' : 'Ferhat',
#     'soyad' : 'Ibrik',
#     'uzmanlık' : ['Front-end'] 
# }
# kullanıcı2 = {
#         'ad' : 'Gökçe',
#         'soyad' : 'Gün',
#         'uzmanlık' : ['Tasarım'] 
# }
# kullanıcı3 = {

#     'ad' : 'Mesut',
#     'soyad' : 'Gün',
#     'uzmanlık' : ['Front-end'] 
# }
# print(kullanıcı1['uzmanlık'])
# print(kullanıcı1.get('uzmanlık'))

# kullanıcı_listesi = [kullanıcı1, kullanıcı2, kullanıcı3]
# for kullanıcı  in kullanıcı_listesi:
#     if kullanıcı.get('uzmanlık') == ['Front-end']:
#         print(kullanıcı.get('ad'))
# for kullanıcı  in kullanıcı_listesi:
#     if 'Front-end' in kullanıcı.get('uzmanlık'):
#         print(kullanıcı.get('ad'))
    
# kullanıcı3['uzmanlık'].append('yazılım')
# print(kullanıcı_listesi)

# kullanıcı_yasları = [22, 32, 34]
# for kullanıcı, yas in zip(kullanıcı_listesi, kullanıcı_yasları):
#     if yas<30:
#         print(kullanıcı)

# değer = 7
# x = değer-1
# while x>1:
#     if değer%x == 0:
#         print('{} değeri asal sayı değil!'.format(değer))
#     else:
#         x-=1
# else:
#     print('{} değeri asaldır'.format(değer)) 

# """ FUNCTIONS """

# def buyuk_sayıyı_dondur(a, b):
#     if a>b:
#         return a
#     elif b>a:
#         return b

# print(buyuk_sayıyı_dondur(7, 4))
# print(buyuk_sayıyı_dondur(3, 1))

# def metin_yazdır (a, b):
#     buyuk_sayı = buyuk_sayıyı_dondur(a, b)
#     şablon_metin = '{} daha büyük sayıdır.'.format(buyuk_sayı)
#     print(şablon_metin)
# print(metin_yazdır(5, 10))

# def isim_soyisim_ayırma (isim_soyisim):
#     isim = isim_soyisim.split()[0]
#     soyisim = isim_soyisim.split()[1]
#     return isim, soyisim

# print(isim_soyisim_ayırma('Onur Yaşar'))
# c,d = isim_soyisim_ayırma('Onur Yaşar')
# print(c)

# def isim_soyisim_birleştirme (*args):
#     for item in args:
#         print(item)
#     return ' '.join(args)
# print(isim_soyisim_birleştirme('MUSTAFA', 'KEMAL', 'ATATÜRK'))

# def gobek_adı_yazdır (**kwargs):
#     if 'gobekadı' in kwargs:
#         print(kwargs ['gobekadı'])
#     else :
#         print('gobek adı yok')

# gobek_adı_yazdır(adı='Onur', gobekadı ='Okan', soyadı = 'Yaşar')

""" 06/07/2022"""
# def karesini_al (x):
#     return x**2
# sayılar = [*range(1,6)]
# print(sayılar)
# print([*map(karesini_al, sayılar)])

# def çift_sayıları_filtrele (x):
#     if x%2 == 0:
#         return x
# print([*filter(çift_sayıları_filtrele, sayılar)])

# print([*map(lambda x : x**2, sayılar)])
# print([*filter(lambda x : x if x%2 == 0 else None, sayılar)])

# print(input('bir_sayı_girin'))
# girdi = input('bir_sayı_girin')
# print(type(int(girdi)))

# def uygulama ():
#     girdi = input('bir_sayı_girin:')
#     islem = input('çift_mi_tek_mi_sorgula:')
#     if islem == 'çift' :
#         if int(girdi)%2 ==0 :
#             return'{} sayısı bir çift sayıdır.'.format(girdi)
#         else:
#             return'{} sayısı bir çift sayı değildir!.'.format(girdi)
#     elif islem == 'tek' :
#         if int(girdi)%2 == 1:
#             return'{} sayısı bir tek sayıdır.'.format(girdi)
#         else:
#             return'{} sayısı bir tek sayı değildir!.'.format(girdi)
#     else:
#         return 'onur İŞLEM kısmına bir şey YAZMADIN!!'
    
# print(uygulama())
""" HESAP MAKİNESİ UYGULAMASI """

# def hesap_makinesi():
#     a = int(input('birinci_sayı: '))
#     b = int(input('ikinci_sayı: '))
#     işlem = input('toplama(+), çıkarma(-), çarpma(*), bölme(/) giriniz: ')
#     if işlem == '+':
#         sonuç = a+b 
#         return sonuç
#     elif işlem == '-':
#         sonuç = a-b
#         return sonuç
#     elif işlem == '*':
#         sonuç = a*b
#         return sonuç
#     elif işlem == '/':
#         sonuç = a/b
#         return sonuç
#     else:
#         return 'HATALISINIZ!!'
    

# print(hesap_makinesi())

# def eposta_kontrol ():
#     girdi = input('geçerli bir eposta giriniz.. : ')
#     while not (('@'in girdi) and ('.'in girdi)):
#         print('Lütfen geçerli bir eposta girin!')
#         girdi = input('geçerli bir eposta giriniz.. : ')
#         print ('TEBRİKLER, geçerli bir eposta girdiniz.')

# eposta_kontrol()
# def mail_kontrol():
#     while True:
#         girdi = input('geçerli bir eposta girin : ')
#         if ('@'in girdi and '.' in girdi):
#              print('TEBRİKLER, geçerli adres girdiniz!!'),
#              break
#         else:
#             print('yanlış girdiniz!!')
#             pass
        
# mail_kontrol()




""" 07/07/2022 """
# def tamsayıya_cevir():
#     while True:
#          girdi = input('ondalık sayı giriniz: ')
#          status = ''
#          try:
#              girdi = float(girdi)
#              print('yuvarlama işleminin sonucu: {}'.format(round(girdi)))
#              status = 'başarılı'
#              break
#          except:
#              print('{} girdisi ondalık tipe çevrilemiyor.'.format(girdi))
#              status = 'başarısız'
#              pass
#          finally:
#             print(' tam sayıya çevirme işlemi {} olarak tanımlandı.'.format(status))
# tamsayıya_cevir()

# vatandaş = {
#     'ad' : 'onur',
#     'tcno' : 425508
# }

# try:
#     print(vatandaş['afd'])
# except IndexError:
#     print('indexlemeye çalıştığınız eleman listenin dışında')
# except KeyError:
#     print('verilen anahtara karşı değer bulunmuyor.')
# except:
#     print('KOD DÜZGÜN ÇALIŞMIYOR.')

""" QUİZ 3 """

# def üstel_sayı (a,b):
    # return a**b
# print(üstel_sayı(3, 2))

#     sonuç = 1
#     if b < 1:
#         return sonuç
#     for kuvvet in range(1, b+1):
#         sonuç = sonuç * a
#     return sonuç
# print(üstel_sayı(4, 1))

# listem = [1, 2, 3,5,6, 4]
# def listedki_enbüyük_2sayı(listem):
#     print(listem.sort)
#     return listem[-1], listem[-2]
# deneme = [1, 2, 3,5,6, 4]

# print(listedki_enbüyük_2sayı(deneme))

# liste = [1,2,3,'d','DS']
# sonuç = []
# def str_filtrele(liste):
# #     for x in liste:
# #         if type(x) == str:
# #             print(sonuç.append(x))
# #         else:
# #             pass
# #     return sonuç
# # liste = [1,2,3,'d','DS']
# # print(str_filtrele(liste))
#     return[*filter(lambda x: x if type (x) == str else None , liste)] 
# print(str_filtrele(liste))

# def paradan_Altı_sıfır_AT  (liste):
#     return[*map(lambda x: int(x/10**6) , liste)]
# print(paradan_Altı_sıfır_AT([2000000,230000000,5600000000]))

# def saat_kaç():
#     saat = input('saat giriniz : ')
#     if saat.isdigit():
#         saat = int(saat)
#         if ((saat >= 0) and (saat < 24)):
#             dakika = input('dakika giriniz : ')
#             if dakika.isdigit():
#                 dakika=int(dakika)
#                 if (dakika >= 0 and dakika < 60):
#                     return 'girilan saat {}:{}'.format(saat, dakika)
#                 else:
#                     return 'girilen dakika aralığı yanlış'
#             else:
#                 return 'dakika tam sayı tipinde değil'
#         else:
#             return 'girilen saat aralığı yanlış'
#     else:
#          return 'saat tam sayı tipinde değil'                      #try
                                                     #except whle true
                                                     #finally


# print(saat_kaç())

# def saat_verisi_Al():
#     while True:
#         saat = input('lütfen saat giriniz: ')
#         dakika = input('lütfen dakika giriniz : ')
#         try:
#            saat = int(saat)
#            dakika = int(dakika)
#            if (saat>=0 and saat<24) and (dakika>=0 and dakika<60):
#                 print('Saat şu anda {}:{}'.format(saat, dakika))
#                 break
#            else:
#                 print('Saat veya dakikayı yanlış aralıkta girdiniz!!')
#                 pass
#         except:
#             print('Geçersiz saat verisi girdiniz!!')

# saat_verisi_Al()

