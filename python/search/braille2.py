
CAP_CODE = '000001'
WHITE_SPACE = '000000'


def decode(encoded_text, text):
    encoding = {}
    i = j = 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            j += 6
            continue

        if text[i].isupper():
            j += 6

        encoding[text[i].lower()] = encoded_text[j:j + 6]
        i += 1
        j += 6

    return encoding


def to_braille(text, braille_encoding):
    encoded_string = ''
    for char in text:
        if char.isupper():
            encoded_string += CAP_CODE
            char = char.lower()

        if char.isspace():
            encoded_string += WHITE_SPACE
            continue

        encoded_string += braille_encoding[char]

    return encoded_string


if __name__ == '__main__':
    s = 'The quick brown fox jumps over the lazy dog'
    char_encoding = decode(
        '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110',
        'The quick brown fox jumps over the lazy dog'
    )

    fixtures = [
        ('code', '100100101010100110100010'),
        (
            'The quick brown fox jumps over the lazy dog',
            '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110',
        ),
    ]
    for f in fixtures:
        result = to_braille(f[0], char_encoding)
        assert f[1] == result
