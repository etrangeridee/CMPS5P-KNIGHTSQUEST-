print("Welcome to KnightsQuest, a simple RPG. To begin, please enter your name:")
a = str(input())
print("Greetings,", a,".")
print("""You are a resident of Fantasia Valley, a fertile land known for both crops and ore. Recently, though, the land has been under attack by a fierce Goblin Army and an enclave of Dragons who seek the gold in the land.
Your village of Writingham is currently prospering, but on a tightrope, because of raids by Goblin legionaries and various monsters. You've decided to take up arms to save your village and the valley, in order to save
the land from the scourges that plague it. Go forth! The land depends on you!""")
print("But, before you go, you might want to figure out how you fair, physically.")
CHOICE = "NO"
while CHOICE == "NO":
    print("""Please select your armor type.
    1 for Light Armor
    2 for Medium Armor
    3 for Heavy Armor.""")
    ARMOR = int(input())
    HP = 0
    SPEED = 0
    ATK = 0
    if ARMOR == 1:
        print("You've selected Light armor.")
        ARMOR = 1
        HP = 40
        SPEED = 3
        STR = 8
    if ARMOR == 2:
        print ("You've selected Medium Armor.")
        ARMOR = 2
        HP = 80
        SPEED = 2
        STR = 10
    if ARMOR == 3:
        print("You've selected Heavy Armor.")
        ARMOR = 3
        HP = 100
        SPEED = 1
        STR = 12
    print("Your choice will give you the following stats:")
    print("Your vitality is:", HP, "Hit Points.")
    print("Your swiftness is:", SPEED, "in combat.")
    print("Your strength is:", STR, "in combat.")
    print("""Is this ok? You can answer YES or NO. Please note that this choice can only be changed at this point in time.
After you've finished choosing, there's no going back on this.""")
    CHOICE = str(input())
    if CHOICE == "YES":
        print("You may proceed.")
    else:
        print("You may change your armor, then.")
WPNCHOICE = "NO"
while WPNCHOICE == "NO":
    print("""Please choose a weapon. This will modify your existing attack only positively, because there's no way I'd let it be a negative impact.
You may choose between: the Shortsword, Longsword, or Crossbow.""")
    WPN = str(input())
    if WPN == "Shortsword":
        print("You've chosen the Shortsword.")
        STR =  STR + 3
        SPEED =  SPEED + 4
    if WPN == "Longsword":
        print("You've chosen the Longsword.")
        STR = STR + 6
        SPEED = SPEED + 2
    if WPN == "Crossbow":
        print("You've chosen the Crossbow")
        STR = STR + 5
        SPEED = SPEED + 3
    print("Let's take a look at your final stats. Accounting armor, you are at:")
    print(STR, "Combat strength.")
    print(HP, "Hit points.")
    print(SPEED, "Combat swiftness.")
    print(ARMOR, "Armor strength.")
    print("Are these your desired starting statistics? Respond with YES or NO.")
    WPNCHOICE = str(input())
    if WPNCHOICE == "YES":
        print("Very well. Congratulations on completeing the configuration portion of the game. Prepare to set off!")
    else:
        print("You may change your weapon, then.")
#This is a general layout for combat. Obviously stats can change and this section can be moved into a module including RNG encounters much later, but
#leave it here for now until both actions have been done 100%. 
print("You begin your journey but are interrupted by a surprise fiend!")
#Lesser Goblin information
print("A lesser goblin blocks your path, in a lesser sense.")
LGSPD = 2
LGSTR = 5
LGSPD = 4
LGHP = 15
EDMG = HP - LGSTR
DMG = LGHP - STR
#These are the lesser goblin's stats. If they're not impressive, don't be surprised, because they're not meant to be.
print("""What will you do? You may choose to [fight] or [flee].
A WORD ON COMBAT: words in brackets are your input choices.""")
COMBATDECISION = str(input())
if COMBATDECISION == "fight":
    print("Prepare for combat...")
    print("Goblin moves to attack!")
if LGSPD < SPEED:
    print("But you're faster and get chance for the first blow!")
else:
    print("Goblin swings first!")
    if LGSTR < STR:
        print("But no damage was dealt...")
        print("You move in to counter with a greater blow!")
    else:
        print("Lesser goblin deals", LGSTR, "points of damage. You are at", EDMG, "HP.")
if DMG < 0 or DMG == 0:
    print("Lesser goblin's lesser HP outran its even lesser combat prowess! Lesser goblin was defeated.")
else:
    print("You deal", STR, "points of damage to the Lesser goblin. Lesser goblin is currently at", DMG, "HP.")
#The former combat scenario works off of both SPEED and STR. It can shorten combat if either stat is superior to the enemy's.
#The following scenario assumes you can't 1HKO the enemy you're fighting. 
while DMG > 0 and HP > 0:
    print("Prepare for combat.")
    print("Beginning attack phase...")
    print("Will you [attack] or [defend]?")
    APCHOICE = str(input())
    if APCHOICE == "attack":
        if STR > LGSTR:
            print("You swing your", WPN, "and consequently deal", STR, "points of damage to the Lesser goblin.")
        else:
            print("Though you tried to attack the Lesser goblin, no damage was dealt.")
        if DMG < 0:
            print("Lesser goblin's lesser HP outran its combat prowess! Lesser goblin was defeated.")
        else:
            print("You deal", STR, "points of damage to the Lesser goblin. Lesser goblin is currently at", DMG, "HP.")
    if APCHOICE == "defend":
        print("You raise your", WPN, "in a defensive stance.")
        print("Lesser goblin moves in to attack!")
        if LGSTR < STR:
            print("But no damage was dealt...")
        else:
            print("Lesser goblin deals", LGSTR, "points of damage. You are at", EDMG, "HP.")
        if EDMG < 0:
            print("Lesser goblin's swing ends you in less than a second.")

