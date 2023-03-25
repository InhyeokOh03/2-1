import re

sentence = input()

swear_words = ['dumb', 'silly', 'goofy', 'stupid', 'dummy']

pattern = '|'.join('[0-9]*'.join(letter for letter in word) for word in swear_words)

output_str = re.sub(pattern, '****', sentence)

print(output_str)
