# CRAB3 config template for flashgg
# More options available on the twiki :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial

from WMCore.Configuration import Configuration
config = Configuration()
import os

config.section_('General')
config.General.requestName = 'monoHWWlvjj-DR2'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DR_step2_template_cfg.py'
config.JobType.numCores = 4

config.section_('Data')
config.Data.inputDataset = '/monoHWW-lvjj_GENSIM_v1/amassiro-crab_monoHWWlvjj-DR1-9c549b5207abdfb5ae0876b07ca1f88d/USER'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'phys03'


config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/amassiro/monoHWWlvjj/Publish/DR2/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ["T2_CH_CERN"]


