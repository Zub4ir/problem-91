# %%

import pandas as pd

import re, sys, argparse

# %%

# the function
def num2word(s: str = 'Example 1234'):

    return 'Hello World'

s = 'Example R82'

# numbers meta data 
dict_numbers = {
    'int_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
    'word_number': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six', 'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 'ninety-eight', 'ninety-nine']
}

df_numbers = pd.DataFrame(dict_numbers)

# grouping meta data
data_grouping = {
    'position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'highest': ['single digit', 'double digit', 'hundred', 'thousand', 'thousand', 'thousand', 'million', 'million', 'million', 'billion', 'billion', 'billion', 'trillion'],
    'grouping': ['single digit', 'double digit', 'hundred', 'single digit', 'double digit', 'hundred', 'single digit', 'double digit', 'hundred', 'single digit', 'double digit', 'hundred', 'single digit']
}

df_grouping = pd.DataFrame(data_grouping)

# grouping meta data
dict_seperator = {0: None, 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}

# strip, fix up later
list_numbers = re.findall(pattern=r'(\d+)', string=s)
list_numbers

# final check
if len(list_numbers) != 1:

    print('number invalid')
    sys.exit(0)

# %%

# create groups of 3
num_str = str(list_numbers[0])
num_str = str('10,010,009')
result_1 = {}

# start from the right, group in threes
position = 0
while num_str:

    # take last 3 characters (or remaining if less than 3)
    group = num_str[-3:] if len(num_str) >= 3 else num_str
    result_1[position] = group
    
    # remove the last 3 characters
    num_str = num_str[:-3]
    position += 1

print(result_1)

# %%

# hundred to word
ll = list(result_1.keys())
ll.sort()
ll.reverse()

for i in ll:

    print(i)

# %%

# 1. create 0 to 99 word numbers
# 2. create hundred reader function
    # simplify str nmber to int (will remove zeros)

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
        print(f"---> reading from file: {args.file}")
        
        with open('file.txt', 'r') as f:
            sentence = f.read()

        num2word(sentence)
            
    elif args.sentence:

        # else use command line input
        print(f"---> sentence: {args.sentence}")

        num2word(args.sentence)

    else:

        parser.print_help()

# %%

if __name__ == '__main__':

    main()
