# Config file: options for background fitting

_year = '2017'

_Channel = "ZZ"

backgroundScriptCfg = {

  'analysis':'HH%sgg'%_Channel,
  # Setup
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/November05_Rename/2017',
  # 'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/September29/HHWWgg_v2_6_2016Data_PhoPt_flashgg5_Workspace_Hadded_Combined',
  'website':'/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit_CMSSW106X/Dec3/%s_%s'%(_Channel,_year),

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
  'year':'%s_%s_FH'%(_year,_Channel),
  'unblind':0,

  # Job submission options
  'batch':'HTCONDOR',
  'queue':'espresso',


  # Mode allows script to carry out single function
  'mode':'fTestOnly', # Options: [std,fTestOnly,bkgPlotsOnly]

}
