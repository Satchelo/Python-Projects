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
