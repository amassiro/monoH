# CRAB3 config template for flashgg
# More options available on the twiki :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial

from WMCore.Configuration import Configuration
config = Configuration()
import os

config.section_('General')
config.General.requestName = 'monoHWWlvjj'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'do_Mock_Publish.py'

config.section_('Data')
#config.Data.inputDataset = '/RSGravToGG_kMpl-02_M-750_TuneCUEP8M1_13TeV-pythia8/RunIISummer15GS-magnetOffBS0T_MCRUN2_71_V1-v1/GEN-SIM'
#config.Data.inputDBS = 'global'
#config.Data.outputPrimaryDataset = 'monoHWW-lvjj_GEN_v0'
config.Data.outputPrimaryDataset = 'monoHWW-lvjj_GEN_v2'
config.Data.userInputFiles = [
  '/store/user/amassiro/monoHWWlvjj/GEN/EXO-RunIISummer15wmLHES-00000.root',
  ]

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDBS = 'phys03'
#config.Data.outputDatasetTag = 'RSGravToGG_kMpl-02_M-750_TuneCUEP8M1_13TeV-pythia8_magnetOffBS0T_74X_mcRun2_0T_v0_MiniAODSIM'
config.Data.outLFNDirBase = '/store/user/amassiro/monoHWWlvjj/Publish/GEN/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_IT_MIB'
config.Site.whitelist = ["T2_CH_CERN"]
#config.Site.blacklist = ["T2_UK_London_Brunel","T1_US_FNAL","T2_US_MIT"]


## config.Data.allowNonValidInputDataset=True


