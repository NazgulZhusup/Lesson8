from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Crossbow(Weapon):
    def attack(self):
        return "стреляет из арбалета"


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack_monster(self, monster):
        action = self.weapon.attack()
        print(f"Боец {action}.")
        monster.defeat()


class Monster:
    def defeat(self):
        print("Монстр побежден!")


def demonstrate_battle():
    monster = Monster()

    fighter = Fighter(Sword())
    print("Боец выбирает меч.")
    fighter.attack_monster(monster)

    print("\nБоец выбирает лук.")
    fighter.change_weapon(Bow())
    fighter.attack_monster(monster)

    print("\nБоец выбирает арбалет.")
    fighter.change_weapon(Crossbow())
    fighter.attack_monster(monster)


demonstrate_battle()
