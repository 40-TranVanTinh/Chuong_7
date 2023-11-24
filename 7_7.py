def tinh_so_to_tien(tien):

	loai_tien = [500000,200000,100000,50000]

	for i in loai_tien:
	 so_to = tien/i
	 print ("co %d to %d nghin dong" %(so_to, i))
	 tien = tien%i

print (" Nhap so tien:")
n = int(input(">"))
tinh_so_to_tien(n)


