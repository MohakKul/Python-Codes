from sys import stdin, stdout
def main():
    a,b = [int(i) for i in stdin.readline().split()]
    c = stdin.readline().split()
    answers = ('EVEN', 'ODD')
    def do(query):
        index = int(query.split()[-1]) - 1
        if query[0] == '0':
            stdout.write('{}\n'.format(answers[c[index] == '1']))
        else:
            c[index] = '0' if c[index] == '1' else '1'
        for query in stdin.read().splitlines():
            do(query)
main()
