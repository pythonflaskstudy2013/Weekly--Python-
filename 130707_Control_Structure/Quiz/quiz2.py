#!/usr/bin/python

def ant_sequence_v1(numbers):
    sequence = list()
    if len(numbers) > 0:
	number = target_number = numbers[0]
	i = 0
	counter = 1
	for number in numbers[1:]:
	    if number == target_number:
		counter = counter + 1
	    else:
		sequence.insert(i, str(counter))
		sequence.insert(i+1, str(target_number))
		i = i + 2
		counter = 1
		target_number = number
	sequence.insert(i, str(counter))
	sequence.insert(i+1, str(number))
    return ''.join(sequence)	

def ant_sequence_v2(numbers):
    return ''

''' http://en.wikipedia.org/wiki/Look-and-say_sequence '''
datas = ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211'];

for data in datas:
    print 'number: ' + data + ', ant sequence: ' + ant_sequence_v1(data)
