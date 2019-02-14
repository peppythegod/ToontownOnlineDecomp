from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE15a',
        'wantDoors': 1
    },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None
    },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    10001: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(44.257774353000002, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'cellId': 0,
        'radius': 10.0
    },
    10003: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(39.396408081099999, 22.259342193599998, 16.065912246700002),
        'hpr':
        Vec3(270.0, 0.0, 90.0),
        'scale':
        Vec3(0.56086426973299996, 0.56086426973299996, 0.56086426973299996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModel',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10005: {
        'type': 'model',
        'name': 'farLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(41.822696685799997, 16.543403625500002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10006: {
        'type': 'model',
        'name': 'farRight',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(41.822696685799997, -16.540000915499999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10007: {
        'type':
        'model',
        'name':
        'copy of <unnamed>',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(39.319274902300002, -22.823434829699998, 13.609273910500001),
        'hpr':
        Vec3(270.0, 0.0, 270.0),
        'scale':
        Point3(0.56000000238400005, 0.56086426973299996, 0.56086426973299996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModel',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10008: {
        'type':
        'model',
        'name':
        'copy of <unnamed>',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(-39.380081176799997, -22.885538101200002, 16.065912246700002),
        'hpr':
        Point3(90.0, 0.0, 90.0),
        'scale':
        Vec3(0.56086426973299996, 0.56086426973299996, 0.56086426973299996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModel',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10009: {
        'type':
        'model',
        'name':
        'copy of <unnamed> (2)',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(-39.306285858199999, 22.1807098389, 13.609273910500001),
        'hpr':
        Point3(90.0, 0.0, 270.0),
        'scale':
        Point3(0.56000000238400005, 0.56086426973299996, 0.56086426973299996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModel',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10010: {
        'type': 'model',
        'name': 'nearLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-41.819999694800003, 16.543403625500002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10011: {
        'type': 'model',
        'name': 'nearRight',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-41.819999694800003, -16.540000915499999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10002: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10004: {
        'type': 'nodepath',
        'name': 'collisions',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}
