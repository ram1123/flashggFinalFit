#commands to send to the monolithic runFinalFits.sh script
from os import system

justPrint=False
#justPrint=True
isSubmitted = False
#isSubmitted = True
phoSystOnly = False
#phoSystOnly = True
sigFitOnly = False
#sigFitOnly = True
#sigPlotsOnly = False
sigPlotsOnly = True
print 'About to run signal scripts'
print 'isSubmitted = %s, phoSystOnly = %s, sigFitOnly = %s, sigPlotsOnly = %s'%(str(isSubmitted), str(phoSystOnly), str(sigFitOnly), str(sigPlotsOnly))

#setup files 
#ext          = 'fullStage1Test'
ext          = 'fullStage1Test_DCB'
print 'ext = %s'%ext
#baseFilePath  = '/vols/cms/es811/FinalFits/ws_%s/'%ext
baseFilePath  = '/vols/cms/es811/FinalFits/ws_fullStage1Test/'
fileNames     = ['output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_GE1J.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_150_250_0J.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_0_150.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VH2JET.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3VETO.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_VBFTOPO_JET3.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_REST.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_WH2HQQ_PTJET1_GT200.root','output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLNU_PTV_GT250.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M123_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M124_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M126_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M127_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_0J.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_GT200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_60_120.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_120_200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_1J_PTH_0_60.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_60_120.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_120_200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_0_60.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3VETO.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_VBFTOPO_JET3.root','output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8_GG2H_GE2J_PTH_GT200.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M120_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M123_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M124_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M126_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_PTJET1_GT200.root','output_VBFHToGG_M127_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_REST.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VH2JET.root','output_VBFHToGG_M130_13TeV_amcatnlo_pythia8_VBF_VBFTOPO_JET3VETO.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M123_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M124_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M126_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M127_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_PTJET1_GT200.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_GT250.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_GE1J.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_150_250_0J.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_QQ2HLL_PTV_0_150.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VH2JET.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3VETO.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_VBFTOPO_JET3.root','output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8_ZH2HQQ_REST.root']
fullFileNames = '' 
for fileName in fileNames: fullFileNames += baseFilePath+fileName+','
fullFileNames = fullFileNames[:-1]
#print 'fileNames = %s'%fullFileNames

#define processes and categories
procs         = ''
for fileName in fileNames: 
  if 'M125' not in fileName: continue
  procs += fileName.split('pythia8_')[1].split('.root')[0]
  procs += ','
procs = procs[:-1]
cats          = 'RECO_0J,RECO_1J_PTH_0_60,RECO_1J_PTH_60_120,RECO_1J_PTH_120_200,RECO_1J_PTH_GT200,RECO_GE2J_PTH_0_60,RECO_GE2J_PTH_60_120,RECO_GE2J_PTH_120_200,RECO_GE2J_PTH_GT200,RECO_VBFTOPO_JET3VETO,RECO_VBFTOPO_JET3,RECO_VH2JET,RECO_0LEP_PTV_0_150,RECO_0LEP_PTV_150_250_0J,RECO_0LEP_PTV_150_250_GE1J,RECO_0LEP_PTV_GT250,RECO_1LEP_PTV_0_150,RECO_1LEP_PTV_150_250_0J,RECO_1LEP_PTV_150_250_GE1J,RECO_1LEP_PTV_GT250,RECO_2LEP_PTV_0_150,RECO_2LEP_PTV_150_250_0J,RECO_2LEP_PTV_150_250_GE1J,RECO_2LEP_PTV_GT250,RECO_TTH_LEP,RECO_TTH_HAD'
print 'with processes: %s'%procs
print 'and categories: %s'%cats

#misc config
lumi          = '35.9'
batch         = 'IC'
queue         = 'hep.q'
beamspot      = '3.4'
nBins         = '320'
print 'lumi %s'%lumi
print 'batch %s'%batch
print 'queue %s'%queue
print 'beamspot %s'%beamspot
print 'nBins %s'%nBins

#photon shape systematics
scales        = 'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB'
scalesCorr    = 'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB'
scalesGlobal  = 'NonLinearity:UntaggedTag_0:2,Geant4'
smears        = 'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho'
#print 'scales %s'%scales
#print 'scalesCorr %s'%scalesCorr
#print 'scalesGlobal %s'%scalesGlobal
#print 'smears %s'%smears

#masses to be considered
masses        = '120,123,124,125,126,127,130'
massLow       = '120'
massHigh      = '130'
print 'masses %s'%masses

theCommand = ''
if isSubmitted:
  theCommand += ('cd /vols/build/cms/es811/FreshStart/STXSstage1/CMSSW_7_4_7/src/flashggFinalFit/Signal\n')
  theCommand += ('eval `scramv1 runtime -sh`\n')
theCommand += './runSignalScripts.sh -i '+fullFileNames+' -p '+procs+' -f '+cats+' --ext '+ext+' --intLumi '+lumi+' --batch '+batch+' --massList '+masses+' --bs '+beamspot
#theCommand += ' --smears '+smears+' --scales '+scales+' --scalesCorr '+scalesCorr+' --scalesGlobal '+scalesGlobal+' --useSSF 1 --useDCB_1G 0'
theCommand += ' --smears '+smears+' --scales '+scales+' --scalesCorr '+scalesCorr+' --scalesGlobal '+scalesGlobal+' --useSSF 1 --useDCB_1G 1'
if phoSystOnly: theCommand += ' --calcPhoSystOnly'
elif sigFitOnly: theCommand += ' --sigFitOnly'
elif sigPlotsOnly: theCommand += ' --sigPlotsOnly'
if not justPrint: system(theCommand)
else: print '\n\n%s'%theCommand
