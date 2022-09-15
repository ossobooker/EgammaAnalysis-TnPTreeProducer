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
    'mc':   cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/4E295BA9-D9F7-6643-B993-57789E70C0CB.root', 'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/0128B7AC-AA95-C44F-86E6-B79FC2C8BF8A.root', 'root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/014406E7-6906-7041-BBB5-E99625AF42E1.root'),
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
