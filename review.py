data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		print(len(data))
print('讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len +=len(d) 
print('留言平均長度為:', sum_len/len(data))


print(data[1])
print('---------------')
print(data[2])