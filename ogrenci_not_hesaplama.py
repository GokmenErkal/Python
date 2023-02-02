ogr_not = []
Ortalama = []
harf_notu = 0


class Ogrenci:
    
    def __init__(self, ogr_isim):
        
        self.ogr_isim = ogr_isim
        
    def notlari_gir(self,vize1,vize2,final):
    
        self.vize1 = vize1
        self.vize2 = vize2
        self.final = final
        
        self.ogr_not = [self.vize1, self.vize2, self.final]
        
        return self.ogr_not
    
    def ortalama_hesapla(self):
        
        vize_1 = self.ogr_not[0]*25/100
        vize_2 = self.ogr_not[1]*35/100
        final_ = self.ogr_not[2]*40/100
        
        self.ortalama = vize_1 + vize_2 + final_
        
        Ortalama.append(self.ortalama)
            
        return self.ortalama
            
    def harf_notunu_hesapla(self):
        
        if self.ortalama <= 100 and self.ortalama >= 90:
            
            self.harf_notu = "AA" 
            
        elif self.ortalama <= 89 and self.ortalama >= 85:
            
            self.harf_notu = "BA"
            
        elif self.ortalama <= 84 and self.ortalama >=80:
            
            self.harf_notu = "BB"
            
        elif self.ortalama <= 79 and self.ortalama >= 75:
            
            self.harf_notu = "CB"            
        
        elif self.ortalama <= 74 and self.ortalama >= 65:
            
            self.harf_notu = "CC"
            
        elif self.ortalama <= 64 and self.ortalama >= 60:
            
            self.harf_notu = "DC"
            
        elif self.ortalama <= 59 and self.ortalama >= 55:
            
            self.harf_notu = "DD"
        
        elif self.ortalama <= 54 and self.ortalama >= 50:
            
            self.harf_notu = "FD"
            
        elif self.ortalama <= 49 and self.ortalama >= 0:
            
            self.harf_notu = "FF"
    
    def ogrenci_notlarini_yazdir(self):
        
        print(f"{ogrenci.ogr_isim} adlı öğrencinin : Vize 1 : {ogrenci.ogr_not[0]}, Vize 2 : {ogrenci.ogr_not[1]}, Final : {ogrenci.ogr_not[2]}, Ortalama : {ogrenci.ortalama}, Harf notu : {ogrenci.harf_notu}")
        
        
ogr_sayi = int(input("Öğrenci sayısını belirleyiniz : "))

for i in range(ogr_sayi):
    
    
    
    isim = input("Öğrenci ismini giriniz : ")
    
    ogrenci = Ogrenci(isim)
    
    vize1 = float(input("Vize 1 notunu giriniz : "))
    vize2 = float(input("Vize 2 notunu giriniz : "))
    final = float(input("Final noutunu giriniz : "))
    print()
    
    ogrenci.notlari_gir(vize1,vize2,final)
    ogrenci.ortalama_hesapla()
    ogrenci.harf_notunu_hesapla()
    
    print(ogrenci.ogrenci_notlarini_yazdir())
    
def sinif_ortalamasini_hesapla_ve_yazdir():
    
    for i in Ortalama:
        
        toplam = 0
        
        toplam += i
        
        ort = toplam / len(Ortalama)
    
    print("Sınıf ortalaması : " + ort)
    
sinif_ortalamasini_hesapla_ve_yazdir()