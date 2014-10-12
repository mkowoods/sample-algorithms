#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     12/10/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np


# graph consistst of 3 nodes A,B,C.
# Node A has 2 outbound links to B and C
# Node B has 1 outbound link to Node C and 1 inbound link from A
# Node C has 1 looping link (C to C) and 2 in boud links


M = [[0,     0,     0],
     [1.0/2, 0,     0],
     [1.0/2, 1.0, 1.0]
    ]

M = np.array(M)

#Number of pages
N = 3

page_rank_0 = [1/float(N) for i in range(N)]

for j in range(N):
    #for each node in the graph identify all of the inbound Nodes represented
    #as rows in teh
