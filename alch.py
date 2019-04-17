import traceback

# set min / max tier of potion, and specify any types of potions you want to ignore when checking ingredients
# copy/paste 'reagents herb' into regs.txt, save file, run script

mintier = 3
maxtier = 4
ignore_types = []

types = ['str', 'con', 'dex', 'int', 'wis', 'chr', 'digestion', 'detox', 'hpregen', 'spregen']

pots = {
    "chr": {
        1: {"Rose Hip": 6, "Spine Flower": 3},
        2: {"Pokeweed": 6, "Ice Leaf": 3},
        3: {"Star Flower": 6, "Trillum": 3},
        4: {"Konjac": 6, "Ballamault": 3}
    },

    "con": {
        1: {"Ash Root": 6, "Cow Leaf": 3},
        2: {"Crown Root": 6, "Mint Leaf": 3},
        3: {"Spiner Root": 6, "Passion Flower": 3},
        4: {"Mint Root": 6, "Cactus Flower": 3}
    },

    "dex": {
        1: {"Galingale": 6, "Catchfly": 3},
        2: {"Desert Lace": 6, "Frozen Rose": 3},
        3: {"Knotweed": 6, "Sun Flower": 3},
        4: {"Exotic Bai": 6, "Helio": 3}
    },

    "int": {
        1: {"White Mushroom": 6, "Death Shoots": 3},
        2: {"Black Mushroom": 6, "Ice Bain": 3},
        3: {"Slimy Mushroom": 6, "Sparkling Yopo": 3},
        4: {"Glowing Mushroom": 6, "SilverLeaf": 3}
    },
    
    "str": {
        1: {"Dark Root": 6, "Cannabis": 3},
        2: {"Rock Leaf": 6, "Cryoflora": 3},
        3: {"Spurge Leaf": 6, "Wild Kanna": 3},
        4: {"Bergamot": 6, "Lord Leaf": 3}
    },

    "wis": {
        1: {"Oak Leaf": 6, "Feverfew": 3},
        2: {"Flaming Sari": 6, "Frosty Mushroom": 3},
        3: {"Sleepwillow": 6, "Pixie Breath": 3},
        4: {"Velvet Larz": 6, "Daturas": 3}
    },
        
    "digestion": {
        1: {"Bamboo Leaf": 6, "Lava Root": 3},
        2: {"Death Mint": 6, "Enchanted Sumac": 3},
        3: {"Rotten Root": 6, "Mandrake": 3},
        4: {"Pond Weed": 6, "Tunnera": 3}
    },
        
    "detox": {
        1: {"Bristlegrass": 6, "Netherroot": 3},
        2: {"Dragon Root": 6, "Rocky Thorns": 3},
        3: {"Glowing Lily": 6, "Red Ivy": 3},
        4: {"Valerian": 6, "Living Rock": 3}
    },

    "hpregen": {
        1: {"Wild Weed": 6, "Dinkweed": 3},
        2: {"Chamomile": 6, "Snowweed": 3},
        3: {"Opium": 6, "Whore's Rose": 3},
        4: {"Cancansa": 6, "Novaroot": 3}
    },

    "spregen": {
        1: {"Brown Mushroom": 6, "Frozen Root": 3},
        2: {"Honey Mushroom": 6, "Jungle Root": 3},
        3: {"Pokadot Mushroom": 6, "Pixie Root": 3},
        4: {"Psilocyin Mushroom": 6, "Vampire Root": 3}
    }
}

def parse_regs():
    with open("regs.txt", "r") as rf:
        text = rf.read()
        
    lines = text.split('\n')
    
    newline = "\n"
    tab = "    "
    
    out = 'regs = {' + newline
    out2 = ''
    
    for line in lines:
        reg1 = line[:35].split(':')
        reg2 = line[35:].split(':')
        
        out += tab + '"' + reg1[0].strip(' ') + '": ' + reg1[1].replace(' ', '') + ',' + newline
        out2 += tab + '"' + reg2[0].strip(' ') + '": ' + reg2[1].replace(' ', '') + ',' + newline
        
    out += out2
    out = out[:-2]
    
    out += newline + '}'
    
    exec(out)
    
    return regs

try:
    regs = parse_regs()
    scripted = []

    for type in [type for type in types if type not in ignore_types]:
        for tier in range(mintier, maxtier + 1):
            make = True
            firstreg = True
            for reg in pots[type][tier].keys():
                if regs[reg] < pots[type][tier][reg]:
                    make = False
                    break
                else:   
                    if not firstreg:
                        check = regs[reg] / pots[type][tier][reg]
                        if check < makenum:
                            makenum = check
                    else:
                        makenum = regs[reg] / pots[type][tier][reg]
                        firstreg = False
            if make:
                scripted.append((type + str(tier), str(makenum)))
                print(type + str(tier) + ': ' + str(makenum))

    if len(scripted) > 1:
        script = "script "
        for item in scripted:
            if int(item[1]) > 1:
                    script += item[1] + ":quickcraft " + item[0] + ","
            else:
                    script += "quickcraft " + item[0] + ","
        script = script.strip(",")
    elif len(scripted) == 1:
        if int(scripted[0][1]) > 1:
            script = "script " + scripted[0][1] + ":quickcraft " + scripted[0][0]
        else:
            script = "quickcraft " + scripted[0][0]
    else:
        script = "No pots."


    print('\n\n' + script)
except:
    traceback.print_exc()

s = raw_input("Copy/paste script to craft all pots.  Press enter to close.")
