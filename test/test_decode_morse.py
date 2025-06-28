import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from decode_morse import decode_morse

def test_hey_jude():
    assert decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'

def test_basic():
    assert decode_morse('.-') == 'A'
    assert decode_morse('--...') == '7'
    assert decode_morse('...-..-') == '$'
    assert decode_morse('.') == 'E'
    assert decode_morse('..') == 'I'
    assert decode_morse('. .') == 'EE'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('...-..- ...-..- ...-..-') == '$$$'
    assert decode_morse('----- .---- ..--- ---.. ----.') == '01289'
    assert decode_morse('.-... ---...   -..-. --...') == '&: /7'
    assert decode_morse('...---...') == 'SOS'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('...   ---   ...') == 'S O S'

def test_extra_spaces():
    assert decode_morse(' . ') == 'E'
    assert decode_morse('   .   . ') == 'E E'

def test_complex():
    assert decode_morse(
        '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   '
        '-... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   '
        '--- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
    ) == 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
