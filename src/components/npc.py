import json

class NPC(object):
    def __init__(self, obj):
        self.name = obj['name']
        self.hp = obj['hp']
        self.ap = obj['atk']
        self.dp = obj['def']
        self.attacks = obj['attacks']
        self.dialogs = obj['dialog']

    def get_option(self, r):
        while True:
            inp = input('Choose: ')
            try:
                if int(inp) in r:
                    return inp
                else:
                    print('invalid option')
            except:
                print('invalid option not a number')

    def dialog(self):
        for i, d in enumerate(self.dialogs):
            print("({0}) Question: {1}".format(i, d['opt']))
        
        inp = self.get_option(list(range(len(self.dialogs))))
        print(self.dialogs[int(inp)]['res'])
    


# Testing
def main():
    with open('../ng.json','r') as f:
        npc_data = json.loads(f.read())
    npc = NPC(npc_data['npc']['Luis Ortiz'])
    # print(npc.dialogs)

    npc.dialog()


main()
