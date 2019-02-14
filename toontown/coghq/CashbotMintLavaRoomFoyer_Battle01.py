from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE18a',
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
    10004: {
        'type': 'locator',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'searchPath': '**/EXIT1'
    },
    10013: {
        'type': 'mintProduct',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(-3.9454963207199998, 18.231958389300001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10014: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(3.8540270328499999, 18.231958389300001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10015: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(-18.556768417400001, 14.150022506699999,
                      6.5729341507000001),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10001: {
        'type': 'model',
        'name': 'vaultDoor',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover.bam'
    },
    10003: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(13.231122016900001, 20.356472015400001, 0.305192321539),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.2184969186800001, 1.2184969186800001,
                      1.2184969186800001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam'
    },
    10007: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(-17.548149108899999, 20.821084976200002, 0.0075693130493199997),
        'hpr':
        Vec3(0.0, 0.0, 0.0),
        'scale':
        Vec3(1.30483365059, 1.30483365059, 1.30483365059),
        'collisionsOnly':
        0,
        'flattenType':
        'light',
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/crates_F1.bam'
    },
    10008: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10007,
        'pos':
        Point3(-1.55398654938, -4.8495068550099996, 0.0),
        'hpr':
        Vec3(0.0, 0.0, 0.0),
        'scale':
        Vec3(0.91359388828300003, 0.91359388828300003, 0.91359388828300003),
        'collisionsOnly':
        0,
        'flattenType':
        'light',
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10009: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10002,
        'pos':
        Point3(-19.041290283199999, -18.431484222400002,
               0.0086744902655500004),
        'hpr':
        Vec3(0.0, 0.0, 0.0),
        'scale':
        Vec3(1.0, 1.0, 1.0),
        'collisionsOnly':
        0,
        'flattenType':
        'light',
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/crates_G1.bam'
    },
    10010: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(18.666227340700001, -13.083732605,
                      0.0057019400410400004),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10002: {
        'type': 'nodepath',
        'name': 'crates',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10005: {
        'type': 'nodepath',
        'name': 'battle',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(-90.0, 0.0, 0.0),
        'scale': 1
    },
    10011: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(-90.0, 0.0, 0.0),
        'scale': 1
    },
    10012: {
        'type': 'nodepath',
        'name': 'product',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}
