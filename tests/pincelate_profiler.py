import os
from os.path import join as opj

from pincelate import Pincelate

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    res = pin.manipulate("internationalization", features={'nas': -5, 'vcd': -5},
                                temperature=0.05)
    print(res)

pin = Pincelate(('/Users/grimmh/Documents/pincelate/pincelate/models/full-orth-phon-enc256-dec256',
                 '/Users/grimmh/Documents/pincelate/pincelate/models/full-phon-orth-enc256-dec256'))

main()
    