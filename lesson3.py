import time
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create(address="192.168.12.10", name="Piedo@piedone")

acqua_ferma = 9
acqua_corrente = 8
oro = 41

while True:
	#Retrieve the current player's X, Y, and Z coordinates
	pos = mc.player.getPos()
	#Store the current player's coordinates in our variables x/y/z
	x = pos.x
	y = pos.y
	z = pos.z
	blocco_sotto = mc.getBlock(x, y - 1, z)
	if blocco_sotto == acqua_ferma or blocco_sotto == acqua_corrente:
		mc.setBlock(x, y-1, z, oro)
	altro_blocco = mc.getBlock(x-1, y-1, z)
	if altro_blocco == acqua_ferma or altro_blocco == acqua_corrente:
		mc.setBlock(x-1, y-1, z, oro)
	altro_blocco = mc.getBlock(x+1, y-1, z)
	if altro_blocco == acqua_ferma or altro_blocco == acqua_corrente:
		mc.setBlock(x+1, y-1, z, oro)
	altro_blocco = mc.getBlock(x, y-1, z-1)
	if altro_blocco == acqua_ferma or altro_blocco == acqua_corrente:
		mc.setBlock(x, y-1, z-1, oro)
	altro_blocco = mc.getBlock(x, y-1, z+1)
	if altro_blocco == acqua_ferma or altro_blocco == acqua_corrente:
		mc.setBlock(x, y-1, z+1, oro)
	time.sleep(0.2)
 
