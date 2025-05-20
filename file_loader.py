# -*- coding: utf-8 -*-
"""
Bu modül, Türkiye'deki mahalle bilgilerini içeren bir dosyadan veri okur
ve kullanıcının istediği il veya ilçedeki mahalleleri listeler.
"""
import re

def load_neighborhood_data(file_path):
    """
    Belirtilen dosyadaki mahalle verilerini okur ve bir liste olarak döndürür.

    Args:
        file_path (str): Mahalle verilerini içeren dosyanın yolu.

    Returns:
        list: Sözlükler içeren bir liste. Her sözlük bir mahalleyi temsil eder
              ve 'il', 'ilce', 'mahalle' anahtarlarını içerir.
              Dosya okuma hatası oluşursa None döndürür.
    """
    neighborhoods_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or '->' not in line:
                    continue

                parts = [part.strip() for part in re.split(r'->', line)]
                if len(parts) < 2 or len(parts) > 3:
                    print(f"UYARI: Beklenmeyen format: {line}")
                    continue

                mahalle_il_bilgisi = parts[0]
                konum_bilgisi = parts[-1]

                kelimeler = mahalle_il_bilgisi.split()
                if not kelimeler:
                    print(f"UYARI: İl/Mahalle bilgisi boş: {mahalle_il_bilgisi}")
                    continue

                il_ham = kelimeler[-1]
                mahalle_ham = " ".join(kelimeler[:-1])

                il = il_ham.replace('İ', 'i').replace('Ü', 'ü').replace('I', 'ı').lower()
                mahalle = mahalle_ham.replace('İ', 'i').replace('Ü', 'ü').replace('I', 'ı').lower()
                ilce = ""
                belde = ""

                if len(parts) == 3:
                    ilce_ham = parts[1]
                    belde_ham = parts[2]
                    ilce = ilce_ham.replace('İ', 'i').replace('Ü', 'ü').replace('I', 'ı').lower()
                    belde = belde_ham.replace('İ', 'i').replace('Ü', 'ü').replace('I', 'ı').lower().replace('-district center', '').replace('-province center', '').strip()
                elif "-DISTRICT CENTER" in konum_bilgisi.lower():
                    ilce = il
                    belde = il
                elif "-PROVINCE CENTER" in konum_bilgisi.lower():
                    ilce = il
                    belde = il
                else:
                    ilce_ham = konum_bilgisi.split()[0]
                    ilce = ilce_ham.replace('İ', 'i').replace('Ü', 'ü').replace('I', 'ı').lower()
                    belde = ilce


                neighborhoods_data.append({
                    'il': il,
                    'ilce': ilce,
                    'mahalle': mahalle,
                    'belde': belde
                })

        return neighborhoods_data
    except FileNotFoundError:
        print(f"Hata: '{file_path}' dosyası bulunamadı.")
        return None
    except Exception as e:
        print(f"Hata: Dosya okunurken bir sorun oluştu: {e}")
        return None
    

#test için ilk 5 satırı al: 
def test_load_neighborhood_data():
    file_path = 'neighborhoods.txt'
    neighborhoods_data = load_neighborhood_data(file_path)
    if neighborhoods_data:
        for i in range(min(5, len(neighborhoods_data))):
            print(neighborhoods_data[i])
    else:
        print("Veri yüklenemedi.")
if __name__ == "__main__":
    test_load_neighborhood_data()
# Bu kod, belirtilen dosyadan mahalle verilerini yükler ve ilk 5 satırı yazdırır.