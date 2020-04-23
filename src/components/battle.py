from json import *
from random import randint

class Battle(object):
	def __init__(self, player_obj, npc_object):
		self.player = player_obj
		self.npc = npc_object
		self.defeated = False	#Boolean value to verify boss is still alive

	def menu():
    		if self.defeated:
    			return
			else:
				#Print options
				print("0. {}\n"
					  "1. {}\n"
					  "2. {}"
					  .format("Attack","Bag","Run"))
				
				#Grab input from user and validate
				#Must research to grab input from user in a way she/he can use
				# arrow keys to select options, much like pokemon
				option = 0
				while option < 0  or option > 2:
    					option = int(input("Choice: "))
					
				if option == 0:
    					self.playerAttack()
				elif option == 1:
    					self.playerItem()
				elif option == 2:
    					return 
				
				self.menu()

	def playerAttack():
		health = self.npc['hp'] - self.player["atk"]
		if health == 0:
			print(self.npc["Luis Ortiz"], "ha caido ante la gran fuerza de.", self.player["name"])
			self.player["exp"] += 5

	def playerItem():
		if self.useItem():
			item = self.chooseItem()
			if not(item):
    				return
			#Increment player attribute depending on item
			if item['type'] == 'def':
					self.player["def"] += item['amount']
			elif item['type'] == 'atk':
    				self.player["atk"] += item['amount']
			elif item['type'] == 'hp':
    				self.player["HP"] += item['amount']
		else:
			return

	def useItem():
		check = input("Do you wish to use an item? Press y for yes.")
		if(check == 'y'):
			return True
		else:
			return False
	
	def chooseItem():
    	#list player items 
		if len(self.player['items']) == 0:
    			print("You don't have any items in bag.\n")
				return None
				
		i = 0
		for i,element in enumerate(self.player['items']):
    			print("\t{}. {}: {}".format(i+1,element['name'],element['desc']))
		while i == 0 or i >= len(self.player['items']):
    			i = int(input("Which one do you want to choose: "))

		return self.player['items'][i-1]

	def npcItem():
		randomInt = randint(0,len(self.npc["items"]))

		if self.npc["items"][randomInt]["amount"] > 0:
			print(self.npc["name"], "uses a", self.npc["items"][randomInt]["name"], "which", self.npc["items"]["desc"])
			self.npc["items"][randomInt]["amount"] -= 1

	def NpcAttack():
		randomInt = randint(0,len(self.npc["attacks"]))


		print("Luis Ortiz usa", self.npc["attacks"][randomInt]["name"])
		print("Luis Ortiz usa {0}".format(self.npc["attacks"][randomInt]["name"]))


		print(self.npc["attacks"][randomInt]["desc"])
		self.npc["atk"] *= self.npc["attacks"][randomInt]["atkmod"]
		self.player["HP"] -= self.npc["atk"]
		self.npc["atk"] = self.npc["atk"] / self.npc["attacks"][randomInt]["atkmod"]

def main():
	# player = 
	# npc = 
	new_battle = Battle(player, npc['Luis Ortiz'])

main()