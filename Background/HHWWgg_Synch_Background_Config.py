# Config file: options for background fitting

_year = '2017'

backgroundScriptCfg = {

  # Setup
  'inputWSDir':'/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/HHWWgg_10July/HHWWgg_2017_Data_Trees_Hadded_Combined',
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
