#!/usr/bin/env python

"""
Takes a positive integer as an argument and prints all of its divisors.

example usage:
    python divisbles.py 100

""" 

import sys
import os, re
import numpy
import builtins
from collections import Counter
#cnt = Counter()
#pos = Counter()
#dict = {}

def getfeatfiles(corp):
    # CPA corpus
    if corp == 'CPA':
        path = 'c:/JavaProjects/FanseParser2/data/psd/CPA/feats/'
    #corp = 'CPA'
    # OEC corpus
    elif corp == 'OEC':
        path = 'C:/JavaProjects/FanseParser2/data/psd/OEC/feats/'
    #corp = 'OEC'
    # TPP corpus
    else:
        path = 'c:/JavaProjects/FanseParser2/data/psd/TPP/feats/'
    #corp = 'TPP'
    files = os.listdir(path)
    for f in files:
        # print(f)
        # if f == "by dint of.feats":
        fname = path + f
        print(f)
        analfile(fname,corp)

def analfile(fname,corp):
    #global cnt, dict
    f = open(fname)
    insts = 0
    poslist = []
    senses = []
    cnt = Counter()
    pos = Counter()
    dict = {}
    # cncnt = Counter()
    sep = '\18'
    for line in f:
        st = line[0:50]
        # OEC feats
        if corp == 'OEC':
            mat = '^[a-z \-]+\.p\.[a-z]+\..*?\.([0-9]+)\x18(.*?)\x18'
        # CPA or TPP feats
        else:
            mat = '^[a-z \']+\.p\.[a-z]+\.([0-9]+)\x18(.*?)\x18' #[0-9]+\([0-9]+|n\)|pv|x)' #(\.[0-9]+\18)' # + sep # + '(.*?)' + sep
        p1 = re.compile(mat)
        m1 = p1.search(st)
        if m1:
            s = m1.group()
            inum = m1.group(1)
            sense = m1.group(2)
            if len(sense) == 0: # around, by, down
                continue
            if sense == "pv" or sense == "x":
                continue
            if sense == "(mislabeling)": #of
                continue
            if sense == "(mislabeled)": # on
                continue
            if sense == "(misidentified)": #at, in
                continue
            if sense == "adverb": #out, outside, past, up, withing
                continue
            if sense == "(adverb)": #about, around, behind, down, round
                continue
            if sense == "(phrasal)": # around, down, round 
                continue
            if sense == "phrasal": # out, up
                continue
            if sense == "(idiom)": # after, behind
                continue
            if sense == "idiom": # out
                continue
            if sense == "(adverbial)": # in, off
                continue
            if sense == "adverbial": # inside
                continue
            if sense == "adverb3": # about
                continue
            if sense == "duplicate?": # after
                continue
            if sense == "(along with)": # along
                continue
            if sense == "(adverb6)": # around
                continue
            if sense == "(tagging error)": # around
                continue
            if sense == "(about)": # out
                continue
            if sense == "5(4)?": # for
                continue
            if sense == "1(!)": # off
                continue
            if sense == "1(1)*": # per
                continue
            if sense == "11(5)*": # on
                continue
            if sense == "11(4b)?+D1644": # to
                continue
            if sense.find(" ") > -1:
                sense = sense[0:sense.find(" ")]
            if sense == "(on": # on
                continue
            if sense == "(in": # in
                continue
            if sense == "(infinitive": # to
                continue
            if sense == "(not": # down, in
                continue
            if sense == "not": # during
                continue
            if sense == "on": # onto
                continue
            if sense == "adv": # together
                continue
            cnt[sense] += 1
            if sense not in senses:
                senses.append(sense)
                dict[sense] = Counter()
        else:
            print(st)
            continue
        #print(re.search('hr:pos:[a-z]+', line))
        #print(re.search(sep + 'hr:pos:[a-z]+' + sep, line))
        p = re.compile('hr:pos:([a-z]+)')
        m = p.search(line)
        if m:
            name = m.group(1)
            insts += 1
            pos[name] += 1
            dict[sense][name] += 1
            if name not in poslist:
                poslist.append(name)
        else:
            name = "None"
            # these are cases that don't have 'hr:pos:'
            print(st)
    f.close()
    strinst = str(insts)
    print("\tInstances = " + strinst)
    poslist.sort()
    senses.sort()
    print ("POS: ", poslist)
    parts = (corp)
    #parts = " "
    for p in poslist:
        parts += ','
        parts += p
    print (parts)
    for c in senses:
        l = c
        for p in poslist:
            l += ','
            l += str(dict[c][p])
        print (l)
    print ("Senses: ", senses)
    print (cnt)
    print (pos)
    print (cnt['2(2)'])
    #print numpy.unique(poslist)
    
def is_divisible(a, b):
    """Determines if integer a is divisible by integer b."""
    
    remainder = a % b
    # if there's no remainder, then a is divisible by b
    if not remainder:
        return True
    else:
        return False


def find_divisors(integer):
    """Find all divisors of an integer and return them as a list."""

    divisors = []
    # we know that an integer divides itself
    divisors.append(integer)
    # we also know that the biggest divisor other than the integer itself
    # must be at most half the value of the integer (think about it)
    divisor = round (integer / 2)

    while divisor > 0:
        if is_divisible(integer, divisor):
            divisors.append(divisor)
        divisor -= 1

    return divisors

if __name__ == '__main__':
    # do some checking of the user's input
    corp = input("Enter corpus: ")
    # divisors = find_divisors(test_integer)
    args = str(sys.argv)
    print (str(sys.argv))
    print (args[1])
    getfeatfiles(corp)
    # print the results
    # print ("The divisors of %d are:" % test_integer)
    # for divisor in divisors:
        # print (divisor)
