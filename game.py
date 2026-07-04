import random

class GameEngine:
    def __init__(self):
        self.resources = {"grain": 200, "wood": 100, "iron": 50}
        self.farmers = 5
        self.tech_level = 1
        self.building_queue = []
        self.hero = {"name": "Zhao Yun", "power": 100, "troop": "cavalry"}
        
    def farm_resources(self):
        for res in self.resources:
            self.resources[res] += self.farmers * 5 * self.tech_level
        print("Resources updated.")

    def add_to_queue(self, building_name):
        if len(self.building_queue) == 0:
            self.building_queue.append(building_name)
            print(f"Construction started: {building_name}")
        else:
            print("Queue busy.")

    def finish_construction(self):
        if self.building_queue:
            self.building_queue.pop(0)
            self.tech_level += 1
            print(f"Tech upgraded to level {self.tech_level}")
        else:
            print("No active construction.")

    def challenge_stage(self, enemy_power, enemy_troop):
        rules = {"cavalry": "archer", "archer": "infantry", "infantry": "cavalry"}
        bonus = 1.5 if rules.get(self.hero["troop"]) == enemy_troop else 1.0
        final_power = self.hero["power"] * self.tech_level * bonus
        
        if final_power >= enemy_power:
            print("Victory!")
            return True
        else:
            print("Failure!")
            return False

def main():
    game = GameEngine()
    game.farm_resources()
    game.add_to_queue("Academy")
    game.finish_construction()
    game.challenge_stage(250, "archer")

if __name__ == "__main__":
    main()
