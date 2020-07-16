a=1
while a<101:
	if a % 7 == 0:
		a = a + 1
		continue
	elif a % 10 == 7 or a // 10 ==7:
		a = a + 1
	else:
		print(a)
		a = a + 1

