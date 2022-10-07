# -*- coding: utf-8 -*-
##########################################################################
#
# Copyright (C) 2022 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
# The contents of this software are proprietary and confidential
# to the Hewlett Packard Enterprise Development LP.  No part of this
# program may be photocopied, reproduced, or translated into another
# programming language without prior written consent of the
# Hewlett Packard Enterprise Development LP.
#
##########################################################################
def runLengthEncoding(string):
    counter = 1
    encoded = ''

    prev = string[0]
    for i in range(1, len(string)):
        if string[i] == prev and counter < 9:
            counter += 1
            continue

        encoded += f'{counter}{prev}'
        counter = 1
        prev = string[i]

    encoded += f'{counter}{prev}'

    return encoded