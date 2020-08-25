# Config file: options for background fitting

_year = '2017'

backgroundScriptCfg = {

  # Setup
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/HHWWgg_10July/HHWWgg_2017_Data_Trees_Hadded_Combined',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_2017_DataFHMinMass_Workspace_Hadded_Combined',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August12/HHWWgg_2017_DataFHPtOrder_Workspace_Hadded_Combined',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_2017_DataMinMass_Workspaces_Hadded_Combined',
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/August20/HHWWgg_v2-6_2017_DataPtOrdered_Workspaces_Hadded_Combined',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_NoBqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_BqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_BqrkPtOrdered/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/20August_NoBqrkPtOrdered/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_BqrkMinMass/',
  # 'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/22August_BqrkPtOrder/',
  'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/test2/',
  # When we don't have signal model then put InSignalFitWSFile = "". Else it will
  # try to find the signal root file present in the signal directory.
  # What string to put?
  # If RootFileName: Signal/outdir_HHWWgg_v2-6_2017_ChannelTest_X550_HHWWgg_qqqq/CMS-HGG_sigfit_HHWWgg_v2-6_2017_ChannelTest_X550_HHWWgg_qqqq.root
  # then put InSignalFitWSFile = "X550_HHWWgg_qqqq"
  # 'InSignalFitWSFile':'',
  'InSignalFitWSFile':'X550_HHWWgg_qqqq',
  'massStep':20,
  #Procs will be inferred automatically from filenames
  'cats':'HHWWggTag_2',
  # 'ext':'HHWWgg_v2-3_2017_2CatsSyst',
  # 'ext':'HHWWgg_v2-6_2017_Synch',
  'ext':'HHWWgg_v2-6_%s_ChannelTest'%_year,
  'year':'2017',
  'unblind':0,

  # Job submission options
  'batch':'HTCONDOR',
  'queue':'espresso',

  'analysis':'HHWWgg',

  # Mode allows script to carry out single function
  'mode':'std', # Options: [std,fTestOnly,bkgPlotsOnly]

}
