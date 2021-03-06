#http://codecombat.com/play/level/borrowed-sword
# На этом уровне ваш герой не должен сражаться.
# Прикажите вашим лучникам стрелять во врагов с наибольшим уровнем здоровья!
def сommandTroops():
    for index, friend in enumerate(self.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)

def CommandArcher(soldier):
    target = None
    leastHealth = 0
    enemyIndex = 0
    enemies = self.findEnemies()
    # Просмотрите всех врагов.
    while enemyIndex<len(enemies):
        if(enemies[enemyIndex].health>leastHealth):
            leastHealth = enemies[enemyIndex].health
            target = enemies[enemyIndex]
        enemyIndex = enemyIndex + 1
    if target:
        self.command(soldier, "attack", target)
loop:
    сommandTroops()
