# coding=utf-8
import mcpi.minecraft as minecraft

#NOTA - sostituire l'indirizzo IP 192.168.12.10 con quello del server a cui
# si è collegati e "rodmcban" con il nome del proprio personaggio
mc = minecraft.Minecraft.create(address="192.168.12.10", name="rodmcban")

###x = -33
###y = 20
###z = 34

###mc.player.setPos(x, y, z)
mc.player.setPos(-33, 20, 34)


