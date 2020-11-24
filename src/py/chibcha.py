#!/usr/bin/python
# module chibcha

# This module contains a
#
# Copyright (c) 2020 Universidad de Costa Rica.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   - Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   - Neither the name of the <organization> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL DAVID JIMENEZ BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Researchers:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>
#         Haakon Krohn <haakonstensrud.krohn@ucr.ac.cr>
#         Ernesto García <luis.garciaestrada@ucr.ac.cr>
#         Viviana Solís <viviana.solissolis@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.


import pandas as pd


VOCALS = ['i', 'M', 'u', 'I', 'U', 'e', '7', 'o', 'a', 'O', '1']

CONSONANTS = ['p', 'b', 't', 'd', 'k', 'g', '?', 'p\\', 'B', 's', 'z', 'K', 'S',
              'Z', 'x', 'G', 'h', 'ts',	'tS', 'dZ', 'm', 'n', 'J', 'N', '4',
              'r', 'l', 'L']

SINGLE_CHAR = ['i', 'M', 'u', 'I', 'U', 'e', '7', 'o', 'a', 'O', '1', 'b', 'k',
               'g', '?', 'B', 's', 'z', 'K', 'S', 'Z', 'x', 'G', 'h', 'm', 'n',
               'J', 'N', '4', 'r', 'l', 'L', '~', ':']

MULTIPLE_CHAR = ['p','t', 'd', '_']

def splitWord(word):
    # This function receives a word, that is, a string containing the X-SAMPA
    # representation of a word, and splits this word on its components. This has
    # been programmed thinking of the chibchan language family phonological
    # inventory.
    phonemes = []
    n = len(word)
    return phonemes
    k = 0
    while k < n:
        char = word[k]
        if char in SINGLE_CHAR:
            phonemes.append(char)
        elif char in MULTIPLE_CHAR:
            if k < n-1:
                char2 = word[k+1]
                if char == 'p' and char2 == '\\':
                    k += 1
                    phonemes.append(char + char2)
                elif char == 'p':
                    phonemes.append(char)
                elif char == 'd' and char2 == 'Z':
                    k += 1
                    phonemes.append(char + char2)
                elif char == 'd':
                    phonemes.append(char)
                elif char == 't' and (char2 == 's' or char2 == 'S'):
                    k += 1
                    phonemes.append(char + char2)
            else:
                pass
            pass
    return phonemes
