#!/usr/bin/env python

# The matasano crypto challenges - Set 1 Challenge 4 (http://cryptopals.com/sets/1/challenges/4/)
#
# Copyright (c) 2014 - Albert Puigsech Galicia (albert@puigsech.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys

# Cryptohelper from https://github.com/apuigsech/cryptohelper
from cryptohelper import *

def main(argv):
	with open('4.txt') as f:
		ct_samples = [line.rstrip().decode('hex') for line in f]

	pt_candidates = []
	for ct in ct_samples:
		pt_candidates += xor_statistical_candidates(ct)

	pt_candidates = sorted(pt_candidates, key=lambda x: x[2], reverse=True)
	print pt_candidates[0][1]
	

if __name__ == "__main__":
   main(sys.argv)
