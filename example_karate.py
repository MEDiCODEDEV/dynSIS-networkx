#!/usr/bin/env python
# ! ## File: example_karate.py
# ! Example of using dynSIS with Karate Club network.
# ! ## See README.md for more information and use
# !-----------------------------------------------------------------------------
# ! SIS epidemic model algorithm based on the article "Simulation of Markovian epidemic models on large networks"
# ! Copyright (C) 2016 Wesley Cota, Silvio C. Ferreira
# ! 
# ! Please cite the above cited paper as reference to our code.
# ! 
# !    This program is free software: you can redistribute it and/or modify
# !    it under the terms of the GNU General Public License as published by
# !    the Free Software Foundation, either version 3 of the License, or
# !    (at your option) any later version.
# !
# !    This program is distributed in the hope that it will be useful,
# !    but WITHOUT ANY WARRANTY; without even the implied warranty of
# !    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# !    GNU General Public License for more details.
# !
# !    You should have received a copy of the GNU General Public License
# !    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# !-----------------------------------------------------------------------------
# ! Author    : Wesley Cota
# ! Email     : wesley.cota@ufv.br
# ! Date      : October 2016
# !-----------------------------------------------------------------------------
# ! See README.md for more details
# ! This code is available at <https://github.com/wcota/dynSIS-networkx>
# ! For performance, see <https://github.com/wcota/dynSIS> (Fortran implementation)
# ! For pure Python, see <https://github.com/wcota/dynSIS-py>

import networkx as nx
import dynSIS
import sys

if len(sys.argv) < 1:
    print('You must enter output name as argument!')
    exit()

fnOutput = sys.argv[1]

G=nx.karate_club_graph()

dynp_sam = int(input('How much dynamics samples? '))
dynp_lb = float(input('Value of infection rate lambda (mu is defined as equal to 1) '))
dynp_tmax = int(input('Maximum time steps (it stops if the absorbing state is reached) '))
dynp_pINI = float(input('Fraction of infected vertices on the network as initial condition (is random to each sample) '))
        
# Run dynamics
dynSIS.dyn_run(G, fnOutput, dynp_sam, dynp_lb, dynp_tmax, dynp_pINI)
