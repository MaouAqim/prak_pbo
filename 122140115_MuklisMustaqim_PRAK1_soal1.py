def hitung_bilangan_ganjil(bawah, atas):
  # Inisialisasi jumlah bilangan ganjil
  jumlah_ganjil = 0

  # Memastikan bawah dan atas tidak negatif
  if bawah < 0 or atas < 0:
      print(" bawah dan atas yang dimasukan tidak boleh di bawah Nol")
      return

  # Menghitung jumlah bilangan ganjil dalam rentang
  for i in range(bawah, atas + 1):
      if i % 2 != 0:
          jumlah_ganjil += 1

  # Mencetak jumlah bilangan ganjil
  print("Total", bawah, "dan", atas, "adalah:", jumlah_ganjil)

# Input bawah dan atas dari user
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

# Memanggil fungsi hitungbilanganganjil
hitung_bilangan_ganjil(bawah, atas)
