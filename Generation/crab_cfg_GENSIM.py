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
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GENSIM_template_cfg.py'
config.JobType.eventsPerLumi = 10000

config.section_('Data')
config.Data.outputPrimaryDataset = 'monoHWW-lvjj_GENSIM_v1'

config.Data.splitting = 'FileBased'
config.Data.totalUnits = 50000

config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/amassiro/monoHWWlvjj/Publish/GENSIM/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
config.Site.whitelist = ["T2_CH_CERN"]


