from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyDanceActivityBaseAI import DistributedPartyDanceActivityBaseAI


class DistributedPartyDance20ActivityAI(DistributedPartyDanceActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        "DistributedPartyDance20ActivityAI")
