# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EXO-RunIISummer15wmLHEGS-00000-fragment.py --fileout file:EXO-RunIISummer15wmLHEGS-00000.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename EXO-RunIISummer15wmLHEGS-00000_1_cfg.py --no_exec -n 51
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')
#process = cms.Process('SIM2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(400)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_14/src/monoH/Generation/EXO-RunIISpring16DR80-00000_step1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/EXO-RunIISummer15wmLHEGS-00000-fragment.py nevts:400'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:EXO-RunIISummer15wmLHEGS-00000.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    #SelectEvents = cms.untracked.PSet(
        #SelectEvents = cms.vstring('generation_step')
    #)
)

#process.LHEoutput = cms.OutputModule("PoolOutputModule",
    #splitLevel = cms.untracked.int32(0),
    #eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    #outputCommands = process.LHEEventContent.outputCommands,
    #fileName = cms.untracked.string('file:EXO-RunIISummer15wmLHEGS-00000_inLHE.root'),
    #dataset = cms.untracked.PSet(
        #filterName = cms.untracked.string(''),
        #dataTier = cms.untracked.string('LHE')
    #)
#)

# Additional output definition

# Other statements
#process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

#process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    #pythiaPylistVerbosity = cms.untracked.int32(1),
    #filterEfficiency = cms.untracked.double(1.0),
    #pythiaHepMCVerbosity = cms.untracked.bool(False),
    #comEnergy = cms.double(13000.0),
    #maxEventsToPrint = cms.untracked.int32(1),
    #PythiaParameters = cms.PSet(
        #pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            #'Main:timesAllowErrors = 10000', 
            #'Check:epTolErr = 0.01', 
            #'Beams:setProductionScalesFromLHEF = off', 
            #'SLHA:keepSM = on', 
            #'SLHA:minMassSM = 1000.', 
            #'ParticleDecays:limitTau0 = on', 
            #'ParticleDecays:tau0Max = 10', 
            #'ParticleDecays:allowPhotonRadiation = on'),
        #pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            #'Tune:ee 7', 
            #'MultipartonInteractions:pT0Ref=2.4024', 
            #'MultipartonInteractions:ecmPow=0.25208', 
            #'MultipartonInteractions:expPow=1.6'),
        #processParameters = cms.vstring('SLHA:useDecayTable = off', 
            #'25:m0 = 125.0', 
            #'25:onMode = off', 
            #'25:onIfMatch = 24 -24', 
            #'24:mMin = 0.05', 
            #'24:onMode = off', 
            #'24:onIfAny = 11 13 15 12 14 16 1 2 3 4'),
        #parameterSets = cms.vstring('pythia8CommonSettings', 
            #'pythia8CUEP8M1Settings', 
            #'processParameters')
    #)
#)


#process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    #nEvents = cms.untracked.uint32(400),
    #outputFile = cms.string('cmsgrid_final.lhe'),
    #scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    #numberOfParameters = cms.uint32(1),
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.0/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/v1/Zprime_A0h_A0chichi_MZp600_MA0300_tarball.tar.xz')
#)


#process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
#process.lhe_step = cms.Path(process.externalLHEProducer)
#process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
#process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
#process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
#for path in process.paths:
        #if path in ['lhe_step']: continue
        #getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
