Production
====

wmLHE + GS
====

Run in local:

    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_7_1_23/src/monoH/Generation
    cmsRun wmLHEGS_template_cfg.py   -----> EXO-RunIISummer15wmLHEGS-00000.root
    cmsRun wmLHEG_template_cfg.py
    
    
    Before matching: total cross section = 3.507e-01 +- 8.570e-05 pb
    After matching: total cross section = 3.507e-01 +- 8.570e-05 pb

    
    cmsRun GS_template_cfg.py   
    
    
    cd /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_14/src/monoH/Generation
    
    cmsRun DR_template_cfg.py   
    cmsRun DR_step2_template_cfg.py   

    cmsRun AOD_template_cfg.py   

    
Time for wmLHE+GS:

    Begin processing the 3rd record. Run 1, Event 3, LumiSection 1 at 23-Mar-2017 18:33:50.020 CET
    Begin processing the 500th record. Run 1, Event 500, LumiSection 1 at 23-Mar-2017 21:48:05.034 CET
    Begin processing the 957th record. Run 1, Event 957, LumiSection 1 at 24-Mar-2017 00:39:01.586 CET

    
    Begin processing the 2nd record. Run 1, Event 2, LumiSection 1 at 27-Mar-2017 10:26:08.718 CEST
    Begin processing the 999th record. Run 1, Event 999, LumiSection 1 at 27-Mar-2017 16:40:52.002 CEST

    
    
Publish GEN for later CRAB submission:

    source /cvmfs/cms.cern.ch/crab3/crab.sh
    
    crab submit crab_cfg_publish.py
    
    
    cmsRun SIM_template_cfg.py
    crab submit crab_cfg_SIM.py
    
    
    gen+sim in one step
    crab submit crab_cfg_GENSIM.py
    
    DR step 1   ----> /monoHWW-lvjj_GENSIM_v1/amassiro-crab_monoHWWlvjj-DR1-9c549b5207abdfb5ae0876b07ca1f88d/USER
    crab submit crab_cfg_DR_step1.py
    
    DR step 2   ----> /monoHWW-lvjj_GENSIM_v1/amassiro-crab_monoHWWlvjj-DR2-7acb7139bf84d3a816d33703984a9cf5/USER
    crab submit crab_cfg_DR_step2.py
    crab status crab_monoHWWlvjj-DR2

    AOD step    ----> 
    crab submit crab_cfg_AOD.py
    crab status crab_monoHWWlvjj-AOD

    
    cmsRun AOD_template_cfg.py   
    
    
    
    
    
Time for DR (1 and 2):
    
    
    Begin processing the 5th record. Run 1, Event 5, LumiSection 1 at 24-Mar-2017 17:39:33.087 CET
    Begin processing the 400th record. Run 1, Event 400, LumiSection 1 at 24-Mar-2017 17:53:05.319 CET

    EXO-RunIISpring16DR80-00000_step1.root
    
    
    
    Begin processing the 1st record. Run 1, Event 1, LumiSection 1 at 24-Mar-2017 17:58:23.345 CET
    Begin processing the 400th record. Run 1, Event 399, LumiSection 1 at 24-Mar-2017 18:17:16.071 CET

    
Latino

    cd /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_26_patch1/src/LatinoTrees/AnalysisStep/test/
    cmsenv
    
    sh /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_14/src/monoH/Generation/latino.sh 400
    sh /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_8_0_14/src/monoH/Generation/latino.sh 1000
    
    r00t latino_stepB_mc_numEvent1000.root
    
    latino->Draw("std_vector_fatjet_prunedmass[0]", "std_vector_fatjet_pt[0]>0 && std_vector_lepton_pt[1] <=0 ");
    latino->Draw("std_vector_fatjet_massdrop[0]", "std_vector_fatjet_pt[0]>0 && std_vector_lepton_pt[1] <=0 ");
    
    
    
    
    