# Config file: options for signal fitting

_year = '2016'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/Workspaces_HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM//Signal/Input/2016/',
  'procs':'ggh', # if auto: inferred automatically from filenames
  'HHWWggLabel':'single_Higgs', 
  'cats':'HHWWggTag_SLDNN_0,HHWWggTag_SLDNN_1,HHWWggTag_SLDNN_2,HHWWggTag_SLDNN_3', # if auto: inferred automatically from (0) workspace
  'ext':'SL_HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_%s_single_Higgs'%_year,
  'analysis':'STXS', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB', # separate nuisance per year
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB', # correlated across years
  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'hep.q'
  #'batch':'condor', # ['condor','SGE','IC','local']
  #'queue':'espresso',

}
