from file_loader import load_neighborhood_data

def search_exact(data, mahalle_adi):
    found = False
    for item in data:
        if item['mahalle'] == mahalle_adi:
            print(f"{item['il'].title()} -> {item['ilce'].title()} -> {item['mahalle'].title()}")
            found = True
    if not found:
        print("Tam eşleşme bulunamadı.")

def search_partial(data, mahalle_adi):
    data=load_neighborhood_data("neighborhoods.txt")
    found = False
    for item in data:
        if mahalle_adi in item['mahalle']:
            print(f"{item['il'].title()} -> {item['ilce'].title()} -> {item['mahalle'].title()}")
            found = True
    if not found:
        print("Kısmi eşleşme bulunamadı.")

def adding_new_neighborhood():
    data = load_neighborhood_data("neighborhoods.txt")
    if data is None:
        print("Veri yüklenemedi")
        return

    def find_matches(keyword, key):
        # keyword küçük harf, key de dict'in anahtarı ('il' veya 'ilce')
        keyword = keyword.lower()
        matches = sorted(set(item[key] for item in data if keyword in item[key].lower()))
        return matches

    # İl seçimi
    while True:
        il_adi = input("Hangi ile eklemek istiyorsunuz?: ").strip()
        il_secenekler = find_matches(il_adi, 'il')
        if not il_secenekler:
            print("Böyle bir il bulunamadı, tekrar deneyin.")
            continue
        elif len(il_secenekler) == 1:
            il_adi = il_secenekler[0]
            print(f"Seçilen il: {il_adi}")
            break
        else:
            print("Birden fazla il bulundu. Lütfen seçim yapın:")
            for i, il in enumerate(il_secenekler, 1):
                print(f"{i}. {il}")
            secim = input("Seçiminiz (numara): ").strip()
            if secim.isdigit() and 1 <= int(secim) <= len(il_secenekler):
                il_adi = il_secenekler[int(secim) -1]
                break
            else:
                print("Geçersiz seçim, tekrar deneyin.")

    # İlçe seçimi
    while True:
        ilce_adi = input(f"{il_adi} ilinin hangi ilçesine eklemek istiyorsunuz?: ").strip()
        ilce_secenekler = sorted(set(item['ilce'] for item in data if item['il'] == il_adi and ilce_adi.lower() in item['ilce'].lower()))
        if not ilce_secenekler:
            print("Böyle bir ilçe bulunamadı, tekrar deneyin.")
            continue
        elif len(ilce_secenekler) == 1:
            ilce_adi = ilce_secenekler[0]
            print(f"Seçilen ilçe: {ilce_adi}")
            break
        else:
            print("Birden fazla ilçe bulundu. Lütfen seçim yapın:")
            for i, ilce in enumerate(ilce_secenekler, 1):
                print(f"{i}. {ilce}")
            secim = input("Seçiminiz (numara): ").strip()
            if secim.isdigit() and 1 <= int(secim) <= len(ilce_secenekler):
                ilce_adi = ilce_secenekler[int(secim) - 1]
                break
            else:
                print("Geçersiz seçim, tekrar deneyin.")

    # Mahalle adı
    yeni_mahalle_adi = input("Eklemek istediğiniz mahalle adını giriniz: ").strip().title()

    # Mahalle kontrolü
    mahalle_kontrol = any(item['mahalle'].lower() == yeni_mahalle_adi.lower() and item['ilce'] == ilce_adi and item['il'] == il_adi for item in data)
    if mahalle_kontrol:
        print("Zaten var olan bir mahalle girdiniz.")
        return

    # Yeni mahalleyi dosyaya ekle
    yeni_satir = f"{yeni_mahalle_adi} {il_adi} {ilce_adi}\n"
    with open("neighborhoods.txt", "a", encoding="utf-8") as file:
        file.write(yeni_satir)

    print("\nYeni mahalle eklendi!")
    print(f"\n{il_adi} - {ilce_adi} içindeki mahalleler:")
    # Data'ya yeni mahalleyi ekleyelim ki ekranda gösterelim
    data.append({'il': il_adi, 'ilce': ilce_adi, 'mahalle': yeni_mahalle_adi})
    for item in data:
        if item['il'] == il_adi and item['ilce'] == ilce_adi:
            print("-", item['mahalle'])

