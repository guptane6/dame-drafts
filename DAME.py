# -*- coding: utf-8 -*-
"""
DAME Code

This package implements the code in the paper "Interpretable Almost-Exact 
Matching For Causual Inference" (Liu, Dieng, Roy, Rudin, Volfovsky) 
TODO: Insert Arxiv Link Here

Example:
    TODO: Insert example here
    
    $ python main.py TODO: commandlines....
        

@author: Neha
"""

import argparse
import data_cleaning
import dame_algorithms


def main():
    
    # parse commandline arguments.
    
    parser = argparse.ArgumentParser(description="Implement the matching \
                                     method from the paper, Interpretable \
                                     Almost-Exact Matching for Causal \
                                     Inference")

    parser.add_argument('--valid_group_by', nargs='?', type=str, 
                        const='bit-vector', 
                        help='enter bit-vector or sql (default: bit-vector)')
    

    parser.add_argument('--file_name', nargs=1, type=argparse.FileType('r'),
                        help='enter name of input file')
    
    # TODO: add option for accepting a dataframe
    
    args = parser.parse_args()
    print(args)
    
    # call functions to do things.
    data_cleaning.process_input_file()
    dame_algorithms.algo1()
    
    
    
if __name__ == "__main__":
    main()