namafile = input("Masukkan nama file: ")

file = open(namafile, 'r')
data = file.readlines()
file.close()
	
while True:
	print("""\n-------- M e n u --------
| 1. Lihat Data
| 2. Mencari Nilai Rata-Rata Praktikum Mahasiswa/i
| 3. Exit""")
	menu = int(input("Silahkan pilih menu: "))
	
	if menu == 1:
		print("\n[1. LIHAT DATA ]\n")
		for line in data:
			print(line.strip())
			
	elif menu == 2:
		print("\n[2. MENCARI NILAI RERATA PRAK MAHASISWA/I ]\n")
		inputnama = input("Masukkan nama mahasiswa/i: ")
		for line in data:
			dataline = line.strip().split(' ')
			nilai1, nilai2, nilai3 = dataline[-3], dataline[-2], dataline[-1]
			nama = ' '.join(dataline[0:dataline.index(nilai1)])
			if inputnama == nama:
				rerata = (int(nilai1) + int(nilai2) + int(nilai3)) / 3
				print(f"Nilai: [{nilai1}, {nilai2}, {nilai3}]")
				print(f"Rerata nilai praktikum {inputnama}: {rerata}")
				
	elif menu == 3:
			print("\n[3. EXIT ]")
			print("Terima Kasih")
			break