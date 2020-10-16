#!/usr/bin/python
# module phonetics

# Copyright (c) 2020 Universidad de Costa Rica
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
# DISCLAIMED. IN NO EVENT SHALL UNIVERSIDAD DE COSTA RICA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Investigators:
#         David Jimenez <david.jimenezlopez@ucr.ac.cr>

# This module contains the methods, classes and variables necessary for the
# implementation of a phonetic system necessary for a research project.

###############
###############
##           ##
##  IMPORTS  ##
##           ##
###############
###############

#############
#############
##         ##
## CLASSES ##
##         ##
#############
#############

class Phone:
    ##############n
    # ATTRIBUTES #
    ##############

    ###########
    # GETTERS #
    ###########

    ###########
    # SETTERS #
    ###########

    #############
    # FUNCTIONS #
    #############

    pass

class FeatureRule:
    # This class implements a small container of a Feature Rule. For example,
    # +CONSONANTAL implies -SYLLABIC could be one of the rules.
    # In this case, both the antecedent as the consequent are lists, as it might
    # be the case there are several arguments on each of these part,

    ##############n
    # ATTRIBUTES #
    ##############

    ###########
    # GETTERS #
    ###########

    ###########
    # SETTERS #
    ###########

    #############
    # FUNCTIONS #
    #############

    pass

class PhoneticSystem:
    ##############
    # ATTRIBUTES #
    ##############

    ###########
    # GETTERS #
    ###########

    ###########
    # SETTERS #
    ###########

    #############
    # FUNCTIONS #
    #############

    pass

#############
#############
##         ##
## METHODS ##
##         ##
#############
#############



######################
######################
##                  ##
## GLOBAL VARIABLES ##
##                  ##
######################
######################

#haakon y viviana no identificaron todos estos rasgos, entonces siempre tendremos espacios nulos si lo queremos usar para crear reglas
NAME_DICT ={
        "PLACE_OF_ARTICULATION":
            [
                "BILABIAL",
                "LABIO_DENTAL",
                "LINGUO_DENTAL",
                "DENTAL",
                "ALVEOLAR",
                "POST_ALVEOLAR",
                "RETROFLEX",
                "PALATAL",
                "VELAR",
                "UVULAR",
                "PHARYNGEAL",
                "GLOTTAL"
            ],
        "MANNER_OF_ARTICULATION":
            [
                "NASAL",
                "STOP",
                "AFFRICATE",
                "FRICATIVE",
                "TRILL",
                "FLAP",
                "FRICATIVE",
                "LATERAL_FRICATIVE",
                "APPROXIMANT",
                "LATERAL_APPROXIMANT"
            ],
        "PHONATION":
            [
                "VOICED",
                "VOICELESS"
            ],
        "VOICE_ONSET_TYPE":
            [
                "STRONG_ASPIRATION",
                "MODERATE_ASPIRATION",
                "MILD_ASPIRATION",
                "TENUIS",
                "PARTIALLY_VOICED",
                "FULLY_VOICED"
            ],
        "AIRSTREAM_MECHANISM":
            [
                "PULMONIC_EGRESSIVE",
                "EJECTIVE",
                "CLICK",
                "IMPLOSSIVE"
            ],
        "LENGTH":
            [
                "SINGLE",
                "GEMINATED"
            ],
        "HEIGHT":
            [
                "HIGH",
                "NEAR_HIGH",
                "HIGH_MID",
                "MID",
                "LOW_MID",
                "NEAR_LOW",
                "LOW"
            ],
        "BACKNESS":
            [
                "FRONT",
                "NEAR_FRONT",
                "CENTRAL",
                "NEAR_BACK",
                "BACK"
            ],
        "ROUNDEDNESS":
            [
                "ROUNDED",
                "UNROUNDED"
            ],
        "FRONT_RAISED_RETRACTED":
            [
                "FRONT",
                "RAISED",
                "RETRACTED"
            ],
        "NAZALIZATION":
            [
                "NAZALIZED"
                "NOT_NAZALIZED"
            ],
        "PHONATION":
            [
                "MODAL_VOICE",
                "UNVOICED",
                "ASPIRATED",
                "BREATHY_VOICE",
                "SLACK_VOICE",
                "CREAKY_VOICE",
                "STIFF_VOICE"
            ]
    }

#haakon y viviana no identificaron todos estos rasgos, entonces siempre tendremos espacios nulos
FEATURES = [
        "SYLLABIC",
        "SONORANT",
        "CONSONANTAL"
        "HIGH",
        "LOW",
        "BACK",
        "ROUND",
        "TENSE",
        "CORONAL",
        "ANTERIOR",
        "STRIDENT",
        "DISTRIBUTED",
        "CONTINUANT",
        "DELAYED_RELEASE",
        "NASAL",
        "LATERAL",
        "SPREAD_GLOTTIS",
        "CONSTRICTED_GLOTTIS",
        "VOICE",
        "LONG",
        "STRESS"
    ]
