#!/bin/bash

## Signal 

# FTest 
./bin/signalFTest -i /afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/24Oct/X250_HHWWgg_qqlnu.root -p ggF -f SL -o /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/24Oct_HHWWgg --datfilename /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/dat/24Oct_HHWWgg_dat.dat

# Produce photon systematics dat file 
# skipping 

# Create 120 and 130 GeV points 
python shiftHiggsDatasets.py # with correct input and ouput path, etc. in python file 

# SignalFit 
./bin/SignalFit -i /afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/24Oct/X_signal_250_120_HHWWgg_qqlnu.root,/afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/24Oct/X_signal_250_125_HHWWgg_qqlnu.root,/afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/24Oct/X_signal_250_130_HHWWgg_qqlnu.root -p ggF -f SL -d dat/24Oct_HHWWgg_dat.dat -s empty.dat --procs ggF --changeIntLumi 42.17

# Plot 
./bin/makeParametricSignalModelPlots -i CMS-HGG_sigfit.root  -o HHWWgg_test_fit -p ggF -f SL


# datacard attempt 

./makeParametricModelDatacardFLASHgg.py -i /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/CMS-HGG_sigfit.root  -o 24Oct_HHWWgg_datacard -p ggF -c SL --photonCatScales /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/empty.dat --isMultiPdf --intLumi 42.17
# gives output 