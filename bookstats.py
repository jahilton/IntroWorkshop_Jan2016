book = open('TaleOfTwoCities.txt','r')

wordcount = {}
total = 0
out_file = open('wordcount.txt','w')
for word in book.read().split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

for k,v in wordcount.items():
	total += v
	out_file.write(str(k,v))
	out_file.write('\n')

out_file.write(str(total))
out_file.write('\n')

out_file.close()
book.close()
