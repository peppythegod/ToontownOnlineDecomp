from toontown.toonbase import TTLocalizer
from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500.0,
        'modelFilename': 'phase_9/models/cogHQ/SelbotLegFactory',
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
    3: {
        'type': 'zone',
        'name': 'Main Entrance',
        'comment': '',
        'parentEntId': 0,
        'scale': Vec3(1, 1, 1),
        'description': TTLocalizer.SellbotLegFactorySpecMainEntrance,
        'visibility': [114]
    },
    4: {
        'type': 'zone',
        'name': 'Lobby',
        'comment': '',
        'parentEntId': 0,
        'scale': Vec3(1, 1, 1),
        'description': TTLocalizer.SellbotLegFactorySpecLobby,
        'visibility': [113, 114]
    },
    5: {
        'type': 'zone',
        'name': 'hallwayFromLobby',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [113, 116]
    },
    6: {
        'type': 'zone',
        'name': 'hallwayToBoiler/Control/Lookout',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecLobbyHallway,
        'visibility': [109, 116, 117, 118]
    },
    7: {
        'type': 'zone',
        'name': 'GearRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecGearRoom,
        'visibility': [109, 110]
    },
    8: {
        'type': 'zone',
        'name': 'BoilerRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecBoilerRoom,
        'visibility': [108, 117]
    },
    9: {
        'type':
        'zone',
        'name':
        'EastCatwalk',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecEastCatwalk,
        'visibility':
        [23, 25, 26, 33, 34, 35, 38, 41, 53, 110, 112, 115, 124, 200, 222]
    },
    10: {
        'type': 'zone',
        'name': 'PaintMixer',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecPaintMixer,
        'visibility': [11, 111, 112]
    },
    11: {
        'type': 'zone',
        'name': 'PaintMixerRewardRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecPaintMixerStorageRoom,
        'visibility': [10, 111, 112]
    },
    12: {
        'type':
        'zone',
        'name':
        'WestSiloCatwalk',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecWestSiloCatwalk,
        'visibility': [
            21, 26, 33, 34, 35, 36, 37, 40, 41, 53, 60, 61, 108, 110, 119, 120,
            125, 127, 128, 129, 130, 200
        ]
    },
    13: {
        'type': 'zone',
        'name': 'PipeRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecPipeRoom,
        'visibility': [119, 121]
    },
    14: {
        'type': 'zone',
        'name': 'StairsToPipeRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [17, 18, 121, 126, 131]
    },
    15: {
        'type': 'zone',
        'name': 'DuctRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecDuctRoom,
        'visibility': [106, 126]
    },
    16: {
        'type': 'zone',
        'name': 'Side Entrance',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecSideEntrance,
        'visibility': [106]
    },
    17: {
        'type': 'zone',
        'name': 'StomperAlley',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecStomperAlley,
        'visibility': [14, 121, 126, 131]
    },
    18: {
        'type': 'zone',
        'name': 'LavaRoomFoyer',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecLavaRoomFoyer,
        'visibility': [19, 20, 102, 103, 105, 131]
    },
    19: {
        'type': 'zone',
        'name': 'LavaRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecLavaRoom,
        'visibility': [17, 18, 20, 105, 131]
    },
    20: {
        'type': 'zone',
        'name': 'LavaRewardRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecLavaStorageRoom,
        'visibility': [18, 19, 105]
    },
    21: {
        'type':
        'zone',
        'name':
        'WestCatwalk',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecWestCatwalk,
        'visibility':
        [12, 23, 26, 33, 34, 35, 40, 41, 53, 60, 108, 119, 120, 125, 127, 200]
    },
    22: {
        'type': 'zone',
        'name': 'OilRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecOilRoom,
        'visibility': [107]
    },
    23: {
        'type': 'zone',
        'name': 'Lookout',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecLookout,
        'visibility': [24, 39, 115, 118, 120, 123, 124, 125]
    },
    24: {
        'type': 'zone',
        'name': 'Warehouse',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecWarehouse,
        'visibility': [23, 39, 115, 120, 123, 124, 125]
    },
    25: {
        'type': 'zone',
        'name': 'PaintMixerExterior',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    26: {
        'type': 'zone',
        'name': 'WarehouseExterior',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    27: {
        'type': 'zone',
        'name': 'OilRoomHallway',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecOilRoomHallway,
        'visibility': [105, 107, 127]
    },
    30: {
        'type': 'zone',
        'name': 'EastSiloControlRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecEastSiloControlRoom,
        'visibility': [130]
    },
    31: {
        'type': 'zone',
        'name': 'WestSiloControlRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecWestSiloControlRoom,
        'visibility': [128]
    },
    32: {
        'type': 'zone',
        'name': 'CenterSiloControlRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecCenterSiloControlRoom,
        'visibility': [129]
    },
    33: {
        'type':
        'zone',
        'name':
        'EastSilo',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecEastSilo,
        'visibility': [
            9, 12, 21, 25, 26, 34, 35, 36, 37, 38, 40, 41, 53, 60, 61, 108,
            110, 112, 119, 124, 128, 129, 130, 200, 222
        ]
    },
    34: {
        'type':
        'zone',
        'name':
        'WestSilo',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecWestSilo,
        'visibility': [
            9, 12, 21, 25, 26, 33, 35, 36, 37, 40, 41, 53, 60, 61, 108, 110,
            112, 119, 120, 125, 127, 128, 129, 130, 200
        ]
    },
    35: {
        'type':
        'zone',
        'name':
        'CenterSilo',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecCenterSilo,
        'visibility': [
            9, 21, 25, 26, 33, 34, 36, 37, 40, 41, 53, 60, 61, 108, 110, 112,
            119, 128, 129, 130, 200
        ]
    },
    36: {
        'type':
        'zone',
        'name':
        'WestSiloBridge',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        '',
        'visibility': [
            9, 12, 21, 25, 26, 33, 34, 35, 36, 37, 40, 41, 53, 60, 61, 108,
            110, 112, 119, 127, 128, 129, 130, 200
        ]
    },
    37: {
        'type':
        'zone',
        'name':
        'EastSiloBridge',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        '',
        'visibility': [
            9, 12, 21, 25, 26, 33, 34, 35, 36, 37, 38, 40, 41, 53, 60, 61, 108,
            110, 112, 119, 128, 129, 130, 200, 222
        ]
    },
    38: {
        'type':
        'zone',
        'name':
        'EastSiloCatwalk',
        'comment':
        '',
        'parentEntId':
        0,
        'scale':
        1,
        'description':
        TTLocalizer.SellbotLegFactorySpecEastSiloCatwalk,
        'visibility': [
            9, 25, 26, 33, 34, 35, 36, 37, 41, 53, 60, 110, 112, 115, 124, 200,
            222
        ]
    },
    39: {
        'type': 'zone',
        'name': 'WarehouseCeiling',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    40: {
        'type': 'zone',
        'name': 'WestExterior',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    41: {
        'type': 'zone',
        'name': 'EastExterior',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    53: {
        'type': 'zone',
        'name': 'ExteriorFloor',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    60: {
        'type': 'zone',
        'name': 'WestElevatorShaft',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecWestElevatorShaft,
        'visibility': [12, 34]
    },
    61: {
        'type': 'zone',
        'name': 'EastElevatorShaft',
        'comment': 'no geom or DCS',
        'parentEntId': 0,
        'scale': 1,
        'description': TTLocalizer.SellbotLegFactorySpecEastElevatorShaft,
        'visibility': [33, 38]
    },
    101: {
        'type': 'zone',
        'name': 'dwToLavaRewardRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    102: {
        'type': 'zone',
        'name': 'dwToLavaRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    103: {
        'type': 'zone',
        'name': 'dwToLavaRoomHallway',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    105: {
        'type': 'zone',
        'name': 'dwToOilRoomCatwalks',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    106: {
        'type': 'zone',
        'name': 'dwToDuctRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    107: {
        'type': 'zone',
        'name': 'dwToOilRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    108: {
        'type': 'zone',
        'name': 'dwFromBoilerRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    109: {
        'type': 'zone',
        'name': 'dwToGearRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    110: {
        'type': 'zone',
        'name': 'dwFromGearRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    111: {
        'type': 'zone',
        'name': 'dwToPaintMixerRewardRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    112: {
        'type': 'zone',
        'name': 'dwToPaintMixer',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    113: {
        'type': 'zone',
        'name': 'dwFromLobby',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    114: {
        'type': 'zone',
        'name': 'dwToLobby',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    115: {
        'type': 'zone',
        'name': 'dwToWarehouseFromRight',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    116: {
        'type': 'zone',
        'name': 'dwFromLobbyFar',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    117: {
        'type': 'zone',
        'name': 'dwToBoilerRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    118: {
        'type': 'zone',
        'name': 'dwToLookout',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    119: {
        'type': 'zone',
        'name': 'dwFromPipeRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    120: {
        'type': 'zone',
        'name': 'dwToWarehouseFromLeft',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    121: {
        'type': 'zone',
        'name': 'dwToPipeRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    122: {
        'type': 'zone',
        'name': 'dwToWarehouseControlRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    123: {
        'type': 'zone',
        'name': 'dwFromWarehouseFloor',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    124: {
        'type': 'zone',
        'name': 'dwFromWarehouseRight',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    125: {
        'type': 'zone',
        'name': 'dwFromWarehouseLeft',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    126: {
        'type': 'zone',
        'name': 'dwFromDuctRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    127: {
        'type': 'zone',
        'name': 'dwFromOilRoomHallway',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    128: {
        'type': 'zone',
        'name': 'dwToWestSiloRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    129: {
        'type': 'zone',
        'name': 'dwToCenterSiloRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    130: {
        'type': 'zone',
        'name': 'dwToEastSiloRoom',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    131: {
        'type': 'zone',
        'name': 'dwFromStomperAlley',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    200: {
        'type': 'zone',
        'name': 'sky',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    201: {
        'type': 'zone',
        'name': 'extraZone201',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    202: {
        'type': 'zone',
        'name': 'extraZone202',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    203: {
        'type': 'zone',
        'name': 'extraZone203',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    204: {
        'type': 'zone',
        'name': 'extraZone204',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    205: {
        'type': 'zone',
        'name': 'extraZone205',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    206: {
        'type': 'zone',
        'name': 'extraZone206',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    207: {
        'type': 'zone',
        'name': 'extraZone207',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    208: {
        'type': 'zone',
        'name': 'extraZone208',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    209: {
        'type': 'zone',
        'name': 'extraZone209',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    210: {
        'type': 'zone',
        'name': 'extraZone210',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    211: {
        'type': 'zone',
        'name': 'extraZone211',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    212: {
        'type': 'zone',
        'name': 'extraZone212',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    213: {
        'type': 'zone',
        'name': 'extraZone213',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    214: {
        'type': 'zone',
        'name': 'extraZone214',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    215: {
        'type': 'zone',
        'name': 'extraZone215',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    216: {
        'type': 'zone',
        'name': 'extraZone216',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    217: {
        'type': 'zone',
        'name': 'extraZone217',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    218: {
        'type': 'zone',
        'name': 'extraZone218',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    219: {
        'type': 'zone',
        'name': 'extraZone219',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    220: {
        'type': 'zone',
        'name': 'extraZone220',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    221: {
        'type': 'zone',
        'name': 'extraZone221',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    222: {
        'type': 'zone',
        'name': 'dwToEastSiloInterior',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    10010: {
        'type': 'ambientSound',
        'name': 'westWind',
        'comment': '',
        'parentEntId': 35,
        'pos': Point3(-52.754899999999999, -38.837400000000002,
                      53.375799999999998),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'enabled': 1,
        'soundPath': 'phase_9/audio/sfx/CHQ_FACT_whistling_wind.mp3',
        'volume': 1
    },
    10016: {
        'type': 'ambientSound',
        'name': 'sndConveyorBelt',
        'comment': '',
        'parentEntId': 10056,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'enabled': 1,
        'soundPath': 'phase_9/audio/sfx/CHQ_FACT_conveyor_belt.mp3',
        'volume': 0.5
    },
    10053: {
        'type': 'ambientSound',
        'name': 'eastWind',
        'comment': '',
        'parentEntId': 35,
        'pos': Point3(52.75, -38.840000000000003, 53.380000000000003),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'enabled': 1,
        'soundPath': 'phase_9/audio/sfx/CHQ_FACT_whistling_wind.mp3',
        'volume': 1
    },
    10055: {
        'type': 'ambientSound',
        'name': 'sndGears',
        'comment': '',
        'parentEntId': 10056,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'enabled': 1,
        'soundPath': 'phase_9/audio/sfx/CHQ_FACT_gears_turning.mp3',
        'volume': 1
    },
    10031: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 8,
        'pos': Point3(-1, 79, 10),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1.75, 1, 1),
        'cellId': 1,
        'radius': 10.0
    },
    10035: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10039,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 4,
        'radius': 10.0
    },
    10038: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 7,
        'pos': Point3(0, -28.039999999999999, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 5,
        'radius': 10.0
    },
    20048: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0.97360199999999997, 71.700000000000003, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 0.20000000000000001, 1),
        'cellId': 0,
        'radius': 15.0
    },
    20063: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20033,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 8,
        'radius': 1
    },
    20064: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20034,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 8,
        'radius': 1
    },
    20065: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20035,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 8,
        'radius': 1
    },
    20066: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20036,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 8,
        'radius': 1
    },
    20086: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(0, 33, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(2, 1, 1),
        'cellId': 6,
        'radius': 12.0
    },
    20112: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(-10.0936, -9.5597499999999993, 4),
        'hpr': Point3(45, 0, 0),
        'scale': Point3(10, 1, 5),
        'cellId': 10,
        'radius': 5.0
    },
    20113: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(9.08399, 4.42157, 0),
        'hpr': Point3(-50, 0, 0),
        'scale': Point3(10, 2, 6),
        'cellId': 9,
        'radius': 5.0
    },
    20114: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60103,
        'pos': Point3(0, 0, 1),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 0.5),
        'cellId': 8,
        'radius': 3.0
    },
    10003: {
        'type': 'beanBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20,
        'pos': Point3(1.25458, 19.2471, 0.0249529),
        'hpr': Vec3(-8.2843400000000003, 0, 0),
        'scale': 1,
        'rewardPerGrab': 25,
        'rewardPerGrabMax': 0
    },
    10011: {
        'type':
        'beanBarrel',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20,
        'pos':
        Point3(16.344000000000001, -9.7300000000000004, 0.025000000000000001),
        'hpr':
        Vec3(-79.888800000000003, 0, 0),
        'scale':
        1,
        'rewardPerGrab':
        25,
        'rewardPerGrabMax':
        0
    },
    20017: {
        'type': 'beanBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(20.003499999999999, 2.94232, 0),
        'hpr': Vec3(-31.603300000000001, 0, 0),
        'scale': 1,
        'rewardPerGrab': 35,
        'rewardPerGrabMax': 0
    },
    10039: {
        'type': 'button',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 22,
        'pos': Point3(-7, 29, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(4, 4, 4),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    20033: {
        'type':
        'button',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20022,
        'pos':
        Point3(0, 0, 0),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        Point3(3, 3, 3),
        'color':
        Vec4(0.86274499999999998, 0.51764699999999997, 0.094117699999999999,
             1),
        'isOn':
        0,
        'isOnEvent':
        0,
        'secondsOn':
        1
    },
    20034: {
        'type':
        'button',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20022,
        'pos':
        Point3(7.5, 0, 0),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        Point3(3, 3, 3),
        'color':
        Vec4(0.86274499999999998, 0.51764699999999997, 0.094117699999999999,
             1),
        'isOn':
        0,
        'isOnEvent':
        0,
        'secondsOn':
        1
    },
    20035: {
        'type':
        'button',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20022,
        'pos':
        Point3(15, 0, 0),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        Point3(3, 3, 3),
        'color':
        Vec4(0.86274499999999998, 0.51764699999999997, 0.094117699999999999,
             1),
        'isOn':
        0,
        'isOnEvent':
        0,
        'secondsOn':
        1
    },
    20036: {
        'type':
        'button',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20022,
        'pos':
        Point3(22.5, 0, 0),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        Point3(3, 3, 3),
        'color':
        Vec4(0.86274499999999998, 0.51764699999999997, 0.094117699999999999,
             1),
        'isOn':
        0,
        'isOnEvent':
        0,
        'secondsOn':
        1
    },
    30040: {
        'type': 'button',
        'name': 'door button',
        'comment': 'Entrance door unlock',
        'parentEntId': 3,
        'pos': Point3(0, 6.75, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(3, 3, 3),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    30076: {
        'type': 'button',
        'name': 'open door 113',
        'comment': 'Lobby door unlock',
        'parentEntId': 4,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(3, 3, 3),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1
    },
    60102: {
        'type': 'button',
        'name': 'door button',
        'comment': 'Entrance Door Unlock',
        'parentEntId': 16,
        'pos': Point3(4, 8, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(3, 3, 3),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    60103: {
        'type': 'button',
        'name': 'door button',
        'comment': '',
        'parentEntId': 20022,
        'pos': Point3(25, -7, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(4, 4, 4),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    60104: {
        'type': 'button',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 31,
        'pos': Point3(0, 10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(5, 5, 4),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    60105: {
        'type': 'button',
        'name': 'door button',
        'comment': '',
        'parentEntId': 30,
        'pos': Point3(-4, 7, 0),
        'hpr': Point3(0, 0, 0),
        'scale': Point3(5, 5, 4),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    60118: {
        'type': 'button',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(0, 20, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(3, 3, 3),
        'color': Vec4(1, 0, 0, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': -1.0
    },
    10005: {
        'type': 'conveyorBelt',
        'name': 'belt',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 45.202399999999997, 7.2493699999999999),
        'hpr': Point3(180, 0, 0),
        'scale': 1,
        'floorName': 'platformcollision',
        'length': 78.818813527042181,
        'speed': 2.0,
        'treadLength': 10.0,
        'treadModelPath': 'phase_9/models/cogHQ/platform1',
        'widthScale': 0.84999999999999998
    },
    20081: {
        'type': 'crate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20080,
        'pos': Point3(0, 0, 0),
        'scale': 0.920000016689,
        'crushCellId': None,
        'gridId': 20080,
        'modelType': 0,
        'pushable': 1
    },
    20091: {
        'type': 'crate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20090,
        'pos': Point3(0, 23, 0),
        'scale': 0.920000016689,
        'crushCellId': None,
        'gridId': 20090,
        'modelType': 0,
        'pushable': 1
    },
    20024: {
        'type': 'crusherCell',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20023,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'col': 1,
        'gridId': 20025,
        'row': 14
    },
    20026: {
        'type': 'crusherCell',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20023,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'col': 10,
        'gridId': 20025,
        'row': 14
    },
    20027: {
        'type': 'crusherCell',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 20023,
        'pos': Point3(1, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'col': 21,
        'gridId': 20025,
        'row': 14
    },
    20028: {
        'type': 'crusherCell',
        'name': 'copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20023,
        'pos': Point3(2, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'col': 28,
        'gridId': 20025,
        'row': 14
    },
    30078: {
        'type': 'cutScene',
        'name': 'button door',
        'comment': '',
        'parentEntId': 114,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'duration': 4.0,
        'effect': 'irisInOut',
        'motion': 'doorUnlock',
        'startStopEvent': 30077
    },
    10002: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 128,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    10052: {
        'type': 'door',
        'name': 'door 127',
        'comment': '',
        'parentEntId': 127,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 10039,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30000: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 114,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 60132,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30001: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 105,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1.0,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30002: {
        'type': 'door',
        'name': 'door 106',
        'comment': '',
        'parentEntId': 106,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 60132,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30003: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 107,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30004: {
        'type': 'door',
        'name': 'doorFromBoilerRoom',
        'comment': '',
        'parentEntId': 108,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30005: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 109,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30006: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 110,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30008: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 112,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30009: {
        'type': 'door',
        'name': 'door 113',
        'comment': '',
        'parentEntId': 113,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 60119,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30010: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 115,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30011: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 116,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30012: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 117,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30013: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 118,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30014: {
        'type': 'door',
        'name': 'doorFromPipeRoom 119',
        'comment': '',
        'parentEntId': 119,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30015: {
        'type': 'door',
        'name': 'door 120',
        'comment': '',
        'parentEntId': 120,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30016: {
        'type': 'door',
        'name': 'door 121',
        'comment': '',
        'parentEntId': 121,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30017: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 122,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30018: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 123,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 0,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 60103,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30019: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 124,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30020: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 125,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    30021: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 126,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 60119,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    60088: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 131,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1.0,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    60094: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 129,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 0,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1.0,
        'unlock0Event': 0,
        'unlock1Event': 60104,
        'unlock2Event': 60105,
        'unlock3Event': 0
    },
    60095: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 130,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    60101: {
        'type': 'door',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 222,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 1,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 1,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 0,
        'unlock2Event': 0,
        'unlock3Event': 0
    },
    10049: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 3
    },
    10051: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 4
    },
    60000: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 5
    },
    60001: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 6
    },
    60002: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 7
    },
    60003: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 9
    },
    60004: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 10
    },
    60005: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 8
    },
    60006: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 21
    },
    60007: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 24
    },
    60009: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 38
    },
    60011: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 12
    },
    60013: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 13
    },
    60014: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 14
    },
    60015: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 17
    },
    60016: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 15
    },
    60017: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 16
    },
    60018: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 19
    },
    60019: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 18
    },
    60024: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 22
    },
    60031: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 23
    },
    60044: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 33
    },
    60066: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 11
    },
    60067: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 27
    },
    60096: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 30
    },
    60108: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 34
    },
    60111: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 36
    },
    60114: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 37
    },
    60121: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 31
    },
    60126: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 35
    },
    60130: {
        'type': 'entityGroup',
        'name': 'viz',
        'comment': '',
        'parentEntId': 32
    },
    10028: {
        'type': 'entrancePoint',
        'name': 'entrance1',
        'comment': '',
        'parentEntId': 3,
        'pos': Point3(0, 10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'entranceId': 0,
        'radius': 15,
        'theta': 20
    },
    10029: {
        'type': 'entrancePoint',
        'name': 'entrance2',
        'comment': '',
        'parentEntId': 16,
        'pos': Point3(0, 10, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'entranceId': 1,
        'radius': 15,
        'theta': 20
    },
    10021: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(-2.02081, 0, 0),
        'hpr': Vec3(337.47699999999998, 0, 0),
        'scale': 1,
        'gagLevel': 2,
        'gagLevelMax': 0,
        'gagTrack': 0,
        'rewardPerGrab': 3,
        'rewardPerGrabMax': 0
    },
    10024: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(20.301200000000001, -26.321899999999999, 0),
        'hpr': Vec3(233.18700000000001, 0, 0),
        'scale': 1,
        'gagLevel': 4,
        'gagLevelMax': 0,
        'gagTrack': 4,
        'rewardPerGrab': 4,
        'rewardPerGrabMax': 0
    },
    10025: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(-47.311999999999998, 7.2257100000000003, 0),
        'hpr': Vec3(19.1524, 0, 0),
        'scale': 1,
        'gagLevel': 0,
        'gagLevelMax': 0,
        'gagTrack': 0,
        'rewardPerGrab': 3,
        'rewardPerGrabMax': 0
    },
    10026: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(-11.2037, 5.4351399999999996, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'gagLevel': 4,
        'gagLevelMax': 0,
        'gagTrack': 5,
        'rewardPerGrab': 4,
        'rewardPerGrabMax': 0
    },
    20020: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20,
        'pos': Point3(-23.020900000000001, 0, 0),
        'hpr': Vec3(126.676, 0, 0),
        'scale': 1,
        'gagLevel': 4,
        'gagLevelMax': 0,
        'gagTrack': 3,
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    20021: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20,
        'pos': Point3(-31.322500000000002, 14.1021, 0),
        'hpr': Vec3(-136.56999999999999, 0, 0),
        'scale': 1,
        'gagLevel': 4,
        'gagLevelMax': 0,
        'gagTrack': 5,
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    20085: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 5,
        'pos': Point3(3.1400000000000001, 12.670299999999999,
                      10.119999999999999),
        'hpr': Vec3(-24.810500000000001, 0, 0),
        'scale': 1,
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 4,
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    20093: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20087,
        'pos': Point3(2.3999999999999999, -1, 7),
        'hpr': Vec3(-151.53200000000001, 0, 0),
        'scale': 1,
        'gagLevel': 0,
        'gagLevelMax': 0,
        'gagTrack': 0,
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    10006: {
        'type': 'gear',
        'name': 'first',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 0, 26.063400000000001),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'degreesPerSec': 20.0,
        'gearScale': 25.0,
        'modelType': 'factory',
        'orientation': 'vertical',
        'phaseShift': 0
    },
    10007: {
        'type': 'gear',
        'name': 'second',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 15, 26.059999999999999),
        'hpr': Point3(180, 0, 0),
        'scale': 1,
        'degreesPerSec': 30.0,
        'gearScale': 25.0,
        'modelType': 'factory',
        'orientation': 'vertical',
        'phaseShift': 0
    },
    10008: {
        'type': 'gear',
        'name': 'third',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 30, 26.059999999999999),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'degreesPerSec': 40.0,
        'gearScale': 25.0,
        'modelType': 'factory',
        'orientation': 'vertical',
        'phaseShift': 0
    },
    10009: {
        'type': 'gear',
        'name': 'fourth',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 45, 26.059999999999999),
        'hpr': Point3(180, 0, 0),
        'scale': 1,
        'degreesPerSec': 47.0,
        'gearScale': 25.0,
        'modelType': 'factory',
        'orientation': 'vertical',
        'phaseShift': 0
    },
    20013: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20012,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.25,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 4
    },
    20014: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20010,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.25,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 4
    },
    20016: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20015,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.25,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 4
    },
    20041: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20040,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20026,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 80.0,
        'strength': 10,
        'velocity': 6.0
    },
    20043: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20042,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20024,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 80.0,
        'strength': 10,
        'velocity': 5.0
    },
    20046: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20044,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20024,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 70,
        'strength': 10,
        'velocity': 6.0
    },
    20047: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20045,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20026,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 80.0,
        'strength': 10,
        'velocity': 6.0
    },
    20052: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20051,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 12.0,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 3,
        'velocity': 4.0
    },
    20054: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20053,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20027,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 80.0,
        'strength': 10,
        'velocity': 5.5
    },
    20056: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20055,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20028,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 70,
        'strength': 10,
        'velocity': 6.0
    },
    20060: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20059,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20028,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 90.0,
        'strength': 10,
        'velocity': 6.5
    },
    20062: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20061,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': 20027,
        'goonType': 'pg',
        'gridId': 20025,
        'hFov': 70,
        'strength': 10,
        'velocity': 7.5
    },
    20071: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20070,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 6.0
    },
    20072: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20069,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 80.0,
        'strength': 7,
        'velocity': 6.0
    },
    20074: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20073,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.25,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 4
    },
    20089: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20084,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 7,
        'velocity': 4
    },
    20115: {
        'type': 'goonClipPlane',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, -7.4000000000000004, 0),
        'hpr': Point3(-90, 0, 0),
        'scale': Point3(5, 5, 5),
        'goonId': 20052
    },
    20116: {
        'type': 'goonClipPlane',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, -58, 0),
        'hpr': Point3(90, 0, 0),
        'scale': 1,
        'goonId': None
    },
    20117: {
        'type': 'goonClipPlane',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(0, -29, 0),
        'hpr': Point3(90, 0, 0),
        'scale': 1,
        'goonId': None
    },
    20118: {
        'type': 'goonClipPlane',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(-52, 0, 5),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'goonId': None
    },
    20025: {
        'type': 'grid',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20023,
        'pos': Point3(-48.444200000000002, -24.938500000000001, 0),
        'scale': 1,
        'cellSize': 3,
        'numCol': 30,
        'numRow': 16
    },
    20080: {
        'type': 'grid',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 5,
        'pos': Point3(1.5, -10.699999999999999, 0),
        'scale': 1,
        'cellSize': 3,
        'numCol': 2,
        'numRow': 5
    },
    20090: {
        'type': 'grid',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 17,
        'pos': Point3(-6.5, -111, 0),
        'scale': 1,
        'cellSize': 3,
        'numCol': 2,
        'numRow': 9
    },
    20011: {
        'type':
        'healBarrel',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        20,
        'pos':
        Point3(-2.0623499999999999, 20.219799999999999, 0.025000000000000001),
        'hpr':
        Vec3(-19.215299999999999, 0, 0),
        'scale':
        1,
        'rewardPerGrab':
        10,
        'rewardPerGrabMax':
        0
    },
    20092: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20087,
        'pos': Point3(-1, -1.5, 7),
        'hpr': Vec3(-191.78999999999999, 0, 0),
        'scale': 1,
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    10041: {
        'type': 'lift',
        'name': 'westLift',
        'comment': '',
        'parentEntId': 60,
        'pos': Point3(0, 0, 0.064199400000000004),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'autoMoveDelay': 5,
        'duration': 7.0,
        'endBoardSides': ['back'],
        'endGuardName': 'topGuard',
        'endPos': Point3(0, 0, 165),
        'floorName': 'elevator_floor',
        'modelPath': 'phase_9/models/cogHQ/Elevator.bam',
        'modelScale': Vec3(1, 1, 1),
        'moveDelay': 1,
        'startBoardSides': ['front'],
        'startGuardName': 'bottomGuard',
        'startPos': Point3(0, 0, 0)
    },
    10048: {
        'type': 'lift',
        'name': 'eastLift',
        'comment': '',
        'parentEntId': 61,
        'pos': Point3(0, -0.68406400000000001, 0.58932200000000001),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'autoMoveDelay': 5.0,
        'duration': 7.0,
        'endBoardSides': ['front', 'back', 'left', 'right'],
        'endGuardName': 'topGuard',
        'endPos': Point3(0, 0, 165),
        'floorName': 'elevator_floor',
        'modelPath': 'phase_9/models/cogHQ/Elevator.bam',
        'modelScale': Vec3(1, 1, 1),
        'moveDelay': 1,
        'startBoardSides': ['front'],
        'startGuardName': 'bottomGuard',
        'startPos': Point3(0, 0, 0)
    },
    10057: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10043,
        'input1Event': 30009,
        'input2Event': 30000,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    10059: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10058,
        'input1Event': 10057,
        'input2Event': 30011,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    10061: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10060,
        'input1Event': 10059,
        'input2Event': 30013,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    10063: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10062,
        'input1Event': 60033,
        'input2Event': 30009,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    30068: {
        'type': 'logicGate',
        'name': 'door 116 and door 118',
        'comment': '',
        'parentEntId': 30069,
        'input1Event': 30013,
        'input2Event': 30011,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60023: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60021,
        'input1Event': 30011,
        'input2Event': 30009,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60025: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60022,
        'input1Event': 60023,
        'input2Event': 30013,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60028: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60026,
        'input1Event': 30011,
        'input2Event': 30005,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60029: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60027,
        'input1Event': 30011,
        'input2Event': 30012,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60030: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 30071,
        'input1Event': 30011,
        'input2Event': 30009,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60033: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 30073,
        'input1Event': 30013,
        'input2Event': 30011,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60034: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 30075,
        'input1Event': 30013,
        'input2Event': 30005,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60035: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60032,
        'input1Event': 30013,
        'input2Event': 30012,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60037: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60036,
        'input1Event': 30005,
        'input2Event': 30012,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60039: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60038,
        'input1Event': 30012,
        'input2Event': 30005,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60041: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60040,
        'input1Event': 30020,
        'input2Event': 30019,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60043: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60042,
        'input1Event': 30019,
        'input2Event': 30020,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60047: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60045,
        'input1Event': 10002,
        'input2Event': 30019,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60049: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60048,
        'input1Event': 30003,
        'input2Event': 10052,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60051: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60050,
        'input1Event': 30001,
        'input2Event': 10052,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60053: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60052,
        'input1Event': 30021,
        'input2Event': 30016,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60055: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60054,
        'input1Event': 30002,
        'input2Event': 30021,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60057: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60056,
        'input1Event': 30016,
        'input2Event': 30021,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60059: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60058,
        'input1Event': 30012,
        'input2Event': 30011,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60061: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60060,
        'input1Event': 30012,
        'input2Event': 30013,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60064: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60062,
        'input1Event': 30005,
        'input2Event': 30011,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60065: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60063,
        'input1Event': 30005,
        'input2Event': 30013,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60074: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60072,
        'input1Event': 10052,
        'input2Event': 30003,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60075: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60073,
        'input1Event': 10052,
        'input2Event': 30001,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60076: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60020,
        'input1Event': 30021,
        'input2Event': 30002,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60078: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60077,
        'input1Event': 30021,
        'input2Event': 30002,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60080: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60079,
        'input1Event': 60057,
        'input2Event': 30002,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60082: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60081,
        'input1Event': 60055,
        'input2Event': 30016,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60084: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60083,
        'input1Event': 30004,
        'input2Event': 30014,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60086: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60085,
        'input1Event': 30006,
        'input2Event': 30008,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60091: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60087,
        'input1Event': 60088,
        'input2Event': 30001,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60093: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60092,
        'input1Event': 30001,
        'input2Event': 60088,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60100: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60099,
        'input1Event': 60095,
        'input2Event': 10002,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60119: {
        'type': 'logicGate',
        'name': 'open sesame Duct & Lobby',
        'comment': 'links together the Duct Room and Lobby buttons',
        'parentEntId': 0,
        'input1Event': 30076,
        'input2Event': 60118,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'or'
    },
    60132: {
        'type': 'logicGate',
        'name': 'open sesame Entrances',
        'comment': 'links together the buttons in the two entrances',
        'parentEntId': 0,
        'input1Event': 30040,
        'input2Event': 60102,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'or'
    },
    60138: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60137,
        'input1Event': 60095,
        'input2Event': 60094,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60141: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60139,
        'input1Event': 10002,
        'input2Event': 60094,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    60142: {
        'type': 'logicGate',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 60140,
        'input1Event': 10002,
        'input2Event': 60095,
        'isInput1': 0,
        'isInput2': 0,
        'logicType': 'and'
    },
    10001: {
        'type': 'model',
        'name': 'dropshadow',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(0, 0, -25),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(2, 1.5, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_3/models/props/drop_shadow.bam'
    },
    10012: {
        'type': 'model',
        'name': 'backCrate',
        'comment': '',
        'parentEntId': 10067,
        'pos': Point3(0, -5.8149600000000001, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    10033: {
        'type': 'model',
        'name': 'dropshadow',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(0, 0, -25),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(2, 1.5, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_3/models/props/drop_shadow.bam'
    },
    10045: {
        'type': 'model',
        'name': 'dropshadow',
        'comment': '',
        'parentEntId': 10008,
        'pos': Point3(0, 0, -25),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(2, 1.5, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_3/models/props/drop_shadow.bam'
    },
    10046: {
        'type': 'model',
        'name': 'dropshadow',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0, 0, -25),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(2, 1.5, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_3/models/props/drop_shadow.bam'
    },
    10050: {
        'type': 'model',
        'name': 'sky',
        'comment': '',
        'parentEntId': 200,
        'pos': Point3(-142.02000000000001, 437.22699999999998,
                      0.92249099999999995),
        'hpr': Point3(0, 0, 0),
        'scale': Point3(2.5, 2.5, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/cog_sky.bam'
    },
    10066: {
        'type': 'model',
        'name': 'frontCrate',
        'comment': '',
        'parentEntId': 10067,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    10069: {
        'type': 'model',
        'name': 'backCrate',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(0, -5.8149600000000001, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    10070: {
        'type': 'model',
        'name': 'frontCrate',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    20082: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        5,
        'pos':
        Point3(4.5081499999999997, 11.6508, 0),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        Point3(0.92000000000000004, 0.92000000000000004, 0.92000000000000004),
        'collisionsOnly':
        0,
        'flattenType':
        'light',
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_9/models/cogHQ/metal_crateB.bam'
    },
    20083: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20082,
        'pos': Point3(0, 0, 5.5),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    20088: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20087,
        'pos': Point3(1, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1.3, 1, 1.3),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/metal_crateB.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'gearGauntletObstacle',
        'comment': '',
        'parentEntId': 10027,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10004: {
        'type': 'nodepath',
        'name': 'gearGauntlet',
        'comment': 'gears are staggered 15 ft in Y',
        'parentEntId': 10000,
        'pos': Point3(0, -23.25, 6.8499999999999996),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10014: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, 34.07, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10015: {
        'type': 'nodepath',
        'name': 'paint mixer platforms',
        'comment': '',
        'parentEntId': 10,
        'pos': Point3(0, 5.1513600000000004, -2),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10022: {
        'type': 'nodepath',
        'name': 'gagBarrels',
        'comment': '',
        'parentEntId': 11,
        'pos': Point3(11.232799999999999, 14.7959, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10023: {
        'type': 'nodepath',
        'name': 'leftCogs',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(-42.036299999999997, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10027: {
        'type': 'nodepath',
        'name': 'zoneNodeCompensate',
        'comment': 'I think the ZoneNode was moved.',
        'parentEntId': 19,
        'pos': Point3(-0.42648200000000003, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    10030: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 8,
        'pos': Point3(2.5, 62.5, 10),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10032: {
        'type': 'nodepath',
        'name': 'rightCogs',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(46.880000000000003, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    10034: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 22,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(180, 0, 0),
        'scale': 1
    },
    10036: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(5.5, 0, 0),
        'hpr': Point3(161, 0, 0),
        'scale': 1
    },
    10037: {
        'type':
        'nodepath',
        'name':
        'cogs',
        'comment':
        '',
        'parentEntId':
        7,
        'pos':
        Point3(3.1000000000000001, -48.270000000000003, 0.050000000000000003),
        'hpr':
        Point3(0, 0, 0),
        'scale':
        1
    },
    10040: {
        'type': 'nodepath',
        'name': 'FactoryBoss',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(0, 68.445700000000002, 9.5669000000000004),
        'hpr': Point3(180, 0, 0),
        'scale': 1
    },
    10047: {
        'type': 'nodepath',
        'name': 'battleCell',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    10056: {
        'type': 'nodepath',
        'name': 'sounds',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 15),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    10064: {
        'type': 'nodepath',
        'name': 'battleCell',
        'comment': '',
        'parentEntId': 32,
        'pos': Point3(0, -5.2044699999999997, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    10065: {
        'type': 'nodepath',
        'name': 'backSteps',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 56.2652, 0),
        'hpr': Point3(0, 0, 0),
        'scale': Point3(1.5, 1.3, 0.72999999999999998)
    },
    10067: {
        'type': 'nodepath',
        'name': 'frontSteps',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, -44.7196, 0),
        'hpr': Point3(180, 0, 0),
        'scale': Point3(1.5, 1.3, 0.72905699999999996)
    },
    10068: {
        'type': 'nodepath',
        'name': 'battleCell',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20000: {
        'type': 'nodepath',
        'name': 'stompers',
        'comment': '',
        'parentEntId': 17,
        'pos': Point3(0.75, 0, 0.5),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20018: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10014,
        'pos': Point3(0, -24, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20019: {
        'type': 'nodepath',
        'name': 'cogsJoin',
        'comment': '',
        'parentEntId': 10030,
        'pos': Point3(16, 2, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20022: {
        'type': 'nodepath',
        'name': 'StomperButtonsNodepath',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(-11.75, -35.799999999999997, 14.9),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20023: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20037: {
        'type': 'nodepath',
        'name': 'SignatureGoonNP',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(-48.444200000000002, -24.938500000000001, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20058: {
        'type': 'nodepath',
        'name': 'SigRoomCogs',
        'comment': '',
        'parentEntId': 24,
        'pos': Point3(-1.0928, -45, 14.99),
        'hpr': Point3(90, 0, 0),
        'scale': 1
    },
    20087: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 17,
        'pos': Point3(-4, -117, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20094: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(-0.72050599999999998, 27.546099999999999, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    20095: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 32,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1
    },
    20096: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(4.8492100000000002, 8.7448200000000007, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    10017: {
        'type':
        'paintMixer',
        'name':
        'fifth',
        'comment':
        '',
        'parentEntId':
        10015,
        'pos':
        Point3(5.2400000000000002, 23.52, 8),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        1,
        'floorName':
        'PaintMixerFloorCollision',
        'modelPath':
        'phase_9/models/cogHQ/PaintMixer',
        'modelScale':
        Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004),
        'motion':
        'easeInOut',
        'offset':
        Point3(-12, -6, 0),
        'period':
        8.0,
        'phaseShift':
        0.5,
        'shaftScale':
        1,
        'waitPercent':
        0.10000000000000001
    },
    10018: {
        'type':
        'paintMixer',
        'name':
        'fourth',
        'comment':
        '',
        'parentEntId':
        10015,
        'pos':
        Point3(-12.1, 3, 8),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        1,
        'floorName':
        'PaintMixerFloorCollision',
        'modelPath':
        'phase_9/models/cogHQ/PaintMixer',
        'modelScale':
        Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004),
        'motion':
        'easeInOut',
        'offset':
        Point3(0, -6, 15),
        'period':
        8.0,
        'phaseShift':
        0.0,
        'shaftScale':
        2.5,
        'waitPercent':
        0.10000000000000001
    },
    10019: {
        'type':
        'paintMixer',
        'name':
        'third',
        'comment':
        '',
        'parentEntId':
        10015,
        'pos':
        Point3(-3.85419, -7.7575099999999999, 22.583600000000001),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        1,
        'floorName':
        'PaintMixerFloorCollision',
        'modelPath':
        'phase_9/models/cogHQ/PaintMixer',
        'modelScale':
        Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004),
        'motion':
        'easeInOut',
        'offset':
        Point3(7, 0, 0),
        'period':
        8.0,
        'phaseShift':
        0.0,
        'shaftScale':
        2.5,
        'waitPercent':
        0.10000000000000001
    },
    10020: {
        'type':
        'paintMixer',
        'name':
        'second',
        'comment':
        '',
        'parentEntId':
        10015,
        'pos':
        Point3(16.010000000000002, -6.4699999999999998, 23),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        1,
        'floorName':
        'PaintMixerFloorCollision',
        'modelPath':
        'phase_9/models/cogHQ/PaintMixer',
        'modelScale':
        Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004),
        'motion':
        'easeInOut',
        'offset':
        Point3(-4, -8, -15),
        'period':
        8.0,
        'phaseShift':
        0.0,
        'shaftScale':
        2.5,
        'waitPercent':
        0.10000000000000001
    },
    10054: {
        'type':
        'paintMixer',
        'name':
        'first',
        'comment':
        '',
        'parentEntId':
        10015,
        'pos':
        Point3(-10, -26.100000000000001, 8),
        'hpr':
        Vec3(0, 0, 0),
        'scale':
        1,
        'floorName':
        'PaintMixerFloorCollision',
        'modelPath':
        'phase_9/models/cogHQ/PaintMixer',
        'modelScale':
        Point3(0.80000000000000004, 0.80000000000000004, 0.80000000000000004),
        'motion':
        'easeInOut',
        'offset':
        Point3(15, 0, 0),
        'period':
        8.0,
        'phaseShift':
        0.0,
        'shaftScale':
        1,
        'waitPercent':
        0.10000000000000001
    },
    20008: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    20009: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 17,
        'pathScale': 1.0
    },
    20010: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 21,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 36,
        'pathScale': 1.0
    },
    20012: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 21,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 34,
        'pathScale': 1.0
    },
    20015: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 21,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 37,
        'pathScale': 1.0
    },
    20038: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 38,
        'pathScale': 1.0
    },
    20039: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 7,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 12,
        'pathScale': 1.0
    },
    20040: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(41.5, 33.5, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    20042: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(15, 34, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    20044: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(1.5, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'pathIndex': 6,
        'pathScale': 1.0
    },
    20045: {
        'type': 'path',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'pathIndex': 7,
        'pathScale': 1.0
    },
    20049: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 7,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 13,
        'pathScale': 1.0
    },
    20051: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(1, -24, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 42,
        'pathScale': 1.0
    },
    20053: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 8,
        'pathScale': 1.0
    },
    20055: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 9,
        'pathScale': 1.0
    },
    20059: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 10,
        'pathScale': 1.0
    },
    20061: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20037,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 11,
        'pathScale': 1.0
    },
    20067: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 39,
        'pathScale': 1.0
    },
    20068: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 15,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 40,
        'pathScale': 1.0
    },
    20069: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 9,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 5,
        'pathScale': 1.0
    },
    20070: {
        'type': 'path',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 9,
        'pos': Point3(1, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 5,
        'pathScale': 1.0
    },
    20073: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 21,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 35,
        'pathScale': 1.0
    },
    20075: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 7,
        'pos': Point3(4, 4, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 14,
        'pathScale': 1.0
    },
    20076: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 8,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 15,
        'pathScale': 1.0
    },
    20077: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 8,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 16,
        'pathScale': 1.0
    },
    20078: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 18,
        'pathScale': 1.0
    },
    20079: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 4,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    20084: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 9,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 41,
        'pathScale': 1.0
    },
    20097: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 19,
        'pathScale': 1.0
    },
    20098: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 20,
        'pathScale': 1.0
    },
    20099: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 34,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 21,
        'pathScale': 1.0
    },
    20100: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 22,
        'pathScale': 1.0
    },
    20101: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 23,
        'pathScale': 1.0
    },
    20102: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 33,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 24,
        'pathScale': 1.0
    },
    20103: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 32,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 25,
        'pathScale': 1.0
    },
    20104: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 32,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 26,
        'pathScale': 1.0
    },
    20105: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 32,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 27,
        'pathScale': 1.0
    },
    20106: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 28,
        'pathScale': 1.0
    },
    20107: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 29,
        'pathScale': 1.0
    },
    20108: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 30,
        'pathScale': 1.0
    },
    20109: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 31,
        'pathScale': 1.0
    },
    20110: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 32,
        'pathScale': 1.0
    },
    20111: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 13,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 33,
        'pathScale': 1.0
    },
    60133: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 22,
        'pos': Point3(-10, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    60134: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 22,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    60135: {
        'type': 'path',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 22,
        'pos': Point3(10, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0
    },
    10042: {
        'type': 'propSpinner',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 7
    },
    20001: {
        'type': 'stomper',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(7, 5, 7),
        'modelPath': 0,
        'motion': 3,
        'period': 4.0,
        'phaseShift': 0.0,
        'range': 30.0,
        'shaftScale': Point3(0.5, 12, 0.5),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20002: {
        'type': 'stomper',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(0, -14.3294, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(7, 5, 7),
        'modelPath': 0,
        'motion': 3,
        'period': 2.0,
        'phaseShift': 0.0,
        'range': 10.0,
        'shaftScale': Point3(0.5, 12, 0.5),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20003: {
        'type': 'stomper',
        'name': 'copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(0, -28.325199999999999, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(7, 5, 7),
        'modelPath': 0,
        'motion': 3,
        'period': 2.0,
        'phaseShift': 0.5,
        'range': 10.0,
        'shaftScale': Point3(0.5, 12, 0.5),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20004: {
        'type': 'stomper',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(-3.5, 16.258800000000001, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(3.5, 5, 3.5),
        'modelPath': 0,
        'motion': 3,
        'period': 3.0001373423482587,
        'phaseShift': 0.0,
        'range': 15.0,
        'shaftScale': Point3(0.70999999999999996, 12, 0.70999999999999996),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 0,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20005: {
        'type': 'stomper',
        'name': 'copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(3.5, 16.258800000000001, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(3.5, 5, 3.5),
        'modelPath': 0,
        'motion': 3,
        'period': 1.5,
        'phaseShift': 0.0,
        'range': 15.0,
        'shaftScale': Point3(0.70999999999999996, 12, 0.70999999999999996),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 1,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20006: {
        'type': 'stomper',
        'name': 'copy of copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(-3.5, 23.4392, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(3.5, 5, 3.5),
        'modelPath': 0,
        'motion': 3,
        'period': 1.5,
        'phaseShift': 0.5,
        'range': 15.0,
        'shaftScale': Point3(0.70999999999999996, 12, 0.70999999999999996),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 0,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20007: {
        'type': 'stomper',
        'name': 'copy of copy of copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20000,
        'pos': Point3(3.5, 23.4392, 0),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(3.5, 5, 3.5),
        'modelPath': 0,
        'motion': 3,
        'period': 3.0,
        'phaseShift': 0.5,
        'range': 15.0,
        'shaftScale': Point3(0.70999999999999996, 12, 0.70999999999999996),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 0,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20029: {
        'type': 'stomper',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20025,
        'pos': Point3(4.5, 43.5, 0.25),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'animateShadow': 0,
        'crushCellId': 20024,
        'damage': 3,
        'headScale': Point3(3, 2, 3),
        'modelPath': 0,
        'motion': 5,
        'period': 2.0,
        'phaseShift': 0.0,
        'range': 12.0,
        'shaftScale': Point3(0.66000000000000003, 37.5, 0.66000000000000003),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 20033,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20030: {
        'type': 'stomper',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 20025,
        'pos': Point3(31.5, 43.5, 0.25),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'animateShadow': 0,
        'crushCellId': 20026,
        'damage': 3,
        'headScale': Point3(3, 2, 3),
        'modelPath': 0,
        'motion': 5,
        'period': 2.0,
        'phaseShift': 0.0,
        'range': 12.0,
        'shaftScale': Point3(0.66000000000000003, 37.5, 0.66000000000000003),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 20034,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20031: {
        'type': 'stomper',
        'name': 'copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20025,
        'pos': Point3(64.5, 43.5, 0.25),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'animateShadow': 0,
        'crushCellId': 20027,
        'damage': 3,
        'headScale': Point3(3, 2, 3),
        'modelPath': 0,
        'motion': 5,
        'period': 2.0,
        'phaseShift': 0.0,
        'range': 12.0,
        'shaftScale': Point3(0.66000000000000003, 37.5, 0.66000000000000003),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 20035,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20032: {
        'type': 'stomper',
        'name': 'copy of copy of copy of <unnamed>',
        'comment': '',
        'parentEntId': 20025,
        'pos': Point3(85.5, 43.5, 0.25),
        'hpr': Point3(0, 0, 0),
        'scale': 1,
        'animateShadow': 0,
        'crushCellId': 20028,
        'damage': 3,
        'headScale': Point3(3, 2, 3),
        'modelPath': 0,
        'motion': 5,
        'period': 2.0,
        'phaseShift': 0.0,
        'range': 12.0,
        'shaftScale': Point3(0.66000000000000003, 37.5, 0.66000000000000003),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 2,
        'style': 'vertical',
        'switchId': 20036,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0
    },
    20050: {
        'type': 'trigger',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 20022,
        'pos': Point3(10, 0, 10),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(20, 20, 20),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': 1,
        'triggerName': 'signatureRoomView'
    },
    20057: {
        'type': 'trigger',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 23,
        'pos': Point3(3, -8.8000000000000007, 15.5091),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(25, 25, 25),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': 1,
        'triggerName': 'lookoutTrigger'
    },
    30077: {
        'type': 'trigger',
        'name': 'button cutscene',
        'comment': '',
        'parentEntId': 3,
        'pos': Point3(-4, 8, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'isOn': 0,
        'isOnEvent': 0,
        'secondsOn': 1,
        'triggerName': ''
    },
    10013: {
        'type': 'visibilityExtender',
        'name': 'intoEastSilo',
        'comment': '',
        'parentEntId': 60009,
        'event': 60101,
        'newZones': [61]
    },
    10043: {
        'type': 'visibilityExtender',
        'name': 'beyondLobby',
        'comment': '',
        'parentEntId': 10049,
        'event': 10057,
        'newZones': [5, 116]
    },
    10044: {
        'type': 'visibilityExtender',
        'name': 'intoEntrance1',
        'comment': '',
        'parentEntId': 10051,
        'event': 30000,
        'newZones': [3]
    },
    10058: {
        'type': 'visibilityExtender',
        'name': 'intoFarHallway',
        'comment': '',
        'parentEntId': 10049,
        'event': 10059,
        'newZones': [6, 118]
    },
    10060: {
        'type': 'visibilityExtender',
        'name': 'intoLookout',
        'comment': '',
        'parentEntId': 10049,
        'event': 10061,
        'newZones': [23]
    },
    10062: {
        'type': 'visibilityExtender',
        'name': 'intoLobby',
        'comment': '',
        'parentEntId': 60031,
        'event': 10063,
        'newZones': [4, 114]
    },
    30022: {
        'type': 'visibilityExtender',
        'name': 'intoLobby',
        'comment': '',
        'parentEntId': 10049,
        'event': 30000,
        'newZones': [4, 113]
    },
    30023: {
        'type': 'visibilityExtender',
        'name': 'beyond door 106',
        'comment': '',
        'parentEntId': 60017,
        'event': 30002,
        'newZones': [15, 126]
    },
    30024: {
        'type': 'visibilityExtender',
        'name': 'beyond door 106',
        'comment': '',
        'parentEntId': 60016,
        'event': 30002,
        'newZones': [16]
    },
    30025: {
        'type': 'visibilityExtender',
        'name': 'beyond door 126',
        'comment': '',
        'parentEntId': 60016,
        'event': 30021,
        'newZones': [14, 17, 121]
    },
    30026: {
        'type': 'visibilityExtender',
        'name': 'beyond door 121',
        'comment': '',
        'parentEntId': 60015,
        'event': 30016,
        'newZones': [13, 119]
    },
    30027: {
        'type': 'visibilityExtender',
        'name': 'beyond door 126',
        'comment': '',
        'parentEntId': 60015,
        'event': 30021,
        'newZones': [15, 106]
    },
    30029: {
        'type': 'visibilityExtender',
        'name': 'beyondLobby',
        'comment': '',
        'parentEntId': 10051,
        'event': 30009,
        'newZones': [5, 116]
    },
    30030: {
        'type': 'visibilityExtender',
        'name': 'beyond door 113',
        'comment': '',
        'parentEntId': 60000,
        'event': 30009,
        'newZones': [4, 114]
    },
    30031: {
        'type': 'visibilityExtender',
        'name': 'beyond door 116',
        'comment': '',
        'parentEntId': 60000,
        'event': 30011,
        'newZones': [6, 109, 117, 118]
    },
    30032: {
        'type': 'visibilityExtender',
        'name': 'intoHallwayFromLobby',
        'comment': '',
        'parentEntId': 60001,
        'event': 30011,
        'newZones': [5, 113]
    },
    30033: {
        'type': 'visibilityExtender',
        'name': 'intoBoilerRoom',
        'comment': '',
        'parentEntId': 60001,
        'event': 30012,
        'newZones': [8]
    },
    30034: {
        'type': 'visibilityExtender',
        'name': 'intoLookout',
        'comment': '',
        'parentEntId': 60001,
        'event': 30013,
        'newZones': [23, 39]
    },
    30035: {
        'type': 'visibilityExtender',
        'name': 'intoGearRoom',
        'comment': '',
        'parentEntId': 60001,
        'event': 30005,
        'newZones': [7]
    },
    30036: {
        'type': 'visibilityExtender',
        'name': 'beyond door 109',
        'comment': '',
        'parentEntId': 60002,
        'event': 30005,
        'newZones': [6, 116, 117, 118]
    },
    30037: {
        'type': 'visibilityExtender',
        'name': 'beyond door 110',
        'comment': '',
        'parentEntId': 60002,
        'event': 30006,
        'newZones': [9, 25, 26, 33, 34, 35, 38, 41, 53, 112, 115, 200]
    },
    30038: {
        'type': 'visibilityExtender',
        'name': 'beyond door 117',
        'comment': '',
        'parentEntId': 60005,
        'event': 30012,
        'newZones': [6, 109, 116, 118]
    },
    30039: {
        'type': 'visibilityExtender',
        'name': 'beyond door 108',
        'comment': '',
        'parentEntId': 60005,
        'event': 30004,
        'newZones': [12, 21, 26, 34, 35, 40, 41, 53, 60, 119, 120, 200]
    },
    30041: {
        'type': 'visibilityExtender',
        'name': 'beyond door 110',
        'comment': '',
        'parentEntId': 60003,
        'event': 30006,
        'newZones': [7]
    },
    30042: {
        'type': 'visibilityExtender',
        'name': 'beyond door 112',
        'comment': '',
        'parentEntId': 60003,
        'event': 30008,
        'newZones': [10, 11]
    },
    30043: {
        'type': 'visibilityExtender',
        'name': 'intoWarehouse',
        'comment': '',
        'parentEntId': 60003,
        'event': 30010,
        'newZones': [24, 39]
    },
    30044: {
        'type': 'visibilityExtender',
        'name': 'beyond door 112',
        'comment': '',
        'parentEntId': 60004,
        'event': 30008,
        'newZones': [9, 25, 26, 33, 34, 35, 38, 41, 53, 110, 115, 200]
    },
    30046: {
        'type': 'visibilityExtender',
        'name': 'beyond door 112',
        'comment': '',
        'parentEntId': 60066,
        'event': 30008,
        'newZones': [9, 25, 26, 41, 200]
    },
    30049: {
        'type': 'visibilityExtender',
        'name': 'beyond door 119',
        'comment': '',
        'parentEntId': 60013,
        'event': 30014,
        'newZones':
        [12, 21, 23, 26, 33, 34, 35, 41, 53, 60, 108, 112, 120, 200]
    },
    30050: {
        'type': 'visibilityExtender',
        'name': 'beyond door 121',
        'comment': '',
        'parentEntId': 60013,
        'event': 30016,
        'newZones': [14, 17, 126]
    },
    30051: {
        'type': 'visibilityExtender',
        'name': 'beyond door 121',
        'comment': '',
        'parentEntId': 60014,
        'event': 30016,
        'newZones': [13, 119]
    },
    30052: {
        'type': 'visibilityExtender',
        'name': 'beyond door 126',
        'comment': '',
        'parentEntId': 60014,
        'event': 30021,
        'newZones': [15, 106]
    },
    30055: {
        'type': 'visibilityExtender',
        'name': 'beyond door 105',
        'comment': '',
        'parentEntId': 60019,
        'event': 30001,
        'newZones': [27, 127]
    },
    30056: {
        'type': 'visibilityExtender',
        'name': 'beyond door 105',
        'comment': '',
        'parentEntId': 60018,
        'event': 30001,
        'newZones': [27, 127]
    },
    30057: {
        'type': 'visibilityExtender',
        'name': 'beyond door 103',
        'comment': '',
        'parentEntId': 60018,
        'event': 60088,
        'newZones': [17]
    },
    30059: {
        'type': 'visibilityExtender',
        'name': 'beyond door 108',
        'comment': '',
        'parentEntId': 60006,
        'event': 30004,
        'newZones': [8, 117]
    },
    30060: {
        'type': 'visibilityExtender',
        'name': 'beyond door 119',
        'comment': '',
        'parentEntId': 60006,
        'event': 30014,
        'newZones': [13, 121]
    },
    30061: {
        'type': 'visibilityExtender',
        'name': 'intoWarehouse',
        'comment': '',
        'parentEntId': 60006,
        'event': 30015,
        'newZones': [24, 39]
    },
    30062: {
        'type': 'visibilityExtender',
        'name': 'beyond door 107',
        'comment': '',
        'parentEntId': 60024,
        'event': 30003,
        'newZones': [27, 127]
    },
    30063: {
        'type': 'visibilityExtender',
        'name': 'intoHallway',
        'comment': '',
        'parentEntId': 60031,
        'event': 30013,
        'newZones': [6, 109, 116, 117]
    },
    30064: {
        'type': 'visibilityExtender',
        'name': 'beyondLowerWestDoor',
        'comment': '',
        'parentEntId': 60007,
        'event': 30015,
        'newZones': [12, 21, 26, 34, 40, 41, 53, 200]
    },
    30066: {
        'type': 'visibilityExtender',
        'name': 'beyondLowerEastDoor',
        'comment': '',
        'parentEntId': 60007,
        'event': 30010,
        'newZones': [9, 25, 26, 33, 38, 41, 200]
    },
    30067: {
        'type': 'visibilityExtender',
        'name': 'beyondUpperEastDoor',
        'comment': '',
        'parentEntId': 60007,
        'event': 30019,
        'newZones': [9, 33, 38, 41, 200, 222]
    },
    30069: {
        'type': 'visibilityExtender',
        'name': 'beyond door 118',
        'comment': '',
        'parentEntId': 60000,
        'event': 30068,
        'newZones': [23]
    },
    30071: {
        'type': 'visibilityExtender',
        'name': 'intoLobby',
        'comment': '',
        'parentEntId': 60001,
        'event': 60030,
        'newZones': [4, 114]
    },
    30073: {
        'type': 'visibilityExtender',
        'name': 'intoLobbyHallway',
        'comment': '',
        'parentEntId': 60031,
        'event': 60033,
        'newZones': [5, 113]
    },
    30075: {
        'type': 'visibilityExtender',
        'name': 'intoGearRoom',
        'comment': '',
        'parentEntId': 60031,
        'event': 60034,
        'newZones': [7]
    },
    60008: {
        'type': 'visibilityExtender',
        'name': 'beyondUpperWestDoor',
        'comment': '',
        'parentEntId': 60007,
        'event': 30020,
        'newZones': [12, 21, 34, 40, 41, 60, 127, 200]
    },
    60010: {
        'type': 'visibilityExtender',
        'name': 'intoWarehouse',
        'comment': '',
        'parentEntId': 60009,
        'event': 30019,
        'newZones': [24, 39, 125]
    },
    60012: {
        'type': 'visibilityExtender',
        'name': 'beyond door 125',
        'comment': '',
        'parentEntId': 60011,
        'event': 30020,
        'newZones': [24, 39, 124]
    },
    60020: {
        'type': 'visibilityExtender',
        'name': 'beyond door 106',
        'comment': '',
        'parentEntId': 60015,
        'event': 60076,
        'newZones': [16]
    },
    60021: {
        'type': 'visibilityExtender',
        'name': 'beyond door 116',
        'comment': '',
        'parentEntId': 10051,
        'event': 60023,
        'newZones': [6, 118]
    },
    60022: {
        'type': 'visibilityExtender',
        'name': 'beyond door 118',
        'comment': '',
        'parentEntId': 10051,
        'event': 60025,
        'newZones': [23]
    },
    60026: {
        'type': 'visibilityExtender',
        'name': 'beyond door 109',
        'comment': '',
        'parentEntId': 60000,
        'event': 60028,
        'newZones': [7]
    },
    60027: {
        'type': 'visibilityExtender',
        'name': 'beyond door 117',
        'comment': '',
        'parentEntId': 60000,
        'event': 60029,
        'newZones': [8]
    },
    60032: {
        'type': 'visibilityExtender',
        'name': 'intoBoilerRoom',
        'comment': '',
        'parentEntId': 60031,
        'event': 60035,
        'newZones': [8]
    },
    60036: {
        'type': 'visibilityExtender',
        'name': 'beyond door 117',
        'comment': '',
        'parentEntId': 60002,
        'event': 60037,
        'newZones': [8]
    },
    60038: {
        'type': 'visibilityExtender',
        'name': 'beyond door 109',
        'comment': '',
        'parentEntId': 60005,
        'event': 60039,
        'newZones': [7]
    },
    60040: {
        'type': 'visibilityExtender',
        'name': 'beyond door 124',
        'comment': '',
        'parentEntId': 60011,
        'event': 60041,
        'newZones': [38]
    },
    60042: {
        'type': 'visibilityExtender',
        'name': 'beyondWarehouse',
        'comment': '',
        'parentEntId': 60009,
        'event': 60043,
        'newZones': [12, 200]
    },
    60045: {
        'type': 'visibilityExtender',
        'name': 'beyond door 124',
        'comment': '',
        'parentEntId': 60044,
        'event': 60047,
        'newZones': [24]
    },
    60046: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60044,
        'event': 10002,
        'newZones': [31]
    },
    60048: {
        'type': 'visibilityExtender',
        'name': 'beyond door 127',
        'comment': '',
        'parentEntId': 60024,
        'event': 60049,
        'newZones': [21, 200]
    },
    60050: {
        'type': 'visibilityExtender',
        'name': 'beyond door 127',
        'comment': '',
        'parentEntId': 60019,
        'event': 60051,
        'newZones': [21, 34, 200]
    },
    60052: {
        'type': 'visibilityExtender',
        'name': 'beyond door 121',
        'comment': '',
        'parentEntId': 60016,
        'event': 60053,
        'newZones': [13, 119]
    },
    60054: {
        'type': 'visibilityExtender',
        'name': 'beyond door 126',
        'comment': '',
        'parentEntId': 60017,
        'event': 60055,
        'newZones': [14, 17, 121]
    },
    60056: {
        'type': 'visibilityExtender',
        'name': 'beyond door 126',
        'comment': '',
        'parentEntId': 60013,
        'event': 60057,
        'newZones': [15, 106]
    },
    60058: {
        'type': 'visibilityExtender',
        'name': 'beyond door 116',
        'comment': '',
        'parentEntId': 60005,
        'event': 60059,
        'newZones': [5]
    },
    60060: {
        'type': 'visibilityExtender',
        'name': 'beyond door 118',
        'comment': '',
        'parentEntId': 60005,
        'event': 60061,
        'newZones': [23]
    },
    60062: {
        'type': 'visibilityExtender',
        'name': 'beyond door 116',
        'comment': '',
        'parentEntId': 60002,
        'event': 60064,
        'newZones': [5]
    },
    60063: {
        'type': 'visibilityExtender',
        'name': 'beyond door 118',
        'comment': '',
        'parentEntId': 60002,
        'event': 60065,
        'newZones': [23]
    },
    60068: {
        'type': 'visibilityExtender',
        'name': 'beyond door 105',
        'comment': '',
        'parentEntId': 60067,
        'event': 30001,
        'newZones': [18, 19, 20, 131]
    },
    60069: {
        'type': 'visibilityExtender',
        'name': 'beyond door 107',
        'comment': '',
        'parentEntId': 60067,
        'event': 30003,
        'newZones': [22]
    },
    60070: {
        'type': 'visibilityExtender',
        'name': 'beyond door 127',
        'comment': '',
        'parentEntId': 60067,
        'event': 10052,
        'newZones': [12, 21, 26, 34, 35, 40, 41, 53, 60, 200]
    },
    60071: {
        'type': 'visibilityExtender',
        'name': 'beyond door 127',
        'comment': '',
        'parentEntId': 60006,
        'event': 10052,
        'newZones': [27, 105, 107]
    },
    60072: {
        'type': 'visibilityExtender',
        'name': 'beyond door 107',
        'comment': '',
        'parentEntId': 60006,
        'event': 60074,
        'newZones': [22]
    },
    60073: {
        'type': 'visibilityExtender',
        'name': 'beyond door 105',
        'comment': '',
        'parentEntId': 60006,
        'event': 60075,
        'newZones': [18]
    },
    60077: {
        'type': 'visibilityExtender',
        'name': 'beyond door 106',
        'comment': '',
        'parentEntId': 60014,
        'event': 60078,
        'newZones': [16]
    },
    60079: {
        'type': 'visibilityExtender',
        'name': 'beyond door 106',
        'comment': '',
        'parentEntId': 60013,
        'event': 60080,
        'newZones': [16]
    },
    60081: {
        'type': 'visibilityExtender',
        'name': 'beyond door 121',
        'comment': '',
        'parentEntId': 60017,
        'event': 60082,
        'newZones': [13]
    },
    60083: {
        'type': 'visibilityExtender',
        'name': 'beyond door 119',
        'comment': '',
        'parentEntId': 60005,
        'event': 60084,
        'newZones': [13]
    },
    60085: {
        'type': 'visibilityExtender',
        'name': 'beyond door 112',
        'comment': '',
        'parentEntId': 60002,
        'event': 60086,
        'newZones': [10]
    },
    60087: {
        'type': 'visibilityExtender',
        'name': 'beyond door 105',
        'comment': '',
        'parentEntId': 60015,
        'event': 60091,
        'newZones': [27]
    },
    60089: {
        'type': 'visibilityExtender',
        'name': 'beyond door 103',
        'comment': '',
        'parentEntId': 60019,
        'event': 60088,
        'newZones': [17]
    },
    60090: {
        'type': 'visibilityExtender',
        'name': 'beyond door 103',
        'comment': '',
        'parentEntId': 60015,
        'event': 60088,
        'newZones': [18, 19, 105]
    },
    60092: {
        'type': 'visibilityExtender',
        'name': 'beyond door 103',
        'comment': '',
        'parentEntId': 60067,
        'event': 60093,
        'newZones': [17]
    },
    60097: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60096,
        'event': 60095,
        'newZones': [33, 34, 35, 36, 37, 60, 61, 128, 129, 200]
    },
    60098: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60044,
        'event': 60095,
        'newZones': [30]
    },
    60099: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60096,
        'event': 60100,
        'newZones': [31]
    },
    60106: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60011,
        'event': 60094,
        'newZones': [32]
    },
    60107: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60011,
        'event': 60095,
        'newZones': [30]
    },
    60109: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60108,
        'event': 60094,
        'newZones': [32]
    },
    60110: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60108,
        'event': 60095,
        'newZones': [30]
    },
    60112: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60111,
        'event': 60094,
        'newZones': [32]
    },
    60113: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60111,
        'event': 60095,
        'newZones': [30]
    },
    60115: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60114,
        'event': 60094,
        'newZones': [32]
    },
    60116: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60114,
        'event': 60095,
        'newZones': [30]
    },
    60117: {
        'type': 'visibilityExtender',
        'name': 'beyond door 103',
        'comment': '',
        'parentEntId': 60014,
        'event': 60088,
        'newZones': [18]
    },
    60120: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60108,
        'event': 10002,
        'newZones': [31]
    },
    60122: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60121,
        'event': 10002,
        'newZones': [33, 34, 35, 36, 37, 60, 61, 128, 129, 130, 200]
    },
    60123: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60111,
        'event': 10002,
        'newZones': []
    },
    60124: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60114,
        'event': 10002,
        'newZones': [31]
    },
    60125: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60011,
        'event': 10002,
        'newZones': [31]
    },
    60127: {
        'type': 'visibilityExtender',
        'name': 'beyond door 128',
        'comment': '',
        'parentEntId': 60126,
        'event': 10002,
        'newZones': [31]
    },
    60128: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60126,
        'event': 60094,
        'newZones': [32]
    },
    60129: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60126,
        'event': 60095,
        'newZones': [30]
    },
    60131: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60130,
        'event': 60094,
        'newZones': [33, 34, 35, 36, 37, 60, 61, 128, 130, 200]
    },
    60136: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60044,
        'event': 60094,
        'newZones': [32]
    },
    60137: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60096,
        'event': 60138,
        'newZones': [32]
    },
    60139: {
        'type': 'visibilityExtender',
        'name': 'beyond door 129',
        'comment': '',
        'parentEntId': 60121,
        'event': 60141,
        'newZones': [32]
    },
    60140: {
        'type': 'visibilityExtender',
        'name': 'beyond door 130',
        'comment': '',
        'parentEntId': 60121,
        'event': 60142,
        'newZones': [30]
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}
