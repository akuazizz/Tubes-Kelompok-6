# daftar menu dan harga
menu = [
    ["Nasi Goreng", 15000],
    ["Mie Goreng", 12000],
    ["Ayam Goreng", 18000],
    ["Gado-Gado", 10000],
    ["Soto Ayam", 15000],
    ["Es Teh", 3000],
    ["Lemon Tea", 5000],
    ["Es Jeruk", 5000],
    ["Jus Alpukat", 7000],
    ["Jus Mangga", 7000],
]


def display_menu(menu):
    print("\nDaftar Menu Makanan:")
    for i in range(len(menu)):
        item = menu[i][0]
        price = menu[i][1]
        print(f"{i+1}. {item} - Rp {price}")
    panggil(menu)


# urutan menu termurah bubble_sort
def urutascending(menu):
    n = len(menu)

    for i in range(n):
        for j in range(n - 1 - i):
            if menu[j][1] > menu[j + 1][1]:
                menu[j], menu[j + 1] = menu[j + 1], menu[j]
    return menu


# urutan menu termahal bubble_sort
def urutdescending(menu):
    n = len(menu)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if menu[j][1] < menu[j + 1][1]:
                menu[j], menu[j + 1] = menu[j + 1], menu[j]
    return menu


# menu yang akan dipesan
def pilih_menu(menu):
    pesanan = []
    selesai = False

    while not selesai:
        print("\nMenu Makanan:")
        for i in range(len(menu)):
            item = menu[i][0]
            price = menu[i][1]
            print(f"{i+1}. {item} - Rp {price}")
        print("0. Selesai")

        pilihan = input("Masukkan nomor menu yang akan dipesan (0 untuk selesai): ")

        if pilihan == "0":
            selesai = True
        elif pilihan.isdigit() and int(pilihan) in range(1, len(menu) + 1):
            menu_index = int(pilihan) - 1
            pesanan.append(menu[menu_index])
            print("Menu telah ditambahkan ke dalam pesanan.")
        else:
            print("Menu tidak valid. Silakan pilih nomor menu yang tersedia.")

    if pesanan:
        print("\nPesanan Anda:")
        total_harga = 0
        for i, item in enumerate(pesanan, start=1):
            name = item[0]
            price = item[1]
            total_harga += price
            print(f"{i}. {name} - Rp {price}")
        print(f"Total Harga: Rp {total_harga}")
    else:
        print("Pesanan Anda kosong.")
    panggil(menu)
    
    
# daftar panggil program
def panggil(menu):
    print("\n<=========Menu Order Makanan=========>")
    print("1. Lihat daftar Menu dan harga")
    print("2. Urutkan menu dari harga termurah")
    print("3. Urutkan menu dari harga termahal")
    print("4. Pilih menu yang akan dipesan")
    print("5. Keluar Program")

    pilih = int(input("Pilih: "))
    if pilih == 1:
        display_menu(menu)
    elif pilih == 2:
        sorted_menu = urutascending(menu)
        print("\nUrutan Menu Makanan dari Harga Termurah :")
        for item in sorted_menu:
            print(item[0], "-", "Rp", item[1])
        panggil(menu)
    elif pilih == 3:
        sorted_menu = urutdescending(menu)
        print("\nUrutan Menu Makanan dari Harga Termahal :")
        for item in sorted_menu:
            print(item[0], "-", "Rp", item[1])
        panggil(menu)
    elif pilih == 4:
        pilih_menu(menu)
    elif pilih == 5:
        print("Terima kasih telah memesan makanan")
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
        panggil(menu)


panggil(menu)