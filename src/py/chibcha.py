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
import numpy as np
import math


VOCALS = ['i', 'M', 'u', 'I', 'U', 'e', '7', 'o', 'a', 'O', '1']

CONSONANTS = ['p', 'b', 't', 'd', 'k', 'g', '?', 'p\\', 'B', 's', 'z', 'K', 'S',
              'Z', 'x', 'G', 'h', 'ts',	'tS', 'dZ', 'm', 'n', 'J', 'N', '4',
              'r', 'l', 'L']

SINGLE_CHAR = ['i', 'M', 'u', 'I', 'U', 'e', '7', 'o', 'a', 'O', '1', 'b', 'k',
               'g', '?', 'B', 's', 'z', 'K', 'S', 'Z', 'x', 'G', 'h', 'm', 'n',
               'J', 'N', '4', 'r', 'l', 'L', '~', ':']

MULTIPLE_CHAR = ['p','t', 'd', '_']

DIACRITC_CHAR = ['~',':','\"','_']

UNINCLUDED = []

GUAREVER = VOCALS + CONSONANTS




def prepareLists():
    # This function reads the Swadesh List file and converts it to a big
    # dictionary object.
    listsSw = pd.read_excel("../../res/listasswadesh.xlsx", sheet_name="Hoja1")
    axes = list(listsSw.axes[1])
    listasSwadesh = listsSw.to_dict()
    spanish = listasSwadesh[axes[1]]
    K = len(axes)
    k = 2
    chibchan_lists = {}
    while k < K:
        language_name = axes[k]
        chibchan_language = listasSwadesh[language_name]
        chibchan_dict = {}
        for n in range(len(chibchan_language)):
            spanish_word = spanish[n]
            chibchan_word = chibchan_language[n]
            if type(chibchan_word) == str:
                chibchan_dict[spanish_word] = chibchan_word
        chibchan_lists[language_name] = chibchan_dict
        k += 1
    return chibchan_lists



def prepareFeatures():
    # This function reads the Feature List and converts it into two dictionary
    # objects, one for vowels and one for consonants.
    df_vow = pd.read_excel("../../res/rasgos.xlsx", sheet_name="vocales")
    df_con = pd.read_excel("../../res/rasgos.xlsx", sheet_name="consonantes")
    vowel_list = df_vow.to_dict()
    vowel_axes = list(df_vow.axes[1])
    consonant_list = df_con.to_dict()
    consonant_axes = list(df_con.axes[1])
    # features = vowel_list[vowel_axes[1]]
    vowels = {}
    consonants = {}
    k = 1
    K = len(vowel_axes)
    while k < K:
        phoneme_name = vowel_axes[k]
        phoneme_features = vowel_list[phoneme_name]
        output_features = []
        for n in range(len(phoneme_features)):
            output_features.append(phoneme_features[n])
        vowels[phoneme_name] = output_features
        k += 1
    features = consonant_list[consonant_axes[1]]
    k = 1
    K = len(consonant_axes)
    while k < K:
        phoneme_name = consonant_axes[k]
        phoneme_features = consonant_list[phoneme_name]
        output_features = []
        for n in range(len(phoneme_features)):
            output_features.append(phoneme_features[n])
        consonants[phoneme_name] = output_features
        k += 1
    return vowels, consonants


# New global variables.
# For some reason, if I add them at the beginning, it gives an error.
chibchan_swadesh_lists = prepareLists()
vowels, consonants = prepareFeatures()


