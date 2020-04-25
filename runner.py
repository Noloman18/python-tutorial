import numpy as np
from roman_numerals import RomanNumerals

if __name__ == "__main__":
    numerals = RomanNumerals()

    arr = np.arange(1, 10, dtype='i')
    arr = arr[::-1]

    for i in arr:
        print('{} = {}'.format(i, numerals.integer_to_numerals(int(i))))
