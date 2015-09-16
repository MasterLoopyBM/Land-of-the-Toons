import ZoneIDs

def Plaza(id, name):
	Plaza = ZoneIDs.ZoneIDs(1000)

environ = loader.loadModel('resrc/phase_4/models/neighborhoods/toontown_central.bam')
environ.reparentTo(render)
environ.setPos(10,-135,0)
environ.setHpr(0,0,0)
environ.setScale(3.15)
crate1 = loader.loadModel('resrc/phase_10/models/cashbotHQ/CBWoodCrate.bam')
crate1.reparentTo(render)
crate1.setPos(19,-147.5,0)
crate1.setHpr(0,0,0)
crate1.setScale(0.85)