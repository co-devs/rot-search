# http://www-personal.umich.edu/~jlawler/wordlist
import argparse


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def __prep_args():
    """Sets up arguments for script.

    In order to clean up the if __name__ block, we pulled out the argument
    definition and placed it in a private funtion.  This may not be the
    approved solution, but I like it.

    Returns:
        argparse.Namespace: The return value.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rotnum", type=int, default=13,
                        help="ROTx, where -r = x")
    parser.add_argument("-d", "--dictionary", default="wordlist.txt",
                        help="Dictionary")
    args = parser.parse_args()
    # print(type(args))
    return args


def rot(x, y):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return "".join([abc[(abc.find(c)+y) % 26] for c in x])


def search(word):
    with open(args.dictionary, 'r') as dic:
        for line in dic:
            if word == line.rstrip('\n'):
                return True
        return False


if __name__ == "__main__":
    args = __prep_args()
    rotnum = args.rotnum
    dictionary = args.dictionary
    with open(f"{rotnum}-findings.txt", 'w+') as findings:
        with open(dictionary, 'r') as dic:
            word = dic.readline().rstrip('\n')
            cnt = 1
            while word:
                if len(word) > 3:
                    rotted = rot(word, rotnum)
                    # print(f"{word}")
                    # print(f"Line {cnt}: {word} | {rotted}")
                    if search(rotted):
                        prog = round((cnt / 69904) * 100, 2)
                        prGreen(f"{prog}%: {word}, {rotted}")
                        findings.write(f"{word}\n")
                    else:
                        pass
                        # print(f"Not found: {word}, {rotted}")
                word = dic.readline().rstrip('\n')
                cnt += 1
