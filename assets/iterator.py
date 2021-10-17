with open('indo.txt') as raw:
    with open('indonesia.py', 'a') as file:
        words = [word.rstrip() for word in raw]
        file.write(f'words = {str(words)}')