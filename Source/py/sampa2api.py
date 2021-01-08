def sampa2api(simbol):
	consult = ""
	converter = {
	"i" : "i",
	"ɯ" : "M",
	"u" : "u",
	"ɪ" : "I",
	"ʊ" : "U",
	"e" : "e",
	"ɤ" : "7",
	"o" : "o",
	"a" : "a",
	"ɔ" : "O",
	"p" : "p",
	"b" : "b",
	"t" : "t",
	"d" : "d",
	"k" : "k",
	"g" : "g",
	"ʔ" : "?",
	"ɸ" : "p\\",
	"β" : "B",
	"s" : "s",
	"z" : "z",
	"ɬ" : "K",
	"ʃ" : "S",
	"ʒ" : "Z",
	"x" : "x",
	"ɣ" : "G",
	"h" : "h",
	"t͡s" : "ts",
	"t͡ʃ" : "tS",
	"d͡ʒ" : "dZ",
	"m" : "m",
	"n" : "n",
	"ɲ" : "J",
	"ŋ" : "N",
	"ɾ" : "4",
	"r" : "r",
	"l" : "l",
	"ɺ" : "r\\"
	}

	for i in converter:
		if simbol == i:
			consult = converter[i]
		else:
			consult = None

	return(consult)


