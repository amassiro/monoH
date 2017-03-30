# CRAB3 config template for flashgg
# More options available on the twiki :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial

from WMCore.Configuration import Configuration
config = Configuration()
import os

config.section_('General')
config.General.requestName = 'monoHWWlvjj-SIM'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SIM_template_cfg.py'

config.section_('Data')
#config.Data.inputDataset = '/RSGravToGG_kMpl-001_M-750_TuneCUEP8M1_13TeV-pythia8_magnetOffBS0T_AODSIM_v3/amassiro-crab_monoHWWlvjj-54137679aec40900410ea308c9544bad/USER'
#config.Data.inputDataset = '/monoHWW-lvjj_GEN_v0/amassiro-crab_monoHWWlvjj-54137679aec40900410ea308c9544bad/USER'
config.Data.inputDataset = '/monoHWW-lvjj_GEN_v1/amassiro-crab_monoHWWlvjj-54137679aec40900410ea308c9544bad/USER'

config.Data.inputDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'monoHWWlvjj-TEST'


config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100
#config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDBS = 'phys03'
#config.Data.outputDatasetTag = 'RSGravToGG_kMpl-02_M-750_TuneCUEP8M1_13TeV-pythia8_magnetOffBS0T_74X_mcRun2_0T_v0_MiniAODSIM'
config.Data.outLFNDirBase = '/store/user/amassiro/monoHWWlvjj/Publish/SIM/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_IT_MIB'
config.Site.whitelist = ["T2_CH_CERN"]
#config.Site.blacklist = ["T2_UK_London_Brunel","T1_US_FNAL","T2_US_MIT"]


## config.Data.allowNonValidInputDataset=True


