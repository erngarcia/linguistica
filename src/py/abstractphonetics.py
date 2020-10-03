#!/usr/bin/python
# module abstractphonetics

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


#################
#################
#################
###           ###
###   NOTES   ###
###           ###
#################
#################
#################


################################
################################
##                            ##
##  IMPLEMENTATION DECISIONS  ##
##                            ##
################################
################################


###################
###################
##               ##
##  LIMITATIONS  ##
##               ##
###################
###################


###########
# IMPORTS #
###########

####################
# GLOBAL VARIABLES #
####################

################################
################################
################################
###                          ###
###   METHODS AND FUNCTIONS  ###
###                          ###
################################
################################
################################

#################
#################
##             ##
##  FUNCTIONS  ##
##             ##
#################
#################


###############
###############
##           ##
##  METHODS  ##
##           ##
###############
###############



###################
###################
###################
###             ###
###   CLASSES   ###
###             ###
###################
###################
###################


##########################
##########################
##                      ##
##  CLASS ABSTRACTPHONE ##
##                      ##
##########################
##########################
class AbstractPhone:
    # This is the class AbstractPhone, that represents, in the most abstract way
    # possible, a phone object as in acustic or articularoty phonetics, but also,
    # if it is the case, phones in the sense of signs in sign language. Even so,
    # if the need arises, it could be used to implement syllabaries.
    #
    # This class has three main attributes:
    #
    # - _features: This is a dictionary, where each key corresponds to a
    #              predefined list of features, given globally by the phonetic
    #              system, and the value is either True, False or None. None is
    #              used only if the particular feature is not specified yet.
    #
    # - _name: This is also a dictionary. In this case, the key is the type of
    #          name to include, for example, in articularoty phonetics, it could
    #          be voicing, point of articulation, manner of articulation, etc.
    #          The value is, the actual value of this particular, like voiced or
    #          unvoiced, plossive, fricative, etc.
    #
    # - _symbol: This is a string, often consisting on a single character, that
    #            identifies the phone in a unique manner. It could be the
    #            IPA symbol, or the X-SAMPA.
    #

    ##############
    # ATTRIBUTES #
    ##############
    _features = {}
    _name     = {}
    _symbol   = ""



    ############
    # CREATORS #
    ############
    def __init__(self,theFeatures,theName,theSymbol):
        # This is a simple creator for the class AbstractPhone. Takes as
        # arguments the following:
        #
        # - theFeatures: This is a dictionary in which the key is the respective
        #                feature name, and the value is True or False, as it
        #                corresponds.
        #
        # - theName: This is a dictionary in which the key is the naming
        #            cathegory and the value is the corresponding name.
        #
        # - theSymbol: String that contains the single character or set of
        #              characters that uniquely identifies the phone.
        #
        self._symbol = theSymbol
        keys = theName.keys()
        for x in keys:
            self._name[x] = theName[x]
        keys = theFeatures.keys()
        for x in keys:
            self._features[x] = theFeatures[x]

    ###########
    # GETTERS #
    ###########
    def getSymbol(self):
        return self._symbol

    def getName(self):
        pass

    def getFeatures(self):
        pass

    def getNameValue(self,cathegory):
        return self._name[cathegory]

    def getFeatureValue(self,feature):
        return self._features[feature]


    ###########
    # SETTERS #
    ###########
    def setSymbol(self,symbol):
        self._symbol = symbol

    def setName(self,name):
        keys = name.keys()
        for key in keys:
            self._name[key] = name[key]

    def setFeatures(self,features):
        keys = features.keys()
        for key in keys:
            self._features[key] = features[key]

    def setNameValue(self,key,value):
        self._name[key] = value

    def setFeatureValue(self,key,value):
        self._features[key] = value


    ###########
    # METHODS #
    ###########


##############################
##############################
##                          ##
##  CLASS ABSTRACTPHONETICS ##
##                          ##
##############################
##############################

class AbstractPhoneticSystem:
    # Description.

    ##############
    # ATTRIBUTES #
    ##############
    _inventory = []
    _rules     = []
    _features  = []
    _names     = []


    ############
    # CREATORS #
    ############
    def __init__(self,featureArray,namingArray):
        self.features = featureArray
        self.names    = namingArray




    ###########
    # GETTERS #
    ###########


    ###########
    # SETTERS #
    ###########

    ###########
    # METHODS #
    ###########
    def addPhone(phone):
        pass

    def addRule(self,rule):
        pass




######################
######################
##                  ##
##  CLASS SOMECLASS ##
##                  ##
######################
######################

class FeatureRule:
    # Description.

    ##############
    # ATTRIBUTES #
    ##############


    ############
    # CREATORS #
    ############


    ###########
    # GETTERS #
    ###########


    ###########
    # SETTERS #
    ###########

    ###########
    # METHODS #
    ###########
    pass


###############
# END OF FILE #
###############