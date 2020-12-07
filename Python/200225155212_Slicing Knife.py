'''
Write a program that contains a constant of the type str, with the following value: "We were more than just a slice".
Use only slicing on this string, and print out the following strings:
1) 'We wer'
2) 'ere more than just a sli'
3) 'W eemr hnjs lc'
4) 'wr oeta utasi'
5) 'ecils a tsuj naht erom erew eW'
'''
def main():
    SENTENCE = "We were more than just a slice"
    print(SENTENCE[:6])
    print(SENTENCE[4:-2])
    print(SENTENCE[::2])
    print(SENTENCE[3:-2:2])
    print(SENTENCE[-1::-1])

if __name__ == '__main__':
    main()