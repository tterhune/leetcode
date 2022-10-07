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
from collections import defaultdict
from typing import List


def tournament_winner(competitions: List[List], results: List[int]) -> str:
    team_results = defaultdict(int)

    current_leader = (0, '')

    for competition, result in zip(competitions, results):
        if result:
            team = competition[0]
        else:
            team = competition[1]

        team_results[team] += 1
        if team_results[team] > current_leader[0]:
            current_leader = (team_results[team], team)

    return current_leader[1]


if __name__ == '__main__':
    test_cases = [
        ([
                 ['HTML', 'C#'],
                 ['C#', 'Python'],
                 ['Python', 'HTML']
         ],
         [0, 0, 1],
         'Python'),
    ]

    for case in test_cases:
        c = case[0]
        r = case[1]
        e = case[2]
        print(f'{c} {r}')

        result = tournament_winner(c, r)
        print(f'result => {result}')
        assert(result == e)
