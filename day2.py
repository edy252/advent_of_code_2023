import re
from collections import defaultdict

file_path = "day2.txt"
pattern = r'\b(\d+)\b'

real_n = {
    'red': 12, 'green': 13, 'blue': 14
}

def validate(pull_dict):
    for key, real_ct in real_n.items():
        if pull_dict[key] > real_ct:
            return False
        
    return True

def func():
    sum = 0
    with open(file_path, 'r') as file:

        for line in file:
            # Get game id
            match = re.search(pattern, line)
            id = match.group(1)
            # print('id', id)
            print(line)

            # Get pulls
            pattern2 = r':\s(.*)'
            match = re.search(pattern2, line)
            text = match.group(1)
            # print(text)

            # Get each pull
            pullarr = text.split('; ')
            # print(pullarr)

            # In each pull, create a dict
            pull_dict = defaultdict(int)
            skip = False
            for pull in pullarr:
                allcolors = pull.split(', ')

                for color in allcolors:
                    color_pair = color.split(' ')
                    # print(color_pair)
                    number = color_pair[0]
                    color = color_pair[1]

                    pull_dict[color] = max(int(number), pull_dict[color])

            # Compute power
            power = 1
            for val in pull_dict.values():
                power *= val

            sum += power
            
            # break

    return sum


ans = func()
print(ans)