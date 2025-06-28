MORSE_CODE = {
    # Letras
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',

    # Dígitos
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',

    # Pontuação e símbolos
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@',

    # Sinais especiais
    '...---...': 'SOS'
}


def decode_morse(morse_code):

    
    codigo_limpo = morse_code.strip()

    palavras_codificadas = codigo_limpo.split('   ')

    mensagem_final = []

    for palavra in palavras_codificadas:

        letras_codificadas = palavra.split(' ')
        
        letras_decodificadas = []
        for letra in letras_codificadas:
            letras_decodificadas.append(MORSE_CODE[letra])

        palavra_decodificada = ''.join(letras_decodificadas)

        mensagem_final.append(palavra_decodificada)
    return ' '.join(mensagem_final)
