#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t=int(input())
    N=0
    r=0
    s=0
    while(t>=1):
        n=t%2
        t=t//2
        N=N*10+n
    arr=[int(i) for i in str(N)]
    for i in range(0,len(arr)):
        if(arr[i]==1):
            s+=1;
            if(r<s):
                r=s
        else:
            s=0
    print(r)