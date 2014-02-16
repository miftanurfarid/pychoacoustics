# -*- coding: utf-8 -*-
from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, unicode_literals
#from PyQt4 import QtGui, QtCore
#from PyQt4.QtGui import QApplication
import random, sys
from .._version_info import*
from pychoacoustics.sndlib import*
                                                                                         

def initialize_sig_detect(prm):
    exp_name = "Demo Signal Detection"
    prm["experimentsChoices"].append(exp_name)
    prm[exp_name] = {}
    prm[exp_name]["paradigmChoices"] = ["Constant 1-Interval 2-Alternatives"]

    prm[exp_name]["opts"] = ["hasFeedback"]

    prm[exp_name]["buttonLabels"] = ["Yes", "No"]
    prm[exp_name]['defaultNIntervals'] = 1
    prm[exp_name]['defaultNAlternatives'] = 2
    
    prm[exp_name]["execString"] = "sig_detect"
    prm[exp_name]["version"] = __name__ + ' ' + pychoacoustics_version + ' ' + pychoacoustics_builddate
    #prm[exp_name]["version"] = __name__ + ' ' + labexp_version + ' ' + labexp_builddate
    
    return prm

def select_default_parameters_sig_detect(parent, par):
   
    field = []
    fieldLabel = []
    chooser = []
    chooserLabel = []
    chooserOptions = []

    fieldLabel.append(parent.tr("Frequency (Hz)"))
    field.append(1000)
    
    
    fieldLabel.append(parent.tr("Duration (ms)"))
    field.append(2)
    
    
    fieldLabel.append(parent.tr("Ramps (ms)"))
    field.append(4)

    fieldLabel.append(parent.tr("Level (dB SPL)"))
    field.append(40)
    

    chooserOptions.append([parent.tr("Right"), parent.tr("Left"), parent.tr("Both")])
    chooserLabel.append(parent.tr("Channel:"))
    chooser.append(parent.tr("Both"))
        
    

    prm = {}
    prm['field'] = field
    prm['fieldLabel'] = fieldLabel
    prm['chooser'] = chooser
    prm['chooserLabel'] = chooserLabel
    prm['chooserOptions'] =  chooserOptions

    return prm


def doTrial_sig_detect(parent):
  
    currBlock = 'b'+ str(parent.prm['currentBlock'])
    if parent.prm['startOfBlock'] == True:
        parent.prm['additional_parameters_to_write'] = {}
        parent.prm['additional_parameters_to_write'][0] = [] #chord frequencies
        parent.prm['additional_parameters_to_write'][1] = 0  #chord component number
        parent.prm['additional_parameters_to_write'][2] = 0 #probeFreq 
        parent.prm['additional_parameters_to_write'][3] = []##phases
        parent.writeResultsHeader('log')
        parent.prm['conditions'] = ["Yes","No"]

    parent.currentCondition = random.choice(parent.prm['conditions'])
    if parent.currentCondition == 'Yes':
        parent.correctButton = 1
    elif parent.currentCondition == 'No':
        parent.correctButton = 2

                

    freq    = parent.prm[currBlock]['field'][parent.prm['fieldLabel'].index("Frequency (Hz)")]
    dur     = parent.prm[currBlock]['field'][parent.prm['fieldLabel'].index("Duration (ms)")]
    ramps   = parent.prm[currBlock]['field'][parent.prm['fieldLabel'].index("Ramps (ms)")]
    lev     = parent.prm[currBlock]['field'][parent.prm['fieldLabel'].index("Level (dB SPL)")]
    phase   = 0
    channel = parent.prm[currBlock]['chooser'][parent.prm['chooserLabel'].index(parent.tr("Channel:"))]
   

    if parent.currentCondition == 'No':
        lev = -200
    sig = pureTone(freq, phase, lev, dur, ramps, channel, parent.prm['sampRate'], parent.prm['maxLevel'])

 
    parent.playSequentialIntervals([sig])
   
