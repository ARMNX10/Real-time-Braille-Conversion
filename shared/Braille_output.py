braille_mapping = {
    'a': '1',
    'b': '12',
    'c': '14',
    'd': '145',
    'e': '15',
    'f': '124',
    'g': '1245',
    'h': '125',
    'i': '24',
    'j': '245',
    'k': '13',
    'l': '123',
    'm': '134',
    'n': '1345',
    'o': '135',
    'p': '1234',
    'q': '12345',
    'r': '1235',
    's': '234',
    't': '2345',
    'u': '136',
    'v': '1236',
    'w': '2456',
    'x': '1346',
    'y': '13456',
    'z': '1356',
    ' ': '0',     # Space represented as '0'
    '.': '256',   # Period
    ',': '2',     # Comma
    '?': '236',   # Question mark
    '!': '2366',  # Exclamation mark
    "'": '3',     # Apostrophe
    '-': '36',    # Hyphen
    ';': '2364',  # Semicolon
    ':': '346',   # Colon
    '(': '126',   # Left Parenthesis
    ')': '356',   # Right Parenthesis
    '[': '146',   # Left Square Bracket
    ']': '456',   # Right Square Bracket
    '{': '1246',  # Left Curly Brace
    '}': '2456',  # Right Curly Brace
    '<': '12346', # Left Angle Bracket
    '>': '23456'  # Right Angle Bracket
    # Add more mappings as needed
}

def text_to_braille(input_text):
    braille_output = []
    for char in input_text.lower():
        if char == ' ':  # If it's a space, add two newlines (one for space, one for word separation)
            braille_output.append('\n\n')
        else:
            braille_pins = braille_mapping.get(char, '') 
            braille_output.append(braille_pins)
    return ' '.join(braille_output)  # Join Braille pins with spaces

input_file_path = 'Output3.txt'
output_file_path = 'Braille_output.txt'

with open(input_file_path, 'r') as file:
    input_text = file.read()

braille_text = text_to_braille(input_text)

with open(output_file_path, 'w') as file:
    file.write(braille_text)
