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
    # Description.

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
