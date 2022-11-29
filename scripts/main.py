#!/usr/bin/env python3


from Instansiation import *
from KeyPairOps import *
import os, sys
import argparse


def main():
'''
    available_keys = list_key_pair()
    filter_list = []

    for idx in available_keys:
        filter_list.append(idx)

    for idx in filter_list:
        res = str(idx).split('-')

        vals = res[1] 
        print(vals)
'''
  create_ec2()



if __name__ == '__main__':
    main()
