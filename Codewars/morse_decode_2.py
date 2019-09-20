"""
In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects
the wires together, which can be detected on a remote station. The Morse code encodes every
character being transmitted as a sequence of "dots" (short presses on the key) and "dashes"
(long presses on the key).
When transmitting the Morse code, the international standard specifies that:
"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.

В этом ката вы должны написать декодер азбуки Морзе для проводного электрического телеграфа.
Электрический телеграф работает на 2-х проводной линии с ключом, который при нажатии соединяет
провода вместе, которые можно обнаружить на удаленной станции. Азбука Морзе кодирует каждый
символ передается в виде последовательности «точек» (коротких нажатий на клавишу) и «тире»
(длительное нажатие на клавишу).
При передаче азбуки Морзе международный стандарт указывает, что:
«Точка» - это 1 единица времени.
«Тире» - это 3 единицы времени.
Пауза между точками и тире в символе - 1 единица времени.
Пауза между символами внутри слова - это 3 единицы времени.
Пауза между словами - это 7 единиц времени.
"""


def morse_bits(bits):
    bits = bits.lstrip('0').rstrip('0')
    n = min([len(i) for i in bits.split('1') + bits.split('0') if i])
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
    code2 = '000111000101010100010000000111011101011100010101110001010001110101110100011101011100' \
            '000001110101010001011101000111011101110001011101110001110100000001010111010001110111' \
            '011100011101010111000000010111011101110001010111000111011100010111011101000101010000' \
            '000111011101110001010101110001000101110100000001110001010101000100000001011101010001' \
            '011100011101110101000111010111011100000001110101000111011101110001110111010001011101' \
            '01110101110'
    print(morse_decode(morse_bits(code)))
    print(morse_decode(morse_bits(code2)))
    print(morse_decode(morse_bits('1110111')))
    print(morse_decode(morse_bits('11111100111111')))
    print(morse_decode(morse_bits('111000111000111')))
    print(morse_decode(morse_bits('000000011100000')))
    print(morse_decode(morse_bits('111')))
    print(morse_decode(morse_bits('111000000000111')))
    print(morse_decode(morse_bits('111110000011111')))
