# -*- coding: utf-8 -*-
"""

@author: Neha
"""
import itertools

def algo1():
    """This function does Algorithm 1 in the paper.

    Args:
        D: The data. 

    Returns:
        MG: Matched groups from all iterations. 

    """    

    
    return

def algo2_GroupedMR():
    # stuff...
    
    return


#TODO: split steps into separate tiny functions for more unittests
#TODO: validate function input.
def algo3GenerateNewActiveSets(s, delta):
    """This function does Algorithm 3 in the paper.

    Args:
        s: A newly dropped set of size k. Stored as a set with 1 tuple of ints. 
        delta: the set of previously processed sets. Previously processed sets 
        are all stored as tuble objects, so this is a set of tuples.

    Returns:
        Z, the new active sets. Stored as set of tuples.

    """
    # TODO: explore variable names. I don't usually use _ but wanted to match 
    # paper notation.
    
    Z = set()
    k = len(list(s)[0])
    set_s = set(list(s)[0])
    
    # Step 3: delta_k is all subsets of delta that are size k, and s. 
    subsets_size_k = set()
    for prev_processed_tup in delta:
        if len(prev_processed_tup) == k:
            subsets_size_k.add(prev_processed_tup)
    delta_k = subsets_size_k.union(s)
        
    # Step 4: rho is all the covariates contained in sets in delta_k
    rho = set()
    for tup in delta_k:
        for i in tup:
            rho.add(i)
                
    # Step 5: s_e is the support of covariate e in delta_k, for covars in rho
    # TODO: combine this with above loop, calculating rho, for time efficiency.
    s_e = dict()
    for e in rho:
        s_e[e] = 0
        for tup in delta_k:
            if e in tup:
                s_e[e] += 1
    
    # Step 6: omega is all the covariates not in s that have enough support
    dict_covars_eno = dict((key, val) for key, val in s_e.items() if val >= k) 
    omega = set(dict_covars_eno.keys())
    omega = omega.difference(set_s)
       
    # Step 7: do all covariates in S have enough support in delta_k?
    # TODO: confirm this step is right. 
    for e,support_e in s_e.items():
        if e in s and support_e < k:
            return Z
        
    # Step 8
    for alpha in omega:
        # Step 9
        r = set_s.union(set([alpha]))
        
        # Step 10: Get all subsets of size k in r, check if belong in delta_k
        subsets_size_k = set(list(itertools.combinations(r, k)))
        allin = True
        for subset in subsets_size_k:
            if subset not in delta_k:
                allin = False
                break
            
        if allin == True:
            # Step 11: Add r to Z
            Z.add(tuple(r))
    
    return Z