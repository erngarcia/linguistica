#!/usr/bin/python
# module acusticphonetics

# This module contains an implementation of the accustic phonetic system, based
# on the class "abstractphonetics"
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

##hay un problema en la creacion del objeto.
acousticPhonetics = AbstractPhoneticSystem()

##objeto no instanciado.
acousticPhonetics.addPhone(
    AbstractPhone(
        {"HIGH": True,
         "LOW":False,
         "BACK":False,
         "ROUND":False,
         "TENSE":True
         },
         {
         ""
         },
         "i"

    )
)
#TODO: resolver el tema de los +-, porque esta siendo un unicode char y no un bool
# creo que tambien si los rasgos que identificaron Haakon y Viviana eran esos, hay algunos que van
# a quedar vacios siempre en el codigo.

consonants = {
    "p": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": True, "CORONAL": False, "DORSAL": False},
    "b": {"sonorante": False, "sonora": True, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": True, "CORONAL": False, "DORSAL": False},
    "t": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "d": {"sonorante": False, "sonora": True, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "k": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": False, "DORSAL": True},
    "g": {"sonorante": False, "sonora": True, "nasal": False, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": False, "DORSAL": True},
    "\"u0294": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": False,
                "lateral": False, "LABIAL": False, "CORONAL": False, "DORSAL": False},
    "\"u0278": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False,
                "lateral": False, "LABIAL": True, "CORONAL": False, "DORSAL": False},
    "\"u03b2": {"sonorante": False, "sonora": True, "nasal": False, "continua": True, "del rel": False,
                "lateral": False, "LABIAL": True, "CORONAL": False, "DORSAL": False},
    "s": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "z": {"sonorante": False, "sonora": True, "nasal": False, "continua": True, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "\"u026c": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False,
                "lateral": True, "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "\"u0283": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False,
                "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": True},
    "\"u0292": {"sonorante": False, "sonora": True, "nasal": False, "continua": True, "del rel": False,
                "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": True},
    "x": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": False, "DORSAL": True},
    "\"u0263": {"sonorante": False, "sonora": True, "nasal": False, "continua": True, "del rel": False,
                "lateral": False, "LABIAL": False, "CORONAL": False, "DORSAL": True},
    "h": {"sonorante": False, "sonora": False, "nasal": False, "continua": True, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": False, "DORSAL": False},
    "t\"u0361s": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": True,
                  "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": False},
    """t"\"u0361"\"u0283""": {"sonorante": False, "sonora": False, "nasal": False, "continua": False, "del rel": True,
                              "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": True},
    """d"\"u0361"\"u0292""": {"sonorante": False, "sonora": True, "nasal": False, "continua": False, "del rel": True,
                              "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": True},
    "m": {"sonorante": True, "sonora": True, "nasal": True, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": True, "CORONAL": False, "DORSAL": False},
    "n": {"sonorante": True, "sonora": True, "nasal": True, "continua": False, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    """\"u0272""": {"sonorante": True, "sonora": True, "nasal": True, "continua": False, "del rel": False,
                    "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": True},
    "\"u014b": {"sonorante": True, "sonora": True, "nasal": True, "continua": False, "del rel": False, "lateral": False,
                "LABIAL": False, "CORONAL": False, "DORSAL": True},
    """\"u027e""": {"sonorante": True, "sonora": True, "nasal": False, "continua": """\"u00b1""", "del rel": False,
                    "lateral": False, "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "r": {"sonorante": True, "sonora": True, "nasal": False, "continua": True, "del rel": False, "lateral": False,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    "l": {"sonorante": True, "sonora": True, "nasal": False, "continua": True, "del rel": False, "lateral": True,
          "LABIAL": False, "CORONAL": True, "DORSAL": False},
    """\"u027d" \/ \"u027a""": {"sonorante": True, "sonora": True, "nasal": False, "continua": "\"u00b1",
                                "del rel": False, "lateral": "\"u00b1", "LABIAL": False, "CORONAL": True,
                                "DORSAL": False}}

vowels = {"i":{"cerrada":True,"abierta":False,"laxa":False,"posterior":False,"redondeada":False},"\u026f":{"cerrada":True,"abierta":False,"laxa":False,"posterior":True,"redondeada":False},"u":{"cerrada":True,"abierta":False,"laxa":False,"posterior":True,"redondeada":True},"\u026a":{"cerrada":True,"abierta":False,"laxa":True,"posterior":False,"redondeada":False},"\u028a":{"cerrada":True,"abierta":False,"laxa":True,"posterior":True,"redondeada":True},"e":{"cerrada":False,"abierta":False,"laxa":False,"posterior":False,"redondeada":False},"\u0264":{"cerrada":False,"abierta":False,"laxa":False,"posterior":True,"redondeada":False},"o":{"cerrada":False,"abierta":False,"laxa":False,"posterior":True,"redondeada":True},"a":{"cerrada":False,"abierta":True,"laxa":False,"posterior":"\u00b1","redondeada":False},"\u0254":{"cerrada":False,"abierta":True,"laxa":False,"posterior":True,"redondeada":True}}






























###############
# END OF FILE #
###############
