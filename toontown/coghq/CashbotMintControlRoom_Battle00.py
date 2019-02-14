from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE31a',
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
    10013: {
        'type': 'mintProduct',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(0.0, 16.545541763300001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10014: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(9.3373184204099999, 15.9028654099, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10015: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(-9.3001441955599997, 11.6405067444, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10003: {
        'type': 'mintShelf',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(19.5716362, 16.3833560944, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10004: {
        'type': 'mintShelf',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(19.5716362, 2.9330446720099999, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10005: {
        'type': 'mintShelf',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(19.5716362, -10.478040695200001, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10006: {
        'type': 'mintShelf',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-19.5699996948, 16.3833560944, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10007: {
        'type': 'mintShelf',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-19.5699996948, 2.9330446720099999, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10008: {
        'type': 'mintShelf',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-19.5699996948, -10.478040695200001, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10001: {
        'type': 'model',
        'name': 'vaultDoor',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 22.997629165599999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover.bam'
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
        'name': 'shelves',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10011: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
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
