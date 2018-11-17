#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    print u"何の数字でアホになるか入力してください"
    aho_num = raw_input(">>>")
    print u"何回アホになりますか？"
    aho_time = raw_input(">>>")

    for i in xrange(1, int(aho_time) + 1):
        if i % int(aho_num) == 0:
            print u"Aho"
        elif aho_num in str(i):
            print (u"Aho")
        else:
            print i
            print u"GitHubのテストです"

if __name__ == '__main__':
    main()
