attacks = {
    "tackle": {
        "name": "Tackle",
        "factor": 3/2,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Tackles the enemy very hard.",
        "type": "normal",
        "effect": None,
        "ap": 30,
    },
    "pick": {
        "name": "Pick",
        "factor": 1.7,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A pick at the enemys weakest spot.",
        "type": "flying",
        "effect": None,
        "ap": 30,
    },
    "apple_drop": {
        "name": "Apple drop",
        "factor": 1.7,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Lets an apple drop on the enemys head.",
        "type": "plant",
        "effect": None,
        "ap": 30,
    },
    "eye_pick": {
        "name": "Eye pick",
        "factor": 2.5,
        "action": "enem.miss_chance += 2",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.6,
        "min_lvl": 0,
        "desc": "Picks out one of the enemys eyes.",
        "type": "flying",
        "effect": None,
        "ap": 10,
    },
    "earch_quake": {
        "name": "Earch quake",
        "factor": 4,
        "action": "",
        "move": ["pound"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Brings the earth to shift.",
        "type": "ground",
        "effect": None,
        "ap": 10,
    },
    "wing_hit": {
        "name": "Wing hit",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 0,
        "desc": "Hits the enemy with a wing.",
        "type": "flying",
        "effect": None,
        "ap": 10,
    },
    "super_sucker": {
        "name": "Super sucker",
        "factor": 0,
        "action": "enem.hp -=2; self.hp +=2 if self.hp+2 <= self.full_hp else 0",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 2 HP from the enemy and adds it to it's own.",
        "type": "plant",
        "effect": None,
        "ap": 10,
    },
    "sucker": {
        "name": "Sucker",
        "factor": 0,
        "action": "enem.hp -=1; self.hp +=1 if self.hp+1 <= self.full_hp else 0",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 1 HP from the enemy and adds it to it's own.",
        "type": "plant",
        "effect": None,
        "ap": 20,
    },
    "brooding": {
        "name": "Brooding",
        "factor": 0,
        "action": "self.hp += 2 if self.hp+2 <= self.full_hp else 0",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Regenerates 2 HP.",
        "type": "normal",
        "effect": None,
        "ap": 10,
    },
    "pepple_fire": {
        "name": "Pepple fire",
        "factor": 1,
        "action": "enem.miss_chance += 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Fires pepples at the enemy and makes it blind.",
        "type": "stone",
        "effect": None,
        "ap": 5,
    },
    "cry": {
        "name": "Cry",
        "factor": 0,
        "action": "enem.miss_chance += 1",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "So loud, it confuses the enemy.",
        "type": "normal",
        "effect": None,
        "ap": 10,
    },
    "bite": {
        "name": "Bite",
        "factor": 1.75,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A hard bite the sharp teeth.",
        "type": "normal",
        "effect": None,
        "ap": 30,
    },
    "power_bite": {
        "name": "Power bite",
        "factor": 8,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 30,
        "desc": "The hardest bite you can think of.",
        "type": "normal",
        "effect": None,
        "ap": 5,
    },
    "politure": {
        "name": "Politure",
        "factor": 0,
        "action": "self.defense += 1; self.atc += 1",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Upgrades defense and attack points.",
        "type": "stone",
        "effect": None,
        "ap": 15,
    },
    "bark_hardening": {
        "name": "Bark hardening",
        "factor": 0,
        "action": "self.defense += 1",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Hardens the bark to protect it better.",
        "type": "plant",
        "effect": None,
        "ap": 15,
    },
    "chocer": {
        "name": "Chocer",
        "factor": 1,
        "action": "enem.atc -= 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Choces the enemy and makes it weaker.",
        "type": "normal",
        "effect": "EffectParalyzation",
        "ap": 15,
    },
    "poison_bite": {
        "name": "Poison bite",
        "factor": 1,
        "action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Makes the enemy weaker.",
        "type": "normal",
        "effect": "EffectPoison",
        "ap": 10,
    },
    "power_pick": {
        "name": "Power pick",
        "factor": 2,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.4,
        "min_lvl": 0,
        "desc": "A harsh picking on the enemys head.",
        "type": "flying",
        "effect": None,
        "ap": 10,
    },
    "bubble_bomb": {
        "name": "Bubble bomb",
        "factor": 6,
        "action": "enem.miss_chance += 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "A deadly bubble.",
        "type": "water",
        "effect": None,
        "ap": 10,
    },
    "bubble_shield": {
        "name": "Bubble shield",
        "factor": 0,
        "action": "self.defense += 2",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Creates a giant bubble that protects the Pokete.",
        "type": "water",
        "effect": None,
        "ap": 10,
    },
    "mind_blow": {
        "name": "Mind blow",
        "factor": 0,
        "action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Causes confusion deep in the enemys mind.",
        "type": "undead",
        "effect": "EffectConfusion",
        "ap": 15,
    },
    "tail_wipe": {
        "name": "Tail wipe",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 10,
        "desc": "Wipes throught the enemys face.",
        "type": "normal",
        "effect": None,
        "ap": 10,
    },
    "meat_skewer": {
        "name": "Meat skewer",
        "factor": 3.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.7,
        "min_lvl": 0,
        "desc": "Drills the horn deep in the enemys flesh.",
        "type": "normal",
        "effect": None,
        "ap": 10,
    },
    "fire_bite": {
        "name": "Fire bite",
        "factor": 2,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Burns and bites the enemy at the same time.",
        "type": "fire",
        "effect": "EffectBurning",
        "ap": 15,
    },
    "ash_throw": {
        "name": "Ash throw",
        "factor": 0.5,
        "action": "enem.miss_chance += 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Throws ashes in the enemys eyes.",
        "type": "fire",
        "effect": None,
        "ap": 15,
    },
    "fire_ball": {
        "name": "Fire ball",
        "factor": 4,
        "action": "",
        "move": ["fireball"],
        "miss_chance": 0,
        "min_lvl": 25,
        "desc": "Casts a fireball at the enemy.",
        "type": "fire",
        "effect": None,
        "ap": 10,
    },
    "power_roll": {
        "name": "Power roll",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Rolls over the enemy.",
        "type": "ground",
        "effect": None,
        "ap": 15,
    },
    "wet_slap": {
        "name": "Wet slap",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Gives the enemy a wet and cold slap in the face.",
        "type": "water",
        "effect": None,
        "ap": 15,
    },
    "brick_throw": {
        "name": "Brick throw",
        "factor": 2,
        "action": "",
        "move": ["throw"],
        "miss_chance": 0.3,
        "min_lvl": 15,
        "desc": "Throws an euler brick at the enemy.",
        "type": "stone",
        "effect": None,
        "ap": 20,
    },
    "shell_pinch": {
        "name": "Shell pinch",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Pinches the enemy with its strong shells.",
        "type": "water",
        "effect": None,
        "ap": 20,
    },
    "branch_stab": {
        "name": "Branch stab",
        "factor": 4,
        "action": "enem.miss_chance += 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Stabs the enemy with a branch, preferably in the enemys eyes.",
        "type": "plant",
        "effect": None,
        "ap": 10,
    },
    "snooze": {
        "name": "Snooze",
        "factor": 0,
        "action": "enem.miss_chance += 0.5; enem.atc -= 1; enem.defense -= 1",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Makes the enemy sleepy.",
        "type": "normal",
        "effect": "EffectSleep",
        "ap": 15,
    },
    "heart_touch": {
        "name": "Heart touch",
        "factor": 4,
        "action": "enem.defense -= 4",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Touches the enemys heard with its' cold gost claws.",
        "type": "undead",
        "effect": None,
        "ap": 10,
    },
    "shock": {
        "name": "Shock",
        "factor": 3/2,
        "action": "",
        "move": ["arch"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Gives the enemy a shock.",
        "type": "electro",
        "effect": None,
        "ap": 30,
    },
    "charging": {
        "name": "Charging",
        "factor": 0,
        "action": "self.atc += 2",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 10,
        "desc": "Charges the Pokete.",
        "type": "electro",
        "effect": None,
        "ap": 15,
    },
    "mega_arch": {
        "name": "Mega arch",
        "factor": 5,
        "action": "",
        "move": ["arch"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Gives the enemy heavy a shock.",
        "type": "electro",
        "effect": "EffectParalyzation",
        "ap": 10,
    },
    "root_strangler": {
        "name": "Root strangler",
        "factor": 1,
        "action": "enem.atc -= 1",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 20,
        "desc": "Uses old and crusty roots to strangle the enemys.",
        "type": "plant",
        "effect": "EffectParalyzation",
        "ap": 15,
    },
    "leaf_storm": {
        "name": "Leaf storm",
        "factor": 5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Blasts a bunch of spikie leafes at the enemy.",
        "type": "plant",
        "effect": None,
        "ap": 10,
    },
    "freeze": {
        "name": "Freeze",
        "factor": 0,
        "action": "",
        "move": ["downgrade"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Freezes the enemy.",
        "type": "ice",
        "effect": "EffectFreezing",
        "ap": 10,
    },
    "snow_storm": {
        "name": "Snow storm",
        "factor": 2.5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Summons a snow storm full of ice spikes onto the enemy.",
        "type": "ice",
        "effect": None,
        "ap": 20,
    },
    "sword_of_ice": {
        "name": "Sword of ice",
        "factor": 5,
        "action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 20,
        "desc": "Stabs a giant ice spike into the enemy.",
        "type": "ice",
        "effect": None,
        "ap": 10,
    },
}

if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
