#https://codecombat.com/play/level/the-gauntlet
# Используйте то, что вы изучили, чтобы победить огров.
# Remember: it takes two attacks to defeat an ogre munchkin!
while True:
    self.moveRight()
    self.attack(self.findNearestEnemy())
    self.attack(self.findNearestEnemy())
