# poli-rpg

## Getting Started

* Download vscode
* Get the vscode live share extension
* Fork this repository
* Clone your poli-rpg fork to a local directory
> git clone https://github.com/cyber-castors/poli-rpg.git
* Read this -> https://reflectoring.io/github-fork-and-pull/ (For updating fork from original repository a.k.a. this one)

## To-do (Project)

* Complete design for game flow and progression.
* Complete design for levels/classes and events.
* Add remaining methods to player class.
* Create NPC class.
* Add remaining methods to battle class.

## Future (Project)
* Add dialog to NPCs.
* Add Flavor Text to Attacks.
* Implement save and load.
* Add game menus.
* Implement slow text (simulated typing) and color to text.

## Classes/Ojbects

1. Player
    * Attributes:
        1. Attack
        2. Defense
        3. HP
        4. Items
        5. Name
        6. Badges (Or other element to track story progression)
        7. Experience
        8. Level
        9. Major
        10. Credits
    * Methods:
        1. Level Up
        2. Use Item (Outside of Battle Instance)
        3. Show Stats
        4. View Badges
        5. View Attacks
        6. View Items
    * Formulas

2. NPC
    * Attributes:
        1. Attack
        2. Defense
        3. HP
        4. Items
        5. Name
        6. Dialog
        7. Experience (For Defeating)

3. Battle (player_obj, npc_obj)
    * Attributes
        <!-- 1. Player Attack
        2. Player Defense -->
        3. Player HP (During Instance)
        <!-- 4. Player Name -->
        <!-- 5. Player Items -->
        <!-- 6. NPC Attack
        7. NPC Defense -->
        8. NPC HP (During Instance)
        <!-- 9. NPC Name -->
        <!-- 10. NPC Items -->
        <!-- 11. NPC Attack Flavor Text -->
        <!-- 12. Player Exp
        13. Player Level -->
    * Method
        1. Player Attacks (Deal damage to instanc npc hp)
        2. NPC Attacks (Deal damage to instance player hp)
        3. Use Item (This may be better to implement in player and npc classes)

4. Store
    * Attributes:
        1. Player Money
        2. Player Items
        3. Store Items
        4. Player Name
    * Methods:
        1. Buy Item
        2. Sell Item
        3. Show Player Items
        4. Show Store Items

5. Level/Course
    * Attributes:
        1. Player Name
        2. Player Badges
        3. NPC Name
        4. NPC Dialog
    * Methods:
        * (WIP) Need to work on game structure and flow

#### JSON Hierarchy

1. Player
    * Player Attributes
2. Courses
    1. Course Code (i.e. CECS1001)
        1. Course Name
        2. NPCs
            1. Name
                * NPC Attributes
        3. Item Rewards
            1. Item name (Use name to append from Items)
        4. EXP Reward
3. Items
    1. Name
        * Item attributes

#### Classes/Objects will be saved in src/components

Levels will correspond to a CS or COE course.
Beating/passing course will unlock the following course.

#### Check notes.md for a rough draft on game progression