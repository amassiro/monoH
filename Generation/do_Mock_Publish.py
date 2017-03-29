import FWCore.ParameterSet.Config as cms

process = cms.Process("MINIAODSIM")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                  '/store/user/amassiro/test.root'
                                  ))

# Output definition
process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         outputCommands = cms.untracked.vstring("keep *"),
                                         fileName = cms.untracked.string("EXO-RunIISummer15wmLHES-00000.root")
)

process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)
process.schedule = cms.Schedule(process.MINIAODSIMoutput_step)
