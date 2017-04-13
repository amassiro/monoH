# CRAB3 config template for flashgg
# More options available on the twiki :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial

from WMCore.Configuration import Configuration
config = Configuration()
import os

config.section_('General')
config.General.requestName = 'monoHWWlvjj-DR1'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DR_template_cfg.py'
config.JobType.numCores = 4

config.section_('Data')
config.Data.inputDataset = '/monoHWW-lvjj_GENSIM_v1/amassiro-crab_monoHWWlvjj-GENSIM_RAWSIMoutput-e342baf80f9cc97daef57e7513feef17/USER'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1


config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/amassiro/monoHWWlvjj/Publish/DR1/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ["T2_CH_CERN"]


