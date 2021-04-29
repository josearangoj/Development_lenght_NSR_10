# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:27:19 2020

@author: JOSE DAVID ARANGO JARAMILLO
"""

"****************************************************************************"
"EXTERN FILES"
import Functions as fn
"****************************************************************************"

"****************************************************************************"
"IMPORTING LIBRARIES OR MODULES"
import sys #interrumpt the process
"****************************************************************************"

"****************************************************************************"
"PROBLEM CONSTANTS"
table = True #Do you want a table of the differents bar sizes? [True or False]
rebar = 7 #Reinforcing bar size [-]
fc = 28 #Concrete Compressive Strength [MPa]
fy = 420 #Specified yield strength for rebar reinforcement [MPa]
sep = 0.2 #Spacing of the rebars [m]
rec = 0.04 #Clear cover to face of bar [m]
confLd = True #Confinement bars along development length? [True or False]
liwe = False #Lightweight concrete? [True or False]
epoxic = False #Epoxic coated bars? [True or False]
hreb = 0.4 #Spacing between upside and downside rebars [m]
"****************************************************************************"

"****************************************************************************"
"PROCESS No: 1"
"FUNTION USED: check1"
"VARIABLES: - fc: Concrete Compressive Strength [MPa]"
"RESULT: True or false if the condition was satisfied or not"
"CODE:"
check1 = fn.check1(fc)
if check1 == False:
    sys.exit()
"****************************************************************************"

"****************************************************************************"
"PROCESS No: 2"
"FUNTION USED: check1"
"VARIABLES: - fc: Concrete Compressive Strength [MPa]"
"RESULT: True or false if the condition was satisfied or not"
"CODE:"
result = round(fn.calculation(liwe,epoxic,hreb,rebar,sep,rec,fc,fy,confLd),2)
print('The development lenght for a rebar No ' + str(rebar) + ' is: ' + 
      str(result) + ' meters')
if table == True:
    ld_table = fn.ld_table(liwe,epoxic,hreb,sep,rec,fc,fy,confLd)
    print(ld_table)
"****************************************************************************"