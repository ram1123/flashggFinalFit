# Config file: options for background fitting

_year = '2017'

backgroundScriptCfg = {

  # Setup
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/September29/HHWWgg_v2_6_PhoPt200GeV_BTag_2017Data_Workspace_Hadded_Combined',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/September29/HHWWgg_v2_6_2016Data_PhoPt_flashgg5_Workspace_Hadded_Combined',
  'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit/NEW_September29_WW_PhoPt200GeV_Btag_2017/',

  # When we don't have signal model then put InSignalFitWSFile = "". Else it will
  # try to find the signal root file present in the signal directory.
  # What string to put?
  # If RootFileName: Signal/outdir_HHWWgg_v2-6_2017_ChannelTest_X550_HHWWgg_qqqq/CMS-HGG_sigfit_HHWWgg_v2-6_2017_ChannelTest_X550_HHWWgg_qqqq.root
  # then put InSignalFitWSFile = "X550_HHWWgg_qqqq"
  # 'InSignalFitWSFile':'',
  'InSignalFitWSFile':'nodeSM_HHWWgg_qqqq',
  'massStep':1, # put this to high value say 5 for quick run.

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
