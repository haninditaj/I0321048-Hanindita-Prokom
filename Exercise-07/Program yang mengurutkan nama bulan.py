#Program yang mengurutkan nama bulan secara alfabetis
nama_bulan = [
    'Januari', 'Februari', 'maret', 'april', 'Mei', 'Juni', 
    'juli', 'agustus', 'September', 'Oktober', 'november', 'desember'
]

def list():
    print("Kondisi awal:")
    print(nama_bulan)

    print("\nMenggunakan fungsi sorted:")
    print(sorted(nama_bulan))

    nama_bulan.sort(key=lambda n: n.lower())
    
    print("\nKondisi akhir:")
    print(nama_bulan)
if __name__ == '__main__':
    list()