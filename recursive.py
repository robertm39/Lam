# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:42:56 2017

@author: rober
"""

def lam(x=None):
    return ( lam if x == None else ( lambda l=None: x if l == None else lam(l(x)) if callable(l) else lam(l) ) ) if not callable(x) else lambda y=None: lam(x) if y == None else lam(x(y))