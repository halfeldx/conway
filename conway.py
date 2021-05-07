#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:31:37 2021
Provides the ConwayBase class and an implementation of said class.

@author: dkappe
"""

from abc import ABC, abstractclassmethod
import numpy as np


class ConwayBase(ABC):
    """
    ConwayBase is an abstract base class with all of the Game's logic missing.
    Any class based on it has to implement the methods:
     * update_field()
     * show_field()

    Parameters
    ----------
    start_field : numpy.ndarray
        Simulation field at the start of the Game.
    
    Properties
    ----------
    start_field: numpy.ndarray
        Simulation field at the start of the Game.
    current_field: numpy.ndarray
        Current state of the Simulation field.
    size: int
        Size of the start_field numpy.ndarray
    shape: (int, int)
        Shape of the start_field numpy.ndarray
    is_empty: bool
        Checks whether there are any points left on the simulation field.
    """

    def __init__(self, start_field: np.ndarray):
        self.start_field = np.array(start_field, dtype=int)
        self.reset_field()  # current field = start field
        self.size = self.current_field.size
        self.shape = self.current_field.shape

    @abstractclassmethod
    def update_field(self):
        """
        Class method providing the Game logic. Here the current_field has to be
        updated for the next frame.
        """

        pass

    @abstractclassmethod
    def show_field(self) -> np.ndarray:
        """
        Class method returning the image to be displayed. The Image can either
        be a 2D numpy array with shape (width, height) or a 3D numpy array with
        shape (width, height, color), where color are RGB values

        Returns
        -------
        numpy.ndarray
            The image to be drawn.

        """
        pass

    def reset_field(self):
        """
        Resets the simulation field to the starting configuration.
        """
        self.current_field = np.array(self.start_field, copy=True, dtype=int)

    @property
    def is_empty(self) -> bool:
        """
        Checks and returns, if current_field has no non-zero values.
        """
        return np.sum(self.current_field) == 0


class Conway(ConwayBase):  # erbt alles aus base-class
    def __init__(self, start_field, border: bool = True):  # ,
        # fade: tuple = (1, 1, 1), gauss_sigma: tuple = (0, 0, 0)):
        super().__init__(start_field)
        start_field.dtype = int
        # pass

    def update_field(self):
        #self.update_field_slow()
        self.update_field_fast(True)
        """

        1. <2 lebende Nachbarn --> stirbt (1->0)
        2. >3 lebende Nachbarn --> stirbt (1->0)
        3. 2/3 lebende Nachbarn --> Zustand bleibt (x->x)
        4. Tote Zelle + 3 lebende Nachbarn --> neues Leben (0->1)

        Regel 1 und 2 werden durch np.zeros_like erledigt

        Returns
        -------

        """


    def update_field_slow(self):
        updated_field = np.zeros_like(self.start_field)
        current_field = self.current_field
        for index in np.ndindex(current_field.shape): #index = (row, column) - iteriert erst über letzte dim (column)
            num_neighbours = self.num_neighbours(index)
            if (current_field[index] == 1 and (num_neighbours == 2 or num_neighbours == 3)) or \
                    (current_field[index] == 0 and num_neighbours == 3):
                updated_field[index] = 1
        self.current_field = updated_field

    def num_neighbours(self, pos):
        return np.sum(self.current_field[pos[0] - 1:pos[0] + 2, pos[1] - 1:pos[1] + 2]) - self.current_field[pos[0], pos[1]]



    def update_field_fast(self, border: np.bool, totalwar=True):
        updated_field = np.zeros_like(self.start_field)
        bordermask = np.zeros_like(self.current_field)
        bordermask[1:-1, 1:-1] = 1
        rolling = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
        # Roll über beide Achsen 0-> in reihe verschoben, 1 -> in spalte verschoben
        roll_arr = [np.roll(np.roll(self.current_field, roll[0], axis=0), roll[1], axis=1) for roll in rolling]
        living_neighbors = sum(roll_arr)
        living = np.logical_or(np.logical_and(np.logical_not(self.current_field), living_neighbors == 3), np.logical_and(self.current_field, np.logical_or(living_neighbors == 2, living_neighbors == 3)))
        updated_field[living] = 1
        if totalwar:
            updated_field[bordermask] = bordermask
        self.current_field = updated_field*bordermask if border else updated_field


    def show_field(self) -> np.ndarray:
        return self.current_field*0xF015A1/sum(self.current_field)




















