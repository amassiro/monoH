if [ $# -lt 1 ]; then
    echo "  "
    echo "  ./test-run-8x-mc.sh EVENTS"
    echo "  "
    exit -1
fi

export EVENTS=$1


#
# GlobalTag choice
#
# cat /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_5/src/Configuration/AlCa/python/autoCond.py | grep run2_mc
#    'run2_mc_50ns'      :   '80X_mcRun2_startup_v12',
#    'run2_mc'           :   '80X_mcRun2_asymptotic_v12',
#



# export MYFILE=file:/afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_14/src/monoH/Generation/EXO-RunIISpring16MiniAODv2-05058.root
### Type              Module                  Label   Process
### LHEEventProduct   "externalLHEProducer"   ""      "LHE"


export MYFILE="/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_1.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_10.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_11.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_12.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_13.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_14.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_15.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_16.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_17.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_18.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_19.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_2.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_20.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_21.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_22.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_23.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_24.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_25.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_26.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_27.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_28.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_29.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_3.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_30.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_31.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_32.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_33.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_34.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_35.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_36.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_37.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_38.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_39.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_4.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_40.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_41.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_42.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_43.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_44.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_45.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_46.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_47.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_48.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_49.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_5.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_6.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_7.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_8.root,\
/store/user/amassiro/monoHWWlvjj/Publish/AOD/monoHWW-lvjj_GENSIM_v1/crab_monoHWWlvjj-AOD/170420_163228/0000/EXO-RunIISpring16MiniAODv2-05058_9.root"


    
    
    
    

rm -rf latino_stepB_mc_numEvent${EVENTS}.root

cmsRun stepB.py print                   \
    reportEvery=10                      \
    summary=false                       \
    is50ns=False                        \
    isPromptRecoData=False              \
    globalTag=80X_mcRun2_asymptotic_2016_TrancheIV_v7 \
    label=monoHww                       \
    outputFile=stepB_mc.root            \
    selection=LooseNoIso                \
    doNoFilter=False                    \
    doMuonIsoId=True                    \
    doEleIsoId=True                     \
    doBTag=True                         \
    runPUPPISequence=True               \
    doPhotonID=True                     \
    doGen=True                          \
    doLHE=True                          \
    doMCweights=True                    \
    maxEvents=${EVENTS}                 \
    inputFiles=${MYFILE}                \
    doFatJet=True                       \
    LHEweightSource=externalLHEProducer \
    LHERunInfo=""

python cmssw2latino.py stepB_mc_numEvent${EVENTS}.root

rm -rf stepB_mc_numEvent${EVENTS}.root







