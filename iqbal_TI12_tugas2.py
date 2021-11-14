print('------Toko Japur------')
print('List Barang:\n'
      '\n1.Kasur'
      '\n2.Lemari'
      '\n3.Kompor'
      '\n4.Mesin_cuci'
      '\n5.Kipas_angin \n'
      )

pilih = int(input('Pilih Nomor..'))

# Hitungan
if(pilih == 1):

    produk = 'Kasur'
    nama = str(input('Nama Pelanggan:'))
    harga = 2000000
    jumlah = int(input('Jumlah Produk:'))
    hargaKotor = harga * jumlah
    diskon = (hargaKotor * 5 / 100)
    ppn = ((hargaKotor - diskon)*10/100)
    hargaBersih = ((hargaKotor - diskon) + ppn)

    print('Nama Pembeli :%s Produk :%s harga :%i dengan jumlah :%i Harga Kotor :%i diskon%i PPN 10persen ditanggung Pembeli Pembeli%i Harga Bersihnya adalah :%i' % (
        nama, produk, harga, jumlah, hargaKotor, diskon, ppn, hargaBersih))

elif(pilih == 2):

    produk = 'Lemari'
    nama = str(input('Nama Pelanggan:'))
    harga = 4000000
    jumlah = int(input('Jumlah Produk:'))
    hargaKotor = harga * jumlah
    diskon = hargaKotor * 10/100 if jumlah >= 3 else(hargaKotor * 5 / 100)
    ppn = ((hargaKotor - diskon)*10/100)
    hargaBersih = ((hargaKotor - diskon) + ppn)

    print('Nama Pembeli :%s Produk : :%s harga :%i dengan jumlah :%i Harga Kotor :%i diskon%i PPN 10persen ditanggung Pembeli Pembeli%i Harga Bersihnya adalah :%i' % (
        nama, produk, harga, jumlah, hargaKotor, diskon, ppn, hargaBersih))

elif(pilih == 3):

    produk = 'Kompor'
    nama = str(input('Nama Pelanggan:'))
    harga = 5000000
    jumlah = int(input('Jumlah Produk:'))
    hargaKotor = harga * jumlah
    diskon = hargaKotor * 20/100 if jumlah >= 5 else(hargaKotor * 5 / 100)
    ppn = ((hargaKotor - diskon)*10/100)
    hargaBersih = ((hargaKotor - diskon) + ppn)

    print('Nama Pembeli :%s Produk : :%s harga :%i dengan jumlah :%i Harga Kotor :%i diskon%i PPN 10persen ditanggung Pembeli Pembeli%i Harga Bersihnya adalah :%i' % (
        nama, produk, harga, jumlah, hargaKotor, diskon, ppn, hargaBersih))

elif(pilih == 4):

    produk = 'Mesin Cuci'
    nama = str(input('Nama Pelanggan:'))
    harga = 3000000
    jumlah = int(input('Jumlah Produk:'))
    hargaKotor = harga * jumlah
    diskon = (hargaKotor * 5 / 100)
    ppn = ((hargaKotor - diskon)*10/100)
    hargaBersih = ((hargaKotor - diskon) + ppn)

    print('Nama Pembeli :%s Produk :%s harga :%i dengan jumlah :%i Harga Kotor :%i diskon%i PPN 10 persen ditanggung Pembeli :%i Harga Bersih :%i' % (
        nama, produk, harga, jumlah, hargaKotor, diskon, ppn, hargaBersih))

elif(pilih == 5):

    produk = 'Kipas Angin'
    nama = str(input('Nama Pelanggan:'))
    harga = 1000000
    jumlah = int(input('Jumlah Produk:'))
    hargaKotor = harga * jumlah
    diskon = (hargaKotor * 5 / 100)
    ppn = ((hargaKotor - diskon)*10/100)
    hargaBersih = ((hargaKotor - diskon) + ppn)

    print('Nama Pembeli :%s Produk : :%s harga :%i dengan jumlah :%i Harga Kotor :%i diskon%i PPN 10persen ditanggung Pembeli Pembeli%i Harga Bersihnya adalah :%i' % (
        nama, produk, harga, jumlah, hargaKotor, diskon, ppn, hargaBersih))

else:
    print('Maaf, Produk tidak ada')
