# capitalize()
# Kod içerisine yazılan cümlenin ya da kelimenin ilk harfini büyük yapar:
print("""küçük harfle başlayan bu cümledeki 'küçük' kelimesinin
k'si büyüdü.""".capitalize())
Küçük harfle başlayan bu cümledeki 'küçük' kelimesinin
k'si büyüdü.
# Bu metod bir değişkene de atanabilir:
isim = "gökay"
print(isim.capitalize())
Gökay
# HATIRLATMA: Değişkene atasam da değişkeni kalıcı olarak değiştirmez. Daha son-
# ra ben değişkeni yazdırmak istediğimde ilk haliyle aynen yazdırır:
print(isim)
gökay
# Ama yeni bir değişkene metodla beraber atarsak değişkeni yeni haliyle yazar:
yeni_isim = isim.capitalize()
print(yeni_isim)
Gökay
