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


M = [[0,     0,     1.0],
     [1.0/2, 0,     0],
     [1.0/2, 1.0,   0]
    ]

M = np.array(M)

#Number of pages
N = 3

#randomization coefficient
BETA = 1.0

#Epsilon for Convergence
EPSILON = 0.0001

#usually 1/N where N is the number of pages
prior_prob = 1


page_rank_prior = np.array([prior_prob for i in range(N)])

page_rank_tmp = np.array([0.0 for i in range(N)])

i_iter = 0

while True:

    i_iter += 1
    for j in range(N):
        #for each node in the graph identify all of the inbound Nodes represented
        #as rows in the M Matrix

        rj_prime = 0.0


        if np.sum(M[j]) > 0:
            ib_links = list(np.array(range(N))[M[j] > 0])
            for i in ib_links:
                # number of out links from node i
                d_i = np.sum(M[:,i] > 0)
                rj_prime += BETA*(page_rank_prior[i]/d_i)

        page_rank_tmp[j] = rj_prime

    S = np.sum(page_rank_tmp)
    page_rank_tmp = page_rank_tmp + (1 - S)/N

    print i_iter
    print page_rank_prior
    print page_rank_tmp



    if np.sum(np.abs(page_rank_tmp - page_rank_prior)) < EPSILON:
        print 'iteration %d page rank vector is'%i_iter, page_rank_tmp
        break

    else:
        page_rank_prior = page_rank_tmp
        page_rank_tmp = np.array([0.0 for i in range(N)])







