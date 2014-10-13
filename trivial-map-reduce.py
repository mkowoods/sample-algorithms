#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     12/10/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



MEM = {}

def mapper(int_input):
    #function takes in an integer input and returns a list of
    #tuples [(p1, i), (p2, i),...] where p1,p2,...pk are  the prime factors
    #of i
    #For example, map(12) = [(2,12), (3,12)]

    pd = []

    copy_int_input = int_input

    while copy_int_input > 1:
        print 'copy', copy_int_input
        ul = int(copy_int_input**.5)
        for i in range(2, ul + 1):
            print i
            if copy_int_input % i == 0:
                pd.append(i)
                copy_int_input = copy_int_input/i
                break


        if i == ul:
            pd.append(copy_int_input)
            copy_int_input = 1

    pd = list(set(pd))

    return [(p, int_input) for p in pd]


def add_to_partition(map_results):
    for n in map_results:
        MEM.setdefault(n[0], [])
        MEM[n[0]].append(n[1])


def reducer(prime, list_ints):
    return (prime, sum(list_ints))

if __name__ == "__main__":

    s = [15, 21, 24, 30, 49]

    for n in s:
        m = mapper(n)
        add_to_partition(m)

    for k,v in MEM.iteritems():
        print reducer(k,v)