# coding=utf-8
import mcpi.minecraft as minecraft

#NOTA - sostituire l'indirizzo IP 127.0.0.1 con quello del server a cui
# si è collegati e "rodmcban" con il nome del proprio personaggio
mc = minecraft.Minecraft.create(address="127.0.0.1", name="talete")

###x = -33
###y = 20
###z = 34

###mc.player.setPos(x, y, z)
mc.player.setPos(-33, 20, 34)


