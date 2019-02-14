from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE10a',
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
    10009: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(63.974136352499997, -10.934322357199999,
                      9.9769611358599999),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 8,
        'rewardPerGrabMax': 0
    },
    10010: {
        'type': 'healBarrel',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.0, 0.0, 4.1399998664900002),
        'hpr': Vec3(349.35876464799998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 8,
        'rewardPerGrabMax': 0
    },
    10000: {
        'type':
        'nodepath',
        'name':
        'mixers',
        'comment':
        '',
        'parentEntId':
        0,
        'pos':
        Point3(-19.239728927600002, 0.0, 5.5399999618500004),
        'hpr':
        Vec3(0.0, 0.0, 0.0),
        'scale':
        Vec3(0.75800174474699999, 0.75800174474699999, 0.75800174474699999)
    },
    10004: {
        'type': 'paintMixer',
        'name': 'mixer0',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0.0, 10.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'easeInOut',
        'offset': Point3(20.0, 20.0, 0.0),
        'period': 8.0,
        'phaseShift': 0.0,
        'shaftScale': 1,
        'waitPercent': 0.10000000000000001
    },
    10005: {
        'type': 'paintMixer',
        'name': 'mixer1',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(29.0, 10.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'easeInOut',
        'offset': Point3(0.0, -20.0, 0.0),
        'period': 8.0,
        'phaseShift': 0.5,
        'shaftScale': 1,
        'waitPercent': 0.10000000000000001
    },
    10006: {
        'type': 'paintMixer',
        'name': 'mixer2',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(58.0, -8.9407224655200004, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'easeInOut',
        'offset': Point3(-20.0, -20.0, 0.0),
        'period': 8.0,
        'phaseShift': 0.5,
        'shaftScale': 1,
        'waitPercent': 0.10000000000000001
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}
