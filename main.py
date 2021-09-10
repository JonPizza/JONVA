import sys

def get_lines(f):
    contents = open(f).read()
    return contents.replace('\n', '').split(';')

def run_line(line, f, ln):
    if line.split('(')[0] == 'System.out.println':
        print(line.replace('4 + 2', '8').replace('"', '').split('(')[-1][:-1])
    elif line.split('(')[0] == 'System.out.print':
        print(line.replace('4 + 2', '8').replace('"', '').split('(')[-1][:-1], end='')
    elif line.split('(')[0] == 'System.out.printlnRed':
        print('\u001b[31m' + line.replace('4 + 2', '8').replace('"', '').split('(')[-1][:-1] + '\u001b[0m')
    else:
        print('SYNTAX ERROR')
        print('Traceback: Most Recent Call Last')
        print(f'file:{f} line:{ln} -- {line}')
        exit()

def main():
    filename = sys.argv[1]
    for i, line in enumerate(get_lines(filename)):
        if line != '':
            run_line(line, filename, i + 1)

if __name__ == '__main__':
    main()