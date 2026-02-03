# %%

import re, sys, argparse

# %%

# numbers meta data
dict_numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty-one', 22: 'twenty-two', 23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five', 26: 'twenty-six', 27: 'twenty-seven', 28: 'twenty-eight', 29: 'twenty-nine', 30: 'thirty', 31: 'thirty-one', 32: 'thirty-two', 33: 'thirty-three', 34: 'thirty-four', 35: 'thirty-five', 36: 'thirty-six', 37: 'thirty-seven', 38: 'thirty-eight', 39: 'thirty-nine', 40: 'forty', 41: 'forty-one', 42: 'forty-two', 43: 'forty-three', 44: 'forty-four', 45: 'forty-five', 46: 'forty-six', 47: 'forty-seven', 48: 'forty-eight', 49: 'forty-nine', 50: 'fifty',
                 51: 'fifty-one', 52: 'fifty-two', 53: 'fifty-three', 54: 'fifty-four', 55: 'fifty-five', 56: 'fifty-six', 57: 'fifty-seven', 58: 'fifty-eight', 59: 'fifty-nine', 60: 'sixty', 61: 'sixty-one', 62: 'sixty-two', 63: 'sixty-three', 64: 'sixty-four', 65: 'sixty-five', 66: 'sixty-six', 67: 'sixty-seven', 68: 'sixty-eight', 69: 'sixty-nine', 70: 'seventy', 71: 'seventy-one', 72: 'seventy-two', 73: 'seventy-three', 74: 'seventy-four', 75: 'seventy-five', 76: 'seventy-six', 77: 'seventy-seven', 78: 'seventy-eight', 79: 'seventy-nine', 80: 'eighty', 81: 'eighty-one', 82: 'eighty-two', 83: 'eighty-three', 84: 'eighty-four', 85: 'eighty-five', 86: 'eighty-six', 87: 'eighty-seven', 88: 'eighty-eight', 89: 'eighty-nine', 90: 'ninety', 91: 'ninety-one', 92: 'ninety-two', 93: 'ninety-three', 94: 'ninety-four', 95: 'ninety-five', 96: 'ninety-six', 97: 'ninety-seven', 98: 'ninety-eight', 99: 'ninety-nine'}

# grouping meta data
dict_seperator = {0: '', 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}

# the function
def num2word(s: str = 'Example 1234'):

    # extract number 
    list_numbers = re.findall(pattern=r'(?<![#$\w])\d+(?![#$\w])', string=s)
    list_numbers

    # only one number 
    if len(list_numbers) != 1:

        return 'number invalid'

    # first check, is this number 0, 00, or 000...
    if int(list_numbers[0]) == 0:

        return 'zero'

    # create groups of 3
    num_str = str(list_numbers[0])
    dict_pockets = {}

    # start from the right, group in threes
    position = 0
    while num_str:

        # take last 3 characters (or remaining if less than 3)
        group = num_str[-3:] if len(num_str) >= 3 else num_str
        dict_pockets[position] = group
        
        # remove the last 3 characters
        num_str = num_str[:-3]
        position += 1

    ll = list(dict_pockets.keys())
    ll.sort()
    ll.reverse()

    result = ''
    list_result_pockets = []

    # construct word representation from each pocket
    for i in ll:

        result_pocket = ''

        # print('---> at seperator', dict_seperator[i], 'pocket', dict_pockets[i])

        # convert string pocket to digit (elimates leading zeros)
        int_digit = int(dict_pockets[i])
        str_digit = str(int_digit)

        if int_digit == 0:

            continue

        if len((str_digit)) == 3:

            sub_pocket = int(str_digit[1:3])

            result_pocket = dict_numbers[int(str_digit[0])] + ' hundred'

            if sub_pocket == 0:

                result_pocket = result_pocket + ' ' + dict_seperator[i]

            else:

                result_pocket = result_pocket + ' and ' + dict_numbers[sub_pocket] + ' ' + dict_seperator[i]

        else:

            result_pocket = dict_numbers[int_digit] + ' ' + dict_seperator[i]

        list_result_pockets.append(result_pocket.strip())

    if 'and' in list_result_pockets[-1].split(' ') or len(list_result_pockets) == 1:

        result = ', '.join(list_result_pockets)

        return result

    else:

        result = ', '.join(list_result_pockets[:-1]) + ' and ' + list_result_pockets[-1]

        return result

# %%

def main():

    # start arg parser
    parser = argparse.ArgumentParser(
                        prog='num2word.py',
                        description='A function that finds a single number in a string converts the given number into words. For example, given the number “1234” as input, return the output “one thousand, two hundred and thirty-four".')

    # optional, otherwise always file takes presedance
    parser.add_argument(
        'sentence',
        type=str,
        nargs='?',
        help='Optional string to parse via stdin.')

    parser.add_argument(
        '--file',
        type=str,
        help='Text file with string data. Multi line file will be read as single piece of text.')
    
    args = parser.parse_args()

    if args.file:
        
        # read from file    
        with open(args.file, 'r') as f:
            sentence = f.read()

        num2word(sentence)
            
    elif args.sentence:

        # else use command line input
        num2word(args.sentence)

    else:

        parser.print_help()

# %%

if __name__ == '__main__':

    main()
