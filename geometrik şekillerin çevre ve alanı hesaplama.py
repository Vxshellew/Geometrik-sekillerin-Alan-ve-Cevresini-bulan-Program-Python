
istek= input("Alanı ve çevresini hesaplamak istediğiniz şeklin numarasını giriniz.:\n 1.Daire\n 2.Dikdörtgen\n 3.Kare\n 4.Üçgen \n Sayı Gir:")
#Daire Çevresi ve Alanı
if istek=="1":
    r=int(input("Yarı Çapı Girin: "))
    cevre=2*3.14*r                        
    alan=3.14*r*r                         
    print("Çevre: ",cevre)
    print("Alan: ",alan)
#Dikdörtgen çevresi ve alanı
elif istek=="2":
    yukseklik = int(input("Kısa Kenarı Girin :"))
    genislik = int(input("Uzun Kenarı Girin :"))

    dkdortgenalan = yukseklik*genislik
    dkdortgencevre = 2*(yukseklik+genislik)                       
 
    print('dikdörtgen cevresi:{0}'.format(dkdortgencevre))
    print('dikdörtgen alanı:{0}'.format(dkdortgenalan))
#Kare çevresi ve alanı
elif istek=="3":
    x = int(input("Karenin bir kenarını giriniz...:"))
    print("Karenin Çevresi....:",x+x+x+x)                    
    print("Karenin Alanı....:", x**2)

#Üçgen çevresi ve alanı
elif istek=="4":
    print("""
    (1) Eşkenar Üçgen
    (2) İkizkenar Üçgen
    (3) Çeşitkenar Üçgen
    """)
    istek2 = int(input('Seçmek istediğiniz Üçgen hangisidir? : '))
    if istek2==1:
        from math import sqrt
        k1 = int(input('Eşkenar Üçgenin kenarını giriniz: '))
        alan = (k1**2 * sqrt(3))/4
        cevre = k1 + k1 + k1
        print('Eşkenar Üçgenin Alanı: ', alan)
        print('Eşkenar Üçgenin Çevresi: ',cevre)
    elif istek2==2:
        ikü1 = int(input('İkizkenar Üçgenin Eşit Olan Kenarlarının uzunluğunu giriniz: '))
        k2 = int(input('İkizkenar Üçgenin Eşit Olmayan kenarının uzunluğunu giriniz:'))
        h = (ikü1**2) - (k2/2)**2 
        x = h**0.5
        ikü_alan = (k2*x)/2
        ikü_cevre = k2 + ikü1 + ikü1
        print('İkizkenar Üçgenin Alanı: ',ikü_alan)
        print('İkizkenar Üçgenin Çevresi: ',ikü_cevre)
    elif istek2==3:
        k4 = int(input('Çeşitkenar Üçgenin birinci kenarının uzunluğunu giriniz: '))
        k5 = int(input('Çeşitkenar Üçgenin ikinci kenarının uzunluğunu giriniz: '))
        k6 = int(input('Çeşitkenar Üçgenin üçüncü kenarının uzunluğunu giriniz: '))
        u = (k4+k5+k6)/2
        cesü_alan = (u * ((u-k4) * (u-k5) * (u-k6)))**0.5
        cesü_cevre = (k4+k5+k6)
        print('Çeşitkenar Üçgenin Alanı: %0.2f' %cesü_alan)
        print('Çeşitkenar Üçgenin Çevresi: ',cesü_cevre)
        if k4 == k5 == k6:
            print('Girdiğiniz Değerler sonucu bu üçgen Eşkenear Üçgen olmuştur.')
        elif k4 == k5 or k4 == k6 or k5 == k6:
            print('girdiğiniz değerler sonucu bu üçgen ikizkenar bir üçgen olmuştur.')
            
else:

    print("Lütfen geçerli bir sayı giriniz!")
    
        
        
    