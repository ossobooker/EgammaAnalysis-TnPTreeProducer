import FWCore.ParameterSet.Config as cms

# Some miniAOD testfiles, about 1000 events copied to our eos storage
# (not running directly on datasets because they get moved around all the time and xrootd sucks)
filesMiniAOD_2018 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIIAutumn18MiniAOD-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018A-17Sep2018-v2.root'),
}

filesMiniAOD_2017 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIIFall17MiniAODv2-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017B-31Mar2018-v1.root'),
}

filesMiniAOD_2016 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer16MiniAODv3-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016B-17Jul2018_ver2-v1.root'),
}


# Some miniAOD UL testfiles, which are available now and hopefully don't get deleted too soon
filesMiniAOD_UL2016preVFP = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16MiniAODAPV-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM.root'),
}

filesMiniAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP.root'),
}

filesMiniAOD_UL2018 = {
    # 'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18MiniAOD-DYJetsToEE_M-50.root'),
    # 'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/4E295BA9-D9F7-6643-B993-57789E70C0CB.root', 'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/0128B7AC-AA95-C44F-86E6-B79FC2C8BF8A.root', 'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/014406E7-6906-7041-BBB5-E99625AF42E1.root'),
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120001/069DD4FC-C445-DE4F-8314-B5339CB4908B.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120001/CDCB1127-CC3D-5F48-ACEB-D2283F34D879.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120001/DA414BAD-2FBE-934E-9924-18FA0E16ED27.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/120001/ADDBE85E-A33A-564A-A7D8-6E8E82FD65FA.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/4E83CA21-985E-C44C-927C-133F0B7D6790.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/A141F6DF-704E-004F-AF82-614BFD36A2F6.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/A4EA2F42-6CFE-0445-81CA-580F83D9770F.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/25E5593B-F333-4C40-A2DE-F9BA7A151538.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/9DE08EAC-2AB1-3244-A45E-040BC5B2DACB.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/AEAE7609-94C5-9F4C-9B4A-25827F6EFBFF.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/5217D103-F808-364F-9DD9-B4E32CA19AF0.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/BF0645A6-4094-8E46-A574-8D10498531EA.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/863E5E39-5960-364A-9B06-067F78F3E673.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/C0617E46-3766-FF44-822C-5F6EE947F97B.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/5F9A3B8E-C78C-C94C-BCD0-9452479BF1C5.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/BE8053FB-FD84-7542-94FE-E6DA4615BBA8.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/A224A8B6-6DD6-8E4F-A16A-3241832EDCC7.root',
                                  'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAOD/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/1010000/9F6C15F4-118C-3F44-BA4A-55FB0600F06A.root',),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018.root'),
}

filesMiniAOD_UL2017 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017.root'),
}


# AOD UL testfiles
filesAOD_UL2016preVFP = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16RECOAPV-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM-AOD.root'),
}

filesAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP-AOD.root'),
}

filesAOD_UL2018 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18RECO-DYToEE_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018-AOD.root'),
}

filesAOD_UL2017 = {
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17RECO-DYToEE_M-50.root'),
    'data': cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017-AOD.root'),
}
