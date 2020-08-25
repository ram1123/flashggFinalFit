# Config file: options for signal fitting

_year = '2017'

signalScriptCfg = {

  # Setup
  'systematics':1, # (0): Use empty systematics dat file. (1): Use generated systematics dat file
  #'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/HHWWgg_15July/GluGluToHHTo_WWgg_qqqq_EFT_Workspaces_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/HHWWgg_9Aug/HHWWgg_v2-6_WorkspaceRadion_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_v2-6_BqrkMinMass_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_v2-6_NoBqrkMinMass_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_v2-6_BqrkPtOrdered_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_v2-6_PtOrderNoBqrk_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_BqrkMinMass_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_BqrkPtOrder_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_ZZ_MinMass_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_ZZ_PtOrder_RadionWorkspace_Hadded',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/combined_WWZZ_Hadded',
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/combined_WWZZ_PtOrder_Hadded',
  # Important: Don't put "/" at the end of inputWSDir.
  #'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/16July/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_NoBqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_BqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_BqrkPtOrdered/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_NoBqrkPtOrdered/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_BqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_BqrkPtOrder/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_ZZMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_ZZPtOrder/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_CombinedMinMass/',
  'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_CombinedPtOrder/',
  'usrprocs':'ggF', # if you want user input production categories
  #'usrprocs':'GluGluToHHTo', # if you want user input production categories
  #Procs will be inferred automatically from filenames
  'cats':'HHWWggTag_2',
  # 'ext':'HHWWgg_v2-3_%s_2CatsSyst'%_year,
  'ext':'HHWWgg_v2-6_%s_ChannelTest'%_year,
  # 'analysis':'stage1_2', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'analysis':'HHWWgg', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'analysis_type':'Res', # For HHWWgg: Res, EFT or NMSSM
  #'analysis_type':'EFT', # For HHWWgg: Res, EFT or NMSSM
  # 'analysis_type':'NMSSM', # For HHWWgg: Res, EFT or NMSSM
  'FinalState':'qqqq', # For HHWWgg. Should choose qqlnu, lnulnu, or qqqq for final state. Will look for this in expected name formats. When we combine channels, and they're defined by tags, we'll add "combined" here and naming format in file will be something like "combined" instead of qqlnu, etc.
  'year':'%s'%_year,
  'beamspot':'3.4',
  'numberOfBins':'320',
  'massPoints':'120,125,130',

  # Use DCB in fit
  'useDCB':0,

  #Photon shape systematics
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB',
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB',
  'scalesGlobal':'NonLinearity:UntaggedTag_0:2,Geant4',
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho',

  # Job submission options
  # 'batch':'IC',
  # 'queue':'hep.q',

  # 'batch':'HTCONDOR',
  # 'queue':'espresso',

  'batch':'', # If you want to run locally just leave these empty
  'queue':'',

  # Mode allows script to carry out single function
  'mode':'std', # Options: [std,calcPhotonSyst,writePhotonSyst,sigFitOnly,packageOnly,sigPlotsOnly]
  ##-- Steps to run:
  # No systematics: std, sigFitOnly, packageOnly, sigPlotsOnly
  # With systematics: std, std
  'verbosity':'1',

}
