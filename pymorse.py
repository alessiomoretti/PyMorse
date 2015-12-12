
def setMorseDict():
	# setting up morse dictionary
	morse = dict()
	# adding morse-coded endings
	morse['l_ending']   = '/'
	morse['w_ending']   = '//'
	# inserting morse dialect - words
	morse['a']  =  '.-'
	morse['b']  =  '-...'
	morse['c']  =  '-.-.'
	morse['d']  =  '-..'
	morse['e']	=  '.'
	morse['f']  =  '..-.'
	morse['g']  =  '--.'
	morse['h']  =  '....'
	morse['i']  =  '..'
	morse['j']  =  '.---'
	morse['k']  =  '-.-'
	morse['l']  =  '.-..'
	morse['m']  =  '--'
	morse['n']  =  '-.'
	morse['o']  =  '---'
	morse['p']  =  '.--.'
	morse['q']  =  '--.-'
	morse['r']  =  '.-.'
	morse['s']  =  '...'
	morse['t']  =  '-'
	morse['u']  =  '..-'
	morse['v']  =  '...-'
	morse['w']  =  '.--'
	morse['x']  =  '-..-'
	morse['y']  =  '-.--'
	morse['z']  =  '--..'
	# inserting morse dialect - numbers
	morse['0']  =  '-----'
	morse['1']  =  '.----'
	morse['2']  =  '..---'
	morse['3']  =  '...--'
	morse['4']  =  '....-'
	morse['5']  =  '.....'
	morse['6']  =  '-....'
	morse['7']  =  '--...'
	morse['8']  =  '---..'
	morse['9']  =  '----.'

	return morse


def translateMorseWord(string, morse):
	# converted final string
	encoded = ""
	# scanning string and building-up the encoded 
	for letter in string:
		if letter in morse:
			encoded += morse[letter]
			encoded += morse['l_ending']
	
	return encoded


def translateMorse(raw_input):
    # retrieving morse
	morse = setMorseDict()
	# splitting input
	_raw_input = raw_input.split(' ')
	# initializing final string
	final = ""
	# translating each word
	for word in _raw_input:
		w_translated = translateMorseWord(word, morse)
		final += w_translated[:len(w_translated) - 1]
		final += morse['w_ending']

	return final

def translateFromMorse(raw_input):
	# retrieving morse
	morse = setMorseDict()
	# initializing final string
	final = ""
	# splitting input
	_raw_input = raw_input.split('//')
	# translating from morse retrieving first morse dict params
	morse_keys = [k for k in morse]
	morse_values = [morse[k] for k in morse]
	for word in _raw_input:
		_word = word.split('/')
		print(_word)
		for letter in _word:
			if letter in morse_values:
				final += morse_keys[morse_values.index(letter)]
		final += ' '

	return final
