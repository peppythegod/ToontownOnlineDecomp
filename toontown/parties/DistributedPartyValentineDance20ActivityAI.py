from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyDanceActivityBaseAI import DistributedPartyDanceActivityBaseAI


class DistributedPartyValentineDance20ActivityAI(
        DistributedPartyDanceActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        "DistributedPartyValentineDance20ActivityAI")
