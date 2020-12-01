# Config file: options for combine fitting

import sys

mode = sys.argv[1] # datacard or combine
print'mode: ',mode

_year = '2017'
_Channel = "WW"

combineScriptCfg = {

  # Setup
  'analysis':'HHWWgg',
  'analysis_type':'EFT',
  # 'analysis_type':'NMSSM',
  # 'analysis_type':'Res',
  'FinalState':'lnulnu', # for HHWWgg. qqlnu, lnulnu, or qqqq. Will add combined eventually.
  'mode':mode,
  # 'mode':'combine',
  'doSystematics':1, # 0: do not include systematics in datacard. 1: include systematics in datacard
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/November23/HHWWgg_v2_6_PhoPt160GeV_CMSSW105X_2017_SingleHiggs_Bkg_workspace_old_Hadded_4',
  'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit_FixName/2017_SingleHiggs4_%s'%_Channel,
  #Procs will be inferred automatically from filenames
  #'HHWWggCatLabel':'2TotCatsCOMBINEDWithSyst', # for name of combine output files
  'HHWWggCatLabel':'2TotCatsbothcombined',
  'cats':'HHWWggTag_2',
  'ext':'HHWWgg_v2-6_%s_ChannelTest_gg_HHWWgg_lnulnu'%_year,
  'year':'%s_%s_FH'%(_year,_Channel),
  # 'signalProcs':'ggh_X125', # "ggF" for Radion, FOR EFT "GluGluToHHTo"
  # 'signalProcs':'tth_X125', # "ggF" for Radion, FOR EFT "GluGluToHHTo"
  # 'signalProcs':'vbf_X125', # "ggF" for Radion, FOR EFT "GluGluToHHTo"
  'signalProcs':'wzh_X125', # "ggF" for Radion, FOR EFT "GluGluToHHTo"
  # 'signalProcs':'ggF', # "ggF" for Radion, FOR EFT "GluGluToHHTo"

  # Add UE/PS systematics to datacard (only relevant if mode == datacard)
  'doUEPS':0, # should I have this on?

  #Photon shape systematics
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB',
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB',
  'scalesGlobal':'NonLinearity:UntaggedTag_0:2,Geant4',
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho',

  # Job submission options
  # 'batch':'HTCONDOR',
  # 'queue':'workday',

  'batch':'',
  'queue':'',

  'printOnly':0, # For dry-run: print command only

}
