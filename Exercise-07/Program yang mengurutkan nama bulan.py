#Program yang mengurutkan nama bulan secara alfabetis
nama_bulan = [
    'Januari', 'Februari', 'maret', 'april', 'Mei', 'Juni', 
    'juli', 'agustus', 'September', 'Oktober', 'november', 'desember'
]

def list():
    print("Data awal")
    print(nama_bulan)

    print("\nUrutan nama sesuai abjad pertama", end=' ')
    print("(diurutkan dari kapital terlebih dahulu)")
    print(sorted(nama_bulan))

    nama_bulan.sort(key=lambda n: n.lower())
    
    print("\nUrutan nama sesuai abjad pertama")
    print("(diurutkan tanpa mempedulikan kapital atau tidak pada huruf awal)")
    print(nama_bulan)
if __name__ == '__main__':
    list()