def phonemeDistance(phoneme1,phoneme2):
    # This function returns the distance between two phonemes. It assumes that
    # the phonemes are in the lists, so, careful what you feed into it. The
    # distance is simple: if one phoneme is blank (" "), then it returns 1. If
    # one of the phonemes is a vowel and the other is a consonant, then it
    # returns 1. If both are vowels or both are consonants, it returns the
    # number of differing features divided by the total number of features.
    if phoneme1 == phoneme2:
        d = 0
    elif phoneme1 == " " or phoneme2 == " ":
        d = 1
    elif phoneme1 in VOCALS and phoneme2 in CONSONANTS:
        d = 1
    elif phoneme1 in CONSONANTS and phoneme2 in VOCALS:
        d = 1
    elif phoneme1 in VOCALS and phoneme2 in VOCALS:
        feat1 = vowels[phoneme1]
        feat2 = vowels[phoneme2]
        K = len(feat1)
        dist = 0
        for k in range(K):
            if feat1[k] != feat2[k]:
                dist += 1
        d = dist/K
    elif phoneme1 in CONSONANTS and phoneme2 in CONSONANTS:
        feat1 = consonants[phoneme1]
        feat2 = consonants[phoneme2]
        K = len(feat1)
        dist = 0
        for k in range(K):
            if feat1[k] != feat2[k]:
                dist += 1
        d = dist/K
    return d

def alignWords(word1, word2):
    # This function takes two strings and alings them using the basic idea of
    # the Needleman Wunst algorithm.
    word1 = flattenWord(splitWord(word1))
    word2 = flattenWord(splitWord(word2))
    K = len(word1)
    N = len(word2)
    alignmentMatrix = np.empty((K+1,N+1))
    alignmentMatrix[:] = np.NaN
    alignmentMatrix[:,0] = 0
    alignmentMatrix[0,:] = 0
    return alignmentMatrix

def checkShit():
    langs = list(chibchan_swadesh_lists.keys())
    for x in langs:
        listota = chibchan_swadesh_lists[x]
        swadi = list(listota.keys())
        for y in swadi:
            splitWord(listota[y])
    pass





def splitWord(word):
    # This function receives a word, that is, a string containing the X-SAMPA
    # representation of a word, and splits this word on its components. This has
    # been programmed thinking of the chibchan language family phonological
    # inventory.
    phonemes = []
    n = len(word)
    k = 0
    while k < n:
        char = word[k]
        if char in SINGLE_CHAR:
            phonemes.append(char)
            if char in GUAREVER:
                GUAREVER.remove(char)
        elif char in MULTIPLE_CHAR:
            if k < n-1:
                char2 = word[k+1]
                if char == 'p' and char2 == '\\':
                    k += 1
                    phonemes.append(char + char2)
                    #DELETE LATER
                    if char+char2 in GUAREVER:
                        GUAREVER.remove(char+char2)

                elif char == 'p':
                    phonemes.append(char)

                    #DELETE LATER
                    if char in GUAREVER:
                        GUAREVER.remove(char)

                elif char == 'd' and char2 == 'Z':
                    k += 1
                    phonemes.append(char + char2)

                    #DELETE LATER
                    if char+char2 in GUAREVER:
                        GUAREVER.remove(char+char2)

                elif char == 'd':
                    phonemes.append(char)

                    #DELETE LATER
                    if char in GUAREVER:
                        GUAREVER.remove(char)

                elif char == 't' and (char2 == 's' or char2 == 'S'):
                    k += 1
                    phonemes.append(char + char2)

                    #DELETE LATER
                    if char+char2 in GUAREVER:
                        GUAREVER.remove(char+char2)

                elif char == 't':
                    phonemes.append(char)

                    #DELETE LATER
                    if char in GUAREVER:
                        GUAREVER.remove(char)

                elif char in DIACRITC_CHAR:
                    if char2 == 'H' or char2 == 'L' or char2 == '/' or char2 == '\"':
                        k += 1
                        phonemes.append(char + char2)

                        #DELETE LATER
                        if char+char2 in GUAREVER:
                            GUAREVER.remove(char+char2)

                    else:
                        print(char)
                        # print('\n')

                else:
                    print(char)
                    # print('\n')
            else:
                phonemes.append(char)
        elif char == 'ñ':
            phonemes.append('J')
        else:
            # print(char)
            if char not in UNINCLUDED:
                UNINCLUDED.append(char)
        k += 1
    return phonemes

def flattenWord(word):
    # This function returns the list of characters without accents, tones or
    # suprasegmentals.
    return [char for char in word if char in VOCALS or char in CONSONANTS]
