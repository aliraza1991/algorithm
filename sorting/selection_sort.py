def selection_sort(sort_list):
	for i in range(0, len(sort_list)-1):
		print(sort_list[i])
		min_val = i

		for j in range(i+1, len(sort_list)):
			if sort_list[j] < sort_list[min_val]:
				min_val = j

		if min_val != i:
			sort_list[min_val], sort_list[i] = sort_list[i], sort_list[min_val]
	return sort_list

sort = selection_sort([1, 5, 9, 16, 25,0,2,57,6])

print(sort)