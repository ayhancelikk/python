# Bu program toplama, çıkarma, çarpma, bölme, tam bölme, mod alma ve üs alma işlemlerini yapmaktadır.

sayi1 = 10
sayi2 = 3

# Toplama
sonuc1 = sayi1 + sayi2

# Çıkarma
sonuc2 = sayi1 - sayi2

# Çarpma
sonuc3 = sayi1 * sayi2

# Bölme
sonuc4 = sayi1 / sayi2

# Tam Bölme
sonuc5 = sayi1 // sayi2

# Mod Alma
sonuc6 = sayi1 % sayi2

# Üs Alma
sonuc7 = sayi1 ** sayi2

# Sonuçlar
print ( 'Toplama: {0} + {1} = {2}'.format ( sayi1, sayi2, sonuc1 ) )

print ( 'Çıkarma: {0} - {1} = {2}'.format ( sayi1, sayi2, sonuc2 ) )

print ( 'Çarpma: {0} * {1} = {2}'.format ( sayi1, sayi2, sonuc3 ) )

print ( 'Bölme: {0} / {1} = {2}'.format ( sayi1, sayi2, sonuc4 ) )

print ( 'Tam Bölme: {0} // {1} = {2}'.format ( sayi1, sayi2, sonuc5 ) )

print ( 'Mod alma: {0} % {1} = {2}'.format ( sayi1, sayi2, sonuc6 ) )

print ( 'Üs alma: {0} ** {1} = {2}'.format ( sayi1, sayi2, sonuc7 ) )

# Bu kısımda kullanıcıdan alınan 2 sayı, kullanıcı tarafından belirtilen aritmetik işleme tabi tutulmaktadır.

# Sayılar alınır.
sayi3 = input ( 'İlk sayıyı giriniz: ' )
sayi4 = input ( 'İkinci sayıyı giriniz: ' )

# İşlem yapılır.

sonuc8 = int ( sayi3 ) + int ( sayi4 )

# Sonuç
print ( '{0} + {1} = {2}'.format ( sayi3, sayi4, sonuc8 ) )
