# in process. sorry /
def morse_bits(bits):
    bits = bits.lstrip('0').rstrip('0')
    print(bits)
    print([len(i) for i in bits.split('0')])
    n = min([len(i) for i in bits.split('1') + bits.split('0') if i])
    return bits.replace('111' * n, '-') \
        .replace('1' * n, '.') \
        .replace('0000000' * n, '  ') \
        .replace('000' * n, ' ') \
        .replace('0' * n, '') \
        .split(' ')

# запилить если

def morse_decode(morseCode):
    print(morseCode)
    CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': '',
            '.': '.-.-.-',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
            }
    code_reversed = {value: key for key, value in CODE.items()}
    return ''.join(code_reversed.get(i) for i in morseCode).lstrip().rstrip()


if __name__ == '__main__':
    code1 = '110011001100110000001100000011111100110011111100111111' \
            '000000000000001100111111001111110011111100000011001100' \
            '1111110000001111110011001100000011'
    code2 = '000000001101101001110000011000000111111010011111001111' \
            '110000000000011101111111101111101111100000010110001111' \
            '1100000111110011101100000100000'  # 'HEY JUDE'
    print(morse_bits(code1))
    print(morse_bits(code2))
