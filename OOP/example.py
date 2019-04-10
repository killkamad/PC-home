def letter():
	S="a1b2c3"
	trans = [""]
	for s in S:
		if not s.isalpha():
			for i in range(len(trans)):
				trans[i] += s
		else:
			for i in range(len(trans)):
				x = trans[i]
				trans[i] += s.lower()
				trans.append(x + s.upper())
	return trans

print(letter())