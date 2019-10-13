#!/bin/bash

# FTest 
./bin/signalFTest -i /afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/test2/X250_HHWWgg_qqlnu.root -p ggF -f SL -o /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/HHWWgg_Test --datfilename /afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/Signal/dat/HHWWgg_Test_dat.dat

# SignalFit 
./bin/SignalFit -i /afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/test2/X_signal_250_120_HHWWgg_qqlnu.root,/afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/test2/X_signal_250_125_HHWWgg_qqlnu.root,/afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/fggfinalfit_files/test2/X_signal_250_130_HHWWgg_qqlnu.root -p ggF -f SL -d dat/HHWWgg_Test_dat.dat -s empty.dat --procs ggF --changeIntLumi 40

# Plot 
./bin/makeParametricSignalModelPlots -i CMS-HGG_sigfit.root  -o HHWWgg_test_fit -p ggF -f SL