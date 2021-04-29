# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:27:19 2020
@author: JOSE DAVID ARANGO JARAMILLO
"""

"*********************************************************************"
"IMPORTING LIBRARIES"
import math as mt
import numpy as np
import pandas as pd

"*********************************************************************"

"*********************************************************************"
"DEFINING DATAFRAMES"
"1. TABLE C.3.5.3-2"
barSize = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18])
diameters = np.array([6.4, 9.5, 12.7, 15.9, 19.1, 22.2, 25.4, 28.7, 32.3, 35.8,
                      43, 57.3])
area = np.array([32, 71, 129, 199, 284, 387, 510, 645, 819, 1006, 1452, 2581])
weight = np.array([0.25, 0.56, 0.994, 1.552, 2.235, 3.042, 3.973, 5.060, 6.404,
                   7.907, 11.380, 20.240])
rows = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
tbC_3532 = pd.DataFrame({"BarSize": barSize, "Diameters[mm]": diameters,
                         "Area[mm2]": area, "Weight[kg/m]": weight},
                        index=rows)
"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 1"
"NAME: Verification of condition of f'c, located on C.12.1.2"
"DESCRIPTION: Verification of condition of f'c, located on C.12.1.2"
"RETURN: True if the condition was satisfied or False if it isn't"
"VARIABLES: -fc: Concrete Compressive Strength [MPa]"
"CODE:"


def check1(fc):
    constant = 8.3  # MPa
    calculation = mt.sqrt(fc)  # MPa
    if calculation > constant:  # Condition located on C.12.1.2
        return False  # Don't satisfied
        print("The condition C.12.1.2 weren't satisfied")
    else:
        return True  # Satisfied
        print("The condition C.12.1.2 were satisfied")


"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 2"
"NAME: Calculation of diameter based on bar size and table C.3.5.3-2"
"DESCRIPTION: Based on the bar size the function select the diameter"
"RETURN: Diameter on milimeters of the bar size"
"VARIABLES: -rebar: Integer between 2-18 which means de rebar size[in]"
"CODE:"


def rebarDiameter(rebar, df=tbC_3532):
    diameter = df.loc[df['BarSize'] == rebar, ['Diameters[mm]']]
    return diameter.iloc[0, 0]


"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 3"
"NAME: Select the indicated formula located on  C.12.2.2"
"DESCRIPTION: Analice the entry parameters to decide which formula"
"             we have to used (formula on C.12.2.2)"
"RETURN: Integer between 1-4 depends on the selected case"
"VARIABLES: -rebar: Integer between 2-18 which means de rebar size[in]"
"           -sep: Horizontal Spacing of the rebars [m]"
"           -rec: Clear cover to face of bar [m]"
"           -confLd: Confinement bars along development length? [T o F]"
"CODE:"


def formulaCase(rebar, sep, rec, confLd):
    diameter = rebarDiameter(rebar) / 1000  # Meters
    diameter2 = diameter * 2
    result = 0
    # Case 1
    if sep > diameter and rec > diameter and confLd == True and rebar <= 6:
        result = 1
    if sep > diameter2 and rec > diameter and rebar <= 6:
        result = 1
    # Case 2
    if sep > diameter and rec > diameter and confLd == True and rebar > 6:
        result = 2
    if sep > diameter2 and rec > diameter and rebar > 6:
        result = 2
    # Case 3
    if rebar <= 6 and result == 0:
        result = 3
    # Case 4
    if rebar > 6 and result == 0:
        result = 4
    return result


"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 4"
"NAME: Select the constants for the calcution located on C.12.2.4"
"DESCRIPTION: Depends on the situation, choose the adecuated constant"
"             based on C.12.2.4"
"RETURN: Data frame whit 2 columns 1. ID 2. Value of the constant"
"VARIABLES: -liwe: Integer between 2-18 which means de rebar size[in]"
"           -epoxic: Epoxic coated bars? [True or False]"
"           -hreb: Spacing between upside and downside rebars [m]"
"           -rebar: Integer between 2-18 which means de rebar size[in]"
"           -sep: Horizontal Spacing of the rebars [m]"
"           -rec: Clear cover to face of bar [m]"
"CODE:"


def constants(liwe, epoxic, hreb, rebar, sep, rec):
    cntName = np.array(["phiT", "phiE", "phiS", "lamda"])
    rows = np.array([1, 2, 3, 4])
    cnt = np.ones(4, dtype='float')
    # phiT
    if hreb > 0.3:
        cnt[0] = 1.3
    # phiE
    condAux = 0
    diameter = rebarDiameter(rebar) / 1000  # Meters
    if epoxic == True and rec < (diameter * 3) and sep < (diameter * 6):
        if cnt[0] == 1.3:
            cnt[1] = 1.7 / 1.3
        if cnt[0] == 1:
            cnt[1] = 1.5
        condAux = 1
    if epoxic == True and condAux == 0:
        cnt[1] = 1.2
    # phiS
    if rebar <= 6:
        cnt[2] = 0.8
    # lamda
    if liwe == True:
        cnt[3] = 0.75
    # create the dataframe
    dfCnt = pd.DataFrame({"Constant": cntName, "Value": cnt},
                         index=rows)
    return dfCnt


"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 5"
"NAME: Calculate the development lenght"
"DESCRIPTION: Based on the constants and he indicated formula located"
"             on  C.12.2.2 calculate the lenght"
"RETURN: Float whit the lenght"
"VARIABLES: -liwe: Integer between 2-18 which means de rebar size[in]"
"           -epoxic: Epoxic coated bars? [True or False]"
"           -hreb: Spacing between upside and downside rebars [m]"
"           -rebar: Integer between 2-18 which means de rebar size[in]"
"           -sep: Horizontal Spacing of the rebars [m]"
"           -rec: Clear cover to face of bar [m]"
"CODE:"


def calculation(liwe, epoxic, hreb, rebar, sep, rec, fc, fy, confLd):
    # get the constants separeted
    dfconstants = constants(liwe, epoxic, hreb, rebar, sep, rec)
    df_phiT = dfconstants[dfconstants['Constant'] == 'phiT']
    phiT = float(df_phiT['Value'])
    df_phiE = dfconstants[dfconstants['Constant'] == 'phiE']
    phiE = float(df_phiE['Value'])
    # phiS =  dfconstants[dfconstants['Constant']=='phiS']
    df_lamda = dfconstants[dfconstants['Constant'] == 'lamda']
    lamda = float(df_lamda['Value'])
    # rebar diameter
    diameter = rebarDiameter(rebar) / 1000  # Meters
    # calculate the lenght
    formula_number = formulaCase(rebar, sep, rec, confLd)
    if formula_number == 1:
        lenght = ((fy * phiT * phiE) / (2.1 * lamda * mt.sqrt(fc))) * diameter
    if formula_number == 2:
        lenght = ((fy * phiT * phiE) / (1.7 * lamda * mt.sqrt(fc))) * diameter
    if formula_number == 3:
        lenght = ((fy * phiT * phiE) / (1.4 * lamda * mt.sqrt(fc))) * diameter
    if formula_number == 4:
        lenght = ((fy * phiT * phiE) / (1.1 * lamda * mt.sqrt(fc))) * diameter
    return lenght


"*********************************************************************"

"*********************************************************************"
"FUNCTION No: 6"
"NAME: Calculate the table of development lenghts"
"DESCRIPTION: Based on function calculation, create a table with the"
"             Development Lenght for each rebar in table tbC_3532"
"RETURN: Data frame with Development Lenghts "
"VARIABLES: -liwe: Integer between 2-18 which means de rebar size[in]"
"           -epoxic: Epoxic coated bars? [True or False]"
"           -hreb: Spacing between upside and downside rebars [m]"
"           -sep: Horizontal Spacing of the rebars [m]"
"           -rec: Clear cover to face of bar [m]"
"CODE:"


def ld_table(liwe, epoxic, hreb, sep, rec, fc, fy, confLd, df=tbC_3532):
    # define the rebars
    rebar_table = df['BarSize']
    # crete the Development Lenght for each rebar
    arr_ld = []
    for rebar in rebar_table:
        ld_rebar = round(calculation(liwe, epoxic, hreb, rebar, sep, rec, fc, fy, confLd), 2)
        arr_ld.append(ld_rebar)
    # create a data frame with the results
    df_ld_table = pd.DataFrame({"Rebar": rebar_table, "Development Lenght [m]": arr_ld})
    df_ld_table = df_ld_table.to_string(index=False)
    return df_ld_table