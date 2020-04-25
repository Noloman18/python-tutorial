class RomanNumerals(object):

    def __init__(self):
        pass

    def integer_to_numerals(self, number):
        if number is None:
            raise Exception("Argument cannot be null")

        if not isinstance(number, int):
            raise Exception("Argument must be an int but {} was provided".format(type(number)))

        if number < 1 or number > 3999:
            raise Exception("Number[{}] not in range 1 and 3999".format(number))

        map_i_to_v = lambda text: text.replace('iiiii', 'v').replace('iiii', 'iv')
        map_v_to_x = lambda text: text.replace('vv', 'x').replace('viv', 'ix')
        map_x_to_l = lambda text: text.replace('xxxxx', 'l').replace('xxxx', 'xl')
        map_l_to_c = lambda text: text.replace('ll', 'c').replace('lxl', 'xc')
        map_c_to_d = lambda text: text.replace('ccccc', 'd').replace('cccc', 'cd')
        map_d_to_m = lambda text: text.replace('dd', 'm').replace('dcd', 'cm')

        num_to_i_symbol = ''.ljust(number, 'i')

        return \
            map_d_to_m(
                map_c_to_d(
                    map_l_to_c(
                        map_x_to_l(map_v_to_x(
                            map_i_to_v(
                                num_to_i_symbol))))))
