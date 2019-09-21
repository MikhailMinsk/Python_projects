def decodeMorse(morse_code):
    """
    In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly
    superceded by voice and digital data communication channels, it still has its use in some applications
    around the world.
    The Morse code encodes every character as a sequence of "dots" and "dashes". For example,
    the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
    The Morse code is case-insensitive, traditionally capital letters are used. When the message
    is written in Morse code, a single space is used to separate the character codes and 3 spaces
    are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

    В этом ката вы должны написать простой декодер азбуки Морзе. Хотя азбука Морзе сейчас в основном
    замененный речевыми и цифровыми каналами передачи данных, он все еще используется в некоторых приложениях
    во всем мире.
    Азбука Морзе кодирует каждый символ как последовательность «точек» и «тире». Например,
    буква A кодируется как · -, буква Q кодируется как −− · -, а цифра 1 кодируется как · ---.
    Азбука Морзе нечувствительна к регистру, традиционно используются заглавные буквы. Когда сообщение
    написано азбукой Морзе, для разделения кодов символов и 3 пробелов используется один пробел
    используются для разделения слов. Например, сообщение HEY JUDE на азбуке Морзе выглядит следующим образом:
    ··· · - · --- - - ···.
    """

    CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': '',
            '.': '.-.-.-', 'SOS': '...---...',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.',

            '!': '-.-.--',
            }
    code_reversed = {value: key for key, value in CODE.items()}
    return ''.join(code_reversed.get(i) for i in morse_code.split(' ')).lstrip().rstrip().replace('  ', ' ')


if __name__ == '__main__':
    print(decodeMorse('.... . -.--   .--- ..- -.. .'))
