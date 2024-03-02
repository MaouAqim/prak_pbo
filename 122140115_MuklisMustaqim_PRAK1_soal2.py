def hitung_luas_dan_keliling_lingkaran(jari_jari):
  if jari_jari < 0:
      print("Jari-jari lingkaran tidak boleh negatif")
      return

  luas = 3.14 * jari_jari ** 2
  keliling = 2 * 3.14 * jari_jari

  print("Luas lingkaran:", luas)
  print("Keliling lingkaran:", keliling)

# Meminta user untuk memasukkan jari-jari lingkaran
try:
  jari_jari = float(input("Masukkan jari-jari lingkaran: "))
  hitung_luas_dan_keliling_lingkaran(jari_jari)
except ValueError:
  print("Masukkan harus berupa bilangan angka")
