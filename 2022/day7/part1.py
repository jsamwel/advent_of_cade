from os.path import join, dirname, basename
import json

with open('puzzle_input.txt') as file:
    puzzle_input = file.read().splitlines()


def navigate_folder(path: str, cmd: str):
    if cmd == '..':
        path = dirname(path)
    elif cmd == '/':
        path = 'root'
    else:
        path = join(path, cmd)

    return path


def fill_dict(structure: dict, keys: list, contents: dict):
    for key in keys[:-1]:
        if key in structure:
            structure = structure[key]
        else:
            structure[key] = {}
            structure = structure[key]

    structure[keys[-1]] = contents


def get_folder_size(name: str, structure: dict, folder_list: list, max_size: int):
    total_size = 0
    
    for key, value in structure[name].items():
        if isinstance(value, dict):
            total_size += get_folder_size(key, structure[name], folder_list, max_size)
        else:
            total_size += int(value)
        
    if total_size <= max_size:
        folder_list.append([name, total_size])
        
    return total_size


formatted_commands = []
for index, item in enumerate(puzzle_input):
    if item[0] == '$':
        formatted_commands.append([index, item[2:].split(' ')])

current_path = ''
folder_structure = {}

for index, command in enumerate(formatted_commands):
    if command[1][0] == 'ls':
        next_index = len(puzzle_input) if len(formatted_commands) == index + 1 else formatted_commands[index + 1][0]
        command[1].extend(puzzle_input[command[0] + 1:next_index])

        content_dict = {}

        for part in command[1][1:]:
            part_split = part.split(' ')
            content_dict[part_split[1]] = {} if part_split[0] == 'dir' else part_split[0]

        fill_dict(folder_structure, current_path.split('\\'), content_dict)

    if command[1][0] == 'cd':
        current_path = navigate_folder(current_path, command[1][1])

pretty = json.dumps(folder_structure, indent=4)
print(pretty)

folder_list = []
root = list(folder_structure.keys())[0]
total = get_folder_size(root, folder_structure, folder_list, 100000)

total_filtered = 0

for folder in folder_list:
    total_filtered += folder[1]
    
print('Total of folders with size less than 100000: ', total_filtered)