# daftar menu dan harga (Ahmad Junaidi)
menu = [
    ["Nasi Goreng", 15000],
    ["Mie Goreng", 12000],
    ["Ayam Goreng", 18000],
    ["Gado-Gado", 10000],
    ["Soto Ayam", 15000]
]

def display_menu(menu):
    print("\nDaftar Menu Makanan:")
    for i in range(len(menu)):
        item = menu[i][0]
        price = menu[i][1]
        print(f"{i+1}. {item} - Rp {price}")
    panggil(menu)

# menu termurah (hanifa)
def urutascending(menu):
    print("\nUrutan Menu Makanan dari Harga Termurah :")
    sorted_menu = sorted(menu, key=lambda x: x[1])
    for i, item in enumerate(sorted_menu, start=1):
        name = item[0]
        price = item[1]
        print(f"{i}. {name} - Rp {price}")
    panggil(menu)

# menu termahal (hanifa)
def urutdescending(menu):
    print("\nUrutan Menu Makanan dari Harga Termahal :")
    sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)
    for i, item in enumerate(sorted_menu, start=1):
        name = item[0]
        price = item[1]
        print(f"{i}. {name} - Rp {price}")
    panggil(menu)

# menu yang akan dipesan (aziz)
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

        if pilihan == '0':
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

   # daftar panggil program (Ahmad Junaidi)
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
        urutascending(menu)
    elif pilih == 3:
        urutdescending(menu)
    elif pilih == 4:
        pilih_menu(menu)
    elif pilih == 5:
        print("Terima kasih telah memesan makanan")
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang tersedia.")
        panggil(menu)

panggil(menu)