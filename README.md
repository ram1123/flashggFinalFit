# HHWWgg Flashgg Final Fit 

Contacts: 
- Abraham Tishelman-Charny - abraham.tishelman.charny@cern.ch 
- Badder Marzocchi - badder.marzocchi@cern.ch
- Toyoko Orimoto - Toyoko.Orimoto@cern.ch 

Presentations: 
- [21 October 2019 Analysis Status](https://indico.cern.ch/event/847927/contributions/3606888/attachments/1930081/3196452/HH_WWgg_Analysis_Status_21_October_2019.pdf)
- [11 November 2019 Analysis Update](https://indico.cern.ch/event/847923/contributions/3632148/attachments/1942588/3221820/HH_WWgg_Analysis_Update_11_November_2019_2.pdf)

Repositories:
- [HHWWgg Development](https://github.com/atishelmanch/flashgg/tree/HHWWgg_dev)
- [HHWWgg MicroAOD Production](https://github.com/atishelmanch/flashgg/tree/HHWWgg_Crab)
- [HHWWgg Private MC Production](https://github.com/NEUAnalyses/HH_WWgg/tree/HHWWgg_PrivateMC)

This repository contains flashgg final fit scripts and instructions specific to the HHWWgg analysis. 

# HHWWgg_v2-2

This section describes instructions specific to the HHWWgg_v2-2 tag. The HHWWgg_v2-2 tag is used to mark the point in the anlaysis where the 95% CL limit on the HH cross section was placed on the 250 GeV semileptonically decaying Radion using the HHWWgg tagger plugin with workspaceStd.py WITHOUT systematics. The purpose of the tag is to document everything used to obtain this *very* preliminary result.

## Signal Model

These are the commands to create a signal model with Signal directory using the X250, qqlnu output from the HHWWgg_v2-2 tag of HHWWgg_dev.

Note: This requires that you have the proper user defined paths in flashggFinalFit/Signal/HHWWgg_Signal_Fit_Steps.sh, specifically for the variables 
fggfinalfitDirec (default:"/afs/cern.ch/work/a/atishelm/8Octflashggfinalfit/CMSSW_7_4_7/src/flashggFinalFit/")

and to use combine:

combineDir (default:"/afs/cern.ch/work/a/atishelm/4NovCombineUpdated/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit")

```
cd Signal
cmsenv
make
. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -f # ftest 
. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -k # signal fit  
. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -p # plot signal (crashes but produces pdf) 
. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -d # produce datacard
```

## Background Model

These are the commands to create a background model with Background directory using the X250, qqlnu output from the HHWWgg_v2-2 tag of HHWWgg_dev:

```
cd Background 
cmsenv 
make
/eos/user/a/atishelm/ntuples/HHWWgg_v2-2/Data.root
```

. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -c # run combine with background model in Background directory 

## Combine 

Note: In order to run this you need combine built with CMSSW_10_2_13 in a separate repository, the path of which is defined by the variable combineDir in the script
flashggFinalFit/Signal/HHWWgg_Signal_Fit_Steps.sh 

To run combine with the previously created signal and background models:

```
cd Signal
cmsenv
make
. HHWWgg_Signal_Fit_Steps.sh -i /eos/user/a/atishelm/ntuples/HHWWgg_v2-2/X250_HHWWgg_qqlnu.root -r HHWWgg_v2-2_X250_qqlnu -c # run combine with this signal model, and background model existing in Background directory
```

## Plot

To plot the limit, after copying the proper files to the Plots/FinalResults repository (this needs to be updated to be more flexible code, currently hardcoded):

```
cd flashggFinalFit/Plots/FinalResults
cmsenv
make
python plot_limits.py
```

If everything worked properly, there should be an output file called UpperLimit.pdf. 