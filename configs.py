#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:25:58 2021
Provides a few Objects to play with and a function simplifing placing an object
onto a simulation field.

@author: dkappe
"""
import numpy as np


def insert_pattern(base, pattern, offset=None): #optional!
    """
    Takes a base simulation field and places a given pattern with an offset
    onto it. When offset is None, the object is placed into the middle

    Parameters
    ----------
    base : numpy.ndarray
        The base simulation field. Can already hold objects.
    pattern : numpy.ndarray
        The pattern to be placed. Should fit onto the simulation field
    offset : (offset_x, offset_y), optional
        offset in the x and y directions, from the middle. The default is None.

    Raises
    ------
    ValueError
        Error is raised, if the pattern does not fit onto the simulation field.

    Returns
    -------
    field : TYPE
        The simulation field with the pattern placed.
    """
    #pass
    pattern = np.array(pattern)
    new_field_config = base
    if offset == None:
        offset = (0,0)
    #neue pos mit offset
    pos = (np.int(new_field_config.shape[0] / 2) + offset[0], np.int(new_field_config.shape[1] / 2 + offset[1]))
    #überschreibe new_field_coinfig mit pattern an gewünschter pos
    new_field_config[pos[0]:pos[0] + pattern.shape[0], pos[1]:pos[1] + pattern.shape[1]] = pattern

    return new_field_config

BLINKER = [[1, 1, 1]]

BEACON = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

PULSER = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

GOSPER = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

FULLARAY = np.ones((99,16), dtype=int)