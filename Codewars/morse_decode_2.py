# !!! in progress ...
def morse_bits(bits):
    def rang(code):
        code = code.lstrip('0')
        k = len(code) - len(code.lstrip('1'))
        if k == 3 and '000000000' not in code:
            return 1
        elif k % 3 == 0 and '000000000' not in code:
            return int(k / 3)
        elif k == 3 and '000000000' in code:
            return 3
        return k

    def rang_2(code):
        code = code.lstrip('0')
        k = len(code) - len(code.lstrip('1'))
        if k % 3 == 0:
            r = int(k / 3)
            if '0' * r or '000' * r in bits:
                return k
            else:
                return int(k / 3)
        return k

    n = rang(bits)
    # n = rang_2(bits)
    return bits.replace('111' * n, '-') \
        .replace('1' * n, '.') \
        .replace('0000000' * n, '  ') \
        .replace('000' * n, ' ') \
        .replace('0' * n, '') \
        .split(' ')


def morse_decode(morseCode):
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
    return ''.join(code_reversed.get(i) for i in morseCode).lstrip()


if __name__ == '__main__':
    code = '1100110011001100000011000000111111001100111111001111110000' \
           '000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
    print(morse_decode(morse_bits(code)))
    print(morse_decode(morse_bits('111000000000111')))
    print(morse_decode(morse_bits('111110000011111')))
    code2 = '000111000101010100010000000111011101011100010101110001010001110101110100011101011100' \
            '000001110101010001011101000111011101110001011101110001110100000001010111010001110111' \
            '011100011101010111000000010111011101110001010111000111011100010111011101000101010000' \
            '000111011101110001010101110001000101110100000001110001010101000100000001011101010001' \
            '011100011101110101000111010111011100000001110101000111011101110001110111010001011101' \
            '01110101110'
    print(morse_decode(morse_bits(code2)))
    print(morse_decode(morse_bits('1110111')))
    print(morse_decode(morse_bits('11111100111111')))
    print(morse_decode(morse_bits('111000111000111')))  # S
    print(morse_decode(morse_bits('000000111000')))  # e
    print(morse_decode(morse_bits('111')))
