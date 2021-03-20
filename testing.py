import time
def max_len_list(lists, base):
	# i = 1
	new_list = []
	print(lists)
	for row in range(0, len(lists)+1):
		k = []
		for col in range(row+1, len(lists)):
			# print(lists[row], lists[col])
			# print(lists[row]+ lists[col])
			if lists[row] in new_list:
				contiue
			if (lists[row] + lists[col]) % base != 0:
				k.append(lists[row])
				# return False
				# if lists[row] not in k:
				# print(lists[row], lists[col], lists[row] + lists[col])
				# k.append(lists[row])
					
		print(k)
		# i += 1
	return new_list

t0 = time.time()
li = max_len_list([1, 3, 5, 7, 9, 11,12, 4], 8)
# li = max_len_list([770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493], 5) #6
# li = max_len_list([278,576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436],7) # 11
# li = max_len_list([422346306, 940894801, 696810740, 862741861, 85835055, 313720373],9) #5

print(len(li), li)
t1 = time.time()
# print(t1 - t0)