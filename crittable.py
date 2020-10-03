import random

def checkcritical(argument):
    switcher = {
        11: True,
        22: True,
        33: True,
        44: True,
        55: True,
        66: True,
        77: True,
        88: True,
        99: True
    }
    return switcher.get(argument,False)
    
"""  
    if argument == 11:
        return True
    elif argument == 22:
        return True
    elif argument == 33:
        return True
    elif argument == 44:
        return True
    elif argument == 55:
        return True
    elif argument == 66:
        return True
    elif argument == 77:
        return True
    elif argument == 88:
        return True
    elif argument == 99:
        return True
    else:
        return False
"""

def crit():
    cl = random.randrange(1, 101)
    if 1<= cl and cl <=9:
        print("The Head")
        HCritwoundtable()
    elif 10<= cl and cl <=24:
        print("The Left Arm")
        LACritwoundtable()
    elif 25<= cl and cl <=44:
        print("The Right Arm")
        RACritwoundtable()
    elif 45<= cl and cl <=79:
        print("The Body")
        BCritwoundtable()
    elif 80<= cl and cl <=89:
        print("The Left Leg")
        LLCritwoundtable()
    elif 90<= cl and cl <=100:
        print("The Right Leg")
        RLCritwoundtable()

def HCritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("Dramatic Injury (1 Wound): A fine wound across the forehead and cheek.  Gain 1 Bleeding Condition.  Once the wound is healed, the impressive scar it leaves provides a bonus of +1 SL to appropriate social Tests.  You can only gain this benefit once.")
    elif 11<=cw and cw<=20:
        print("Minor Cut (1 Wound): The strike opens your cheek and blood flies.  Gain 1 Bleeding Condition.")
    elif 21<=cw and cw<=25:
        print("Poked Eye (1 Wound): The blow glances across the eye socket.  Gain 1 Blinded Condition.")
    elif 26<=cw and cw<=30:
        print("Ear Bash (1 Wound): After a sickening impact, your ear is left ringing.  Gain 1 Deafened Condition.")
    elif 31<=cw and cw<=35:
        print("Rattling Blow (2 Wounds): The blow floods your vision with flashing lights.  Gain 1 Stunned Condition.")
    elif 36<=cw and cw<=40:
        print("Black Eye (2 Wounds): A solid blow hits your eye, leaving tears and pain.  Gain 2 Blinded Conditions.")
    elif 41<=cw and cw<=45:
        print("Sliced Ear (2 Wounds): The side of your head takes a hard blow, cutting deep into your ear.  Gain 2 Deafened and 1 Bleeding Conditions.")
    elif 46<=cw and cw<=50:
        print("Struck Forehead (2 Wounds): A solid blow hits your forehead.  Gain 2 Bleeding Conditions and a Blinded Condition that cannot be removed until all Bleeding Conditions are removed.")
    elif 51<=cw and cw<=55:
        print("Fractured Jaw (3 Wounds): With a sickening crunch, pain fills your face as the blow fractures your jaw.  Gain 2 Stunned Conditions.  Suffer a Broken Bone (Minor) injury.")
    elif 56<=cw and cw<=60:
        print("Major Eye Wound (3 Wounds): The blow cracks across your eye socket.  Gain 1 Bleeding Condition.  Also gain 1 Blinded Condition that cannot be removed until you recieve Medical Attention.")
    elif 61<=cw and cw<=65:
        print("Major Ear Wound (3 Wounds): The blow strikes deep into one ear.  Suffer a permananent -20 penalty on all Tests relating to hearing.  If you suffer this result again, your hearing is permanently lost as the second ear falls quiet.  Only magic can heal this.")
    elif 66<= cw and cw<=70:
        print("Broken Nose (3 Wounds): A solid blow to the center of your face causing blood to pour.  Gain 2 Bleeding Conditions.  Make a Challenging (+0) Endurance Tests, or also gain a Stunned Condition.  After this wound has healed, gain +1/-1 SL on Social rolls, depending on context, unless Surgery is used to reset the nose.")
    elif 71<= cw and cw<=75:
        print("Broken Jaw (4 Wounds): The crack is sickening as the blow hits you under the chin, breaking your jaw.  Gain 3 Stunned Conditions.  Make a Challenging (+0) Endurance Test or gain an Unconscious Condition.  Suffer a Broken Bone (Major) injury.")
    elif 76<=cw and cw<=80:
        print("Concussive Blow (4 Wounds): Your brain rattles in your skull as blood spurts from your nose and ears.  Take 1 Deafened, 2 Bleeding, and 1d10 Stunned Conditions.  Gain a Fatigued Condition that lasts for 1d10 days.  If you recieve another Critical Wound to your head while suffering this Fatigued Condition, make an Average (+20) Endurance Test or also gain an Unconscious Condition.")
    elif 81<=cw and cw<=85:
        print("Smashed Mouth (4 Wounds): With a sickening crunch, your mouth is suddenly filled with broken teeth and blood.  gain 2 Bleeding Conditions.  Lose 1d10 teeth -- Amputation (Easy).")
    elif 86<=cw and cw<=90:
        print("Mangled Ear (4 Wounds): Little is left of your ear as the blow tears it apart.  You gain 3 Deafeend and 2 Bleeding Conditions.  Lose your ear -- Amputation (Average).")
    elif 91<=cw and cw<=93:
        print("Devastated Eye (5 Wounds): A strike to your eye completely bursts it, causing extraordinary pain.  Gain 3 Blinded, 2 Bleeding, and 1 Stunned Condition.  Lose your eye -- Amputation (Difficult).")
    elif 94<=cw and cw<=96:
        print("Disfiguring Blow (5 Wounds): The blow smashes your entire face, destroying your eye and nose in a cloud of blood.  Gain 3 Bleeding, 3 Blinded, and 2 Stunned Conditions.  Lose your eye and nose -- Amputation (Hard).")
    elif 97<=cw and cw<=99:
        print("Mangled Jaw (5 Wounds): The blow almost removes your jaw as it utterly destroys your tongue, sending teeth flying in a shower of blood.  Gain 4 Bleeding and 3 Stunned Conditions.  Make a Very Hard (-30) Endurance Test or gain an Unconscious Condition.  Suffer a Broken Bone (Major) injury and lose your tongue and 1d10 teeth -- Amputation (Hard).")
    elif cw == 100:
        print("Decapitated (Death): Your head is entirely severed from your neck and soars through the air, landing 1d10 feet away in a random direction (see Scatter).  Your body collapses, instantly dead.")

def LACritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("Jarred Arm (1 Wound): Your arm is jarred in the attack.  Drop whatever was held in your left hand.")
    elif 11<=cw and cw<=20:
        print("Minor Cut (1 Wound): Gain a Bleeding condition as your left upper arm is cut badly.")
    elif 21<=cw and cw<=25:
        print("Sprain (1 Wound): You Sprain your left arm, suffering a Torn Muscle (Minor) injury.")
    elif 26<=cw and cw<=30:
        print("Badly Jarred Arm (2 Wounds): Your left arm is badly jarred in the attack.  Drop whatever was held in that hand, which is useless for 1d10-Toughness Bonus Rounds (minimum 1).  For this time, treat the hand as lost (see Amputated Parts pg. 180).")
    elif 31<=cw and cw<=35:
        print("Torn Muscles (2 Wounds): The blow slams into your left forearm.  Gain a Bleeding Condition and a Torm Muscle (Minor) injury.")
    elif 36<=cw and cw<=40:
        print("Bleeding Hand (2 Wounds): Your left hand is cut badly, making your grip slippery.  Gain 1 Bleeding Condition.  While suffering from that Bleeding Condition, make an Average (+20) Dexterity Test before taking any Action that requires something being held in that hand if you fail, the item slips from your grip.")
    elif 41<=cw and cw<=45:
        print("Wrenched Arm (2 Wounds): Your left arm is almost pulled from its socket.  Drop whatever is held in the associated hand the arm is useless for 1d10 Rounds (see Amputated Parts pg. 180).")
    elif 46<=cw and cw<=50:
        print("Gaping Wound (3 Wounds): The blow opens a deep, gaping wound on your left arm.  Gain 2 Bleeding Conditions.  Until recieve Surgery to stitch up the cut, any associated Left Arm Damage you receive will also inflict 1 Bleeding Condition as the wound reopens.")
    elif 51<=cw and cw<=55:
        print("Clean Break (3 Wounds): An audible crack resounds as the blow strikes your left arm.  Drop whatever was held in the associated hand and gain a Broken Bone (Minor) injury.  Pass a Difficult (-10) Endurance Test or gain a Stunned Condition.")
    elif 56<=cw and cw<=60:
        print("Ruptured Ligament (3 Wounds): You immediately drop whatever was held in your left hand.  Suffer a Torn Muscle (Major) injury.")
    elif 61<=cw and cw<=65:
        print("Deep Cut (3 Wounds): Gain 2 Bleeding Conditions as your left arm is mangled.  Gain 1 Stunned Condition and suffer a Torn Muscle (Minor) injury.  Take a Hard (-20) Endurance Test or gain the Unconscious Condition.")
    elif 66<= cw and cw<=70:
        print("Damaged Artery (4 Wounds): Gain 4 Bleeding Conditions.  Until you recieve Surgery, gain 2 Bleeding Conditions every time you take damage to your left arm.")
    elif 71<= cw and cw<=75:
        print("Crushed Elbow (4 Wounds): The blow crushes your left elbow, splintering bone and cartilage.  You immediately drop whatever was held in that hand and gain a Broken Bone (Major) injury.")
    elif 76<=cw and cw<=80:
        print("Dislocated Shoulder (4 Wounds): Your left arm is wrenched out of its socket.  Pass a hard (-20) Endurance Test or gain the Stunned and Prone Condition.  Drop whatever is held in that hand: the arm is useless and counts as lost (see Amputated Part pg 180).  Gain 1 Stunned Condition until you recieve Medical Attention.  After this initial Medical Attention, an Extended Average (+20) Heal Test needing 6 SL is required to reset the arm, at which point you regain its use.  Tests made using this arm suffer a -10 penalty for 1d10 days.")
    elif 81<=cw and cw<=85:
        print("Severed Finger (4 Wounds): You gape in horror as a finger flies from your left hand -- Amputation (Average).  Gain a Bleeding Condition.")
    elif 86<=cw and cw<=90:
        print("Cleft Hand (5 Wounds): Your left hand splays open from the blow.  Lose 1 finger -- Amputation (Difficult).  Gain 2 Bleeding and 1 Stunned Condition.  For every succeeding Round in which you don't receive Medical Attention, you lose another finger as the wound tears if you run out of fingers, you lose the hand -- Amputation (Difficult).")
    elif 91<=cw and cw<=93:
        print("Mauled Bicep (5 Wounds): The blow almost seperates your left bicep and tendons from bone, leaving an ugly wound that sprays blood over you and your opponent.  You Automatically drop anything held in the associated hand and suffer a Torn Muscle (Major) injury and 2 Bleeding and 1 Stunned Condition.")
    elif 94<=cw and cw<=96:
        print("Mangled Hand (5 Wounds): Your left hand is left a mauled, bleeding mess.  You lose your hand -- Amputation (Hard).  Gain 2 Bleeding Condition.  Take a Hard (-20) Endurance Test or gain the Stunned and Prone Conditions.")
    elif 97<=cw and cw<=99:
        print("Sliced Tendons (5 Wounds): Your tendons are cut by the blow, leaving your left arm hanging useless -- Amputation (Very Hard).  Gain 3 Bleeding, 1 Prone, and 1 Stunned Condition.  Pass a Hard (-20) Endurance Test or gain the Unconscious Condition.")
    elif cw == 100:
        print("Brutal Dismemberment (Death): Your left arm is severed, spraying arterial blood 1d10 feet in a random direction (see Scatter), before the blow follows through to your chest.")

def RACritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("Jarred Arm (1 Wound): Your arm is jarred in the attack.  Drop whatever was held in your right hand.")
    elif 11<=cw and cw<=20:
        print("Minor Cut (1 Wound): Gain a Bleeding condition as your right upper arm is cut badly.")
    elif 21<=cw and cw<=25:
        print("Sprain (1 Wound): You Sprain your right arm, suffering a Torn Muscle (Minor) injury.")
    elif 26<=cw and cw<=30:
        print("Badly Jarred Arm (2 Wounds): Your right arm is badly jarred in the attack.  Drop whatever was held in that hand, which is useless for 1d10-Toughness Bonus Rounds (minimum 1).  For this time, treat the hand as lost (see Amputated Parts pg. 180).")
    elif 31<=cw and cw<=35:
        print("Torn Muscles (2 Wounds): The blow slams into your right forearm.  Gain a Bleeding Condition and a Torm Muscle (Minor) injury.")
    elif 36<=cw and cw<=40:
        print("Bleeding Hand (2 Wounds): Your right hand is cut badly, making your grip slippery.  Gain 1 Bleeding Condition.  While suffering from that Bleeding Condition, make an Average (+20) Dexterity Test before taking any Action that requires something being held in that hand if you fail, the item slips from your grip.")
    elif 41<=cw and cw<=45:
        print("Wrenched Arm (2 Wounds): Your right arm is almost pulled from its socket.  Drop whatever is held in the associated hand the arm is useless for 1d10 Rounds (see Amputated Parts pg. 180).")
    elif 46<=cw and cw<=50:
        print("Gaping Wound (3 Wounds): The blow opens a deep, gaping wound on your right arm.  Gain 2 Bleeding Conditions.  Until recieve Surgery to stitch up the cut, any associated Left Arm Damage you receive will also inflict 1 Bleeding Condition as the wound reopens.")
    elif 51<=cw and cw<=55:
        print("Clean Break (3 Wounds): An audible crack resounds as the blow strikes your right arm.  Drop whatever was held in the associated hand and gain a Broken Bone (Minor) injury.  Pass a Difficult (-10) Endurance Test or gain a Stunned Condition.")
    elif 56<=cw and cw<=60:
        print("Ruptured Ligament (3 Wounds): You immediately drop whatever was held in your right hand.  Suffer a Torn Muscle (Major) injury.")
    elif 61<=cw and cw<=65:
        print("Deep Cut (3 Wounds): Gain 2 Bleeding Conditions as your right arm is mangled.  Gain 1 Stunned Condition and suffer a Torn Muscle (Minor) injury.  Take a Hard (-20) Endurance Test or gain the Unconscious Condition.")
    elif 66<= cw and cw<=70:
        print("Damaged Artery (4 Wounds): Gain 4 Bleeding Conditions.  Until you recieve Surgery, gain 2 Bleeding Conditions every time you take damage to your right arm.")
    elif 71<= cw and cw<=75:
        print("Crushed Elbow (4 Wounds): The blow crushes your right elbow, splintering bone and cartilage.  You immediately drop whatever was held in that hand and gain a Broken Bone (Major) injury.")
    elif 76<=cw and cw<=80:
        print("Dislocated Shoulder (4 Wounds): Your right arm is wrenched out of its socket.  Pass a hard (-20) Endurance Test or gain the Stunned and Prone Condition.  Drop whatever is held in that hand: the arm is useless and counts as lost (see Amputated Part pg 180).  Gain 1 Stunned Condition until you recieve Medical Attention.  After this initial Medical Attention, an Extended Average (+20) Heal Test needing 6 SL is required to reset the arm, at which point you regain its use.  Tests made using this arm suffer a -10 penalty for 1d10 days.")
    elif 81<=cw and cw<=85:
        print("Severed Finger (4 Wounds): You gape in horror as a finger flies from your right hand -- Amputation (Average).  Gain a Bleeding Condition.")
    elif 86<=cw and cw<=90:
        print("Cleft Hand (5 Wounds): Your right hand splays open from the blow.  Lose 1 finger -- Amputation (Difficult).  Gain 2 Bleeding and 1 Stunned Condition.  For every succeeding Round in which you don't receive Medical Attention, you lose another finger as the wound tears if you run out of fingers, you lose the hand -- Amputation (Difficult).")
    elif 91<=cw and cw<=93:
        print("Mauled Bicep (5 Wounds): The blow almost seperates your right bicep and tendons from bone, leaving an ugly wound that sprays blood over you and your opponent.  You Automatically drop anything held in the associated hand and suffer a Torn Muscle (Major) injury and 2 Bleeding and 1 Stunned Condition.")
    elif 94<=cw and cw<=96:
        print("Mangled Hand (5 Wounds): Your right hand is left a mauled, bleeding mess.  You lose your hand -- Amputation (Hard).  Gain 2 Bleeding Condition.  Take a Hard (-20) Endurance Test or gain the Stunned and Prone Conditions.")
    elif 97<=cw and cw<=99:
        print("Sliced Tendons (5 Wounds): Your tendons are cut by the blow, leaving your right arm hanging useless -- Amputation (Very Hard).  Gain 3 Bleeding, 1 Prone, and 1 Stunned Condition.  Pass a Hard (-20) Endurance Test or gain the Unconscious Condition.")
    elif cw == 100:
        print("Brutal Dismemberment (Death): Your right arm is severed, spraying arterial blood 1d10 feet in a random direction (see Scatter), before the blow follows through to your chest.")

def BCritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("'Tis But A Scratch! (1 Wound): Gail 1 Bleeding Condition.");
    elif 11<=cw and cw<=20:
        print("Gut Blow (1 Wound): Gain 1 Stunned Condition.  Pass an Easy (+40) Endurance Test, or vomit, gaining the Prone Condition.");
    elif 21<=cw and cw<=25:
        print("Low Blow! (1 Wound): Make a Hard (-20) Endurance Test or gain 3 STunned Condition.");
    elif 26<=cw and cw<=30:
        print("Twisted Back (1 Wound): Suffer a Torn Muscle (Minor) injury.");
    elif 31<=cw and cw<=35:
        print("Winded (2 Wounds): Gain a Stunned Condition.  Make an Average (+20) Endurance Test, or gain the Prone Condition.  Movement is halved for 1d10 rounds as yo uget your breath back.");
    elif 36<=cw and cw<=40:
        print("Bruised Ribs (2 Wounds): All Agility-based Tests suffer a -10 penalty for 1d10 days.");
    elif 41<=cw and cw<=45:
        print("Wrenched Collar Bone (2 Wounds): Randomly select one arm.  Drop whatever is held in that hand; the arm is useless for 1d10 rounds (see Amputated Parts).");
    elif 46<=cw and cw<=50:
        print("Ragged Wound (2 Wounds): Take 2 Bleeding Conditions.");
    elif 51<=cw and cw<=55:
        print("Cracked Ribs (3 Wounds): The hit cracks one or more ribs.  Gain a Stunned Condition.  Gain a Broken Bone (Minor) injury.");
    elif 56<=cw and cw<=60:
        print("Gaping Wound (3 Wounds): Take 3 Bleeding Conditions.  Until you recieve Surgery, any Wounds you receive to the Body Hit Location will inflict an additional Bleeding Condition as the cut reopens.");
    elif 61<=cw and cw<=65:
        print("Painful Cut (3 Wounds): Gain 2 Bleeding Conditions and a Stunned Condition.  Take a Hard (-20) Endurance Test or gain the Unconscious Condition as you black out from the pain.  Unless you achieve 4+ SL, you also scream out in agony.");
    elif 66<= cw and cw<=70:
        print("Arterial Damage (3 Wounds): Gain 4 Bleeding Conditions.  Until you receive Surgery, every time you receive damage to the Body Hit Location, gain 2 Bleeding Conditions.");
    elif 71<= cw and cw<=75:
        print("Pulled Back (4 Wounds): Your back turns to white pain as you pull a muscle.  Suffer a Torn Muscle (Major) injury.");
    elif 76<=cw and cw<=80:
        print("Fractured Hip (4 Wounds): Gain a Stunned Condition.  Take a Challenging (+0) Endurance Test or also gain the Prone Condition.  SUffer a Broken Bone (Minor) injury.");
    elif 81<=cw and cw<=85:
        print("Major Chest Wound (4 Wounds):  You take a significant wound to your chest, flensing skin from muscle and sinew.  Take 4 Bleeding Conditions.  Until you receive Surgery, to stitch the wound together, any Wounds you receive to the Body Hit Location will also inflict 2 Bleeding Conditions as the tears reopen.");
    elif 86<=cw and cw<=90:
        print("Gut Wound (4 Wounds): Contract a Festering Wound (See Disease and Infection) and gain 2 Bleeding Conditions.");
    elif 91<=cw and cw<=93:
        print("Smashed Rib Cage (5 Wounds): Gain a Stunned Condition that can only be removed throguh Medical Attention, and suffer a Broken Bone (Major) injury.");
    elif 94<=cw and cw<=96:
        print("Broken Collar Bone (5 Wounds):  Gain the Unconscious Condition until you recieve Medical Attention, and suffer a Broken Bone (Major) injury.");
    elif 97<=cw and cw<=99:
        print("Internal Bleeding (5 Wounds): Gain a Bleeding Condition that can only be removed through Surgery.  Contract Blood Rot (See Disease and Infection).");
    elif cw == 100:
        print("Torn Apart (Death): You are hacked in two.  The top half lands in a random direction, and all characters within 2 yards are showered in blood.");

def LLCritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("Stubbed Toe (1 Wound): In the scuffle, you stub your left big toe.  Pass a Routine (+20) Endurance Test or suffer -10 on Agility Tests until the end of the next turn.");
    elif 11<=cw and cw<=20:
        print("Twisted Ankle (1 Wound): You go over your left ankle, hurting it.  Agility Tests suffer a -10 penalty for 1d10 rounds.");
    elif 21<=cw and cw<=25:
        print("Minor Cut (1 Wound): Gain 1 Bleeding Condition.");
    elif 26<=cw and cw<=30:
        print("Lost Footing (1 Wound): In the scuffle you lose your footing.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.");
    elif 31<=cw and cw<=35:
        print("Thigh Strike (2 Wounds): A painful blow slams into your left upper thigh.  Gain a Bleeding Condition and take an Average (+20) Endurance Test or stumble, gaining the Prone Condition.");
    elif 36<=cw and cw<=40:
        print("Sprained Ankle (2 Wounds): You sprain your left ankle, giving you a Torn Muscle (Minor) injury.");
    elif 41<=cw and cw<=45:
        print("Twisted Knee (2 Wounds): You twist your left knee too far.  Agility Tests suffer a -20 penalty for 1d10 rounds.");
    elif 46<=cw and cw<=50:
        print("Badly Cut Toe (2 Wounds): Gain 1 Bleeding Condition.  After the encounter, make a Challenging (+0) Endurance Test.  If you fail, lose 1 toe on your left foot -- Amputation (Average).");
    elif 51<=cw and cw<=55:
        print("Bad Cut (3 Wounds): Gain 2 Bleeding Conditions as a deep wound opens up your left shin.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.");
    elif 56<=cw and cw<=60:
        print("Badly Twisted Knee (3 Wounds): You badly twist your left knee trying to avoid your opponent.  Gain a Torn Muscle (Major) injury.");
    elif 61<=cw and cw<=65:
        print("Hacked Leg (3 Wounds): A cut bites down into the left hip.  Gain 1 Prone and 2 Bleeding Conditions, and suffer a Broken Bone (Minor) injury.  Further, take a Hard (-20) Endurance Test or also gain a Stunned condition from the pain.");
    elif 66<= cw and cw<=70:
        print("Torn Thigh (3 Wounds): Gain 3 Bleeding Conditions as the weapon opens up your left upper thigh.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.  Until you receive Surgery to stitch up the wound, each time you receive Damage to this Leg, also receive 1 Bleeding Condition.");
    elif 71<= cw and cw<=75:
        print("Ruptured Tendon (4 Wounds): Gain a Prone and Stunned Condition as one of your tendons on your left leg tears badly.  Pass a Hard (-20) Endurance Test or gain the Unconscious Condition.  Your leg is useless (see Amputated Parts).  Suffer a Torn Muscle (Major) injury.");
    elif 76<=cw and cw<=80:
        print("Carved Shin (4 Wounds): The weapon drives clean through your left leg by the knee, slicing into bone and through tendons.  Gain a Stunned and Prone Condition.  Further, suffer a Torn Msucle (Major) and Broken Bone (Minor) injury.");
    elif 81<=cw and cw<=85:
        print("Broken Knee (4 Wounds): The blow hacks into your left kneecap, shattering it into several pieces.  You gain 1 Bleeding, 1 Prone, and 1 Stunned Condition, and a Broken Bone (Major) injury as you fall to the ground, clutching your ruined leg.");
    elif 86<=cw and cw<=90:
        print("Dislocated Knee (4 Wounds): Your left knee is wrenched out of its socket.  Gain the Prone Condition.  Pass a Hard (-20) Endurance Test, or gain the Stunned Condition, which is not removed until you recieve Medical Attention.  After this initial Medical Attention, an Extended Average (+20) Heal Test needing 6 SL is required to reset the knee at which point you regain its use.  Movement is halved, and Tests made using this leg suffer a -10 penalty for d10 days.");
    elif 91<=cw and cw<=93:
        print("Crushed Foot (5 Wounds): The blow crushes your left foot.  Make an Average (+20) Endurance Test; if you fail, gain the Prone Condition and lose 1 toe, plus 1 additional toe for each SL below 0 -- Amputation (Average).  Gain 2 Bleeding Conditions.  If you don't receive Surgery within 1d10 days, you will lose the foot entirely.");
    elif 94<=cw and cw<=96:
        print("Severed Foot (5 Wounds): Your left foot is severed at the ankle and lads 1d10 feet away in a random direction -- Amputation (Hard) (See Scatter).  You gain 3 Bleeding, 2 Stunned, and 1 Prone Condition.");
    elif 97<=cw and cw<=99:
        print("Cut Tendon (5 Wounds): A major tendon at the back of your left leg is cut, causing you to scream out in pain as your leg collapses.  Gain 2 Bleeding, 2 Stunned, and 1 Prone Condition and look on in horor as your leg never works again -- Amputation (Very Hard).");
    elif cw == 100:
        print("Shattered Pelvis (Death): The blow shatters your pelvis, severing one leg then driving through to the next.  You die instantly from traumatic shock.");

def RLCritwoundtable():
    cw = random.randrange(1,101)
    if 1<=cw and cw<=10:
        print("Stubbed Toe (1 Wound): In the scuffle, you stub your right big toe.  Pass a Routine (+20) Endurance Test or suffer -10 on Agility Tests until the end of the next turn.");
    elif 11<=cw and cw<=20:
        print("Twisted Ankle (1 Wound): You go over your right ankle, hurting it.  Agility Tests suffer a -10 penalty for 1d10 rounds.");
    elif 21<=cw and cw<=25:
        print("Minor Cut (1 Wound): Gain 1 Bleeding Condition.");
    elif 26<=cw and cw<=30:
        print("Lost Footing (1 Wound): In the scuffle you lose your footing.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.");
    elif 31<=cw and cw<=35:
        print("Thigh Strike (2 Wounds): A painful blow slams into your right upper thigh.  Gain a Bleeding Condition and take an Average (+20) Endurance Test or stumble, gaining the Prone Condition.");
    elif 36<=cw and cw<=40:
        print("Sprained Ankle (2 Wounds): You sprain your right ankle, giving you a Torn Muscle (Minor) injury.");
    elif 41<=cw and cw<=45:
        print("Twisted Knee (2 Wounds): You twist your right knee too far.  Agility Tests suffer a -20 penalty for 1d10 rounds.");
    elif 46<=cw and cw<=50:
        print("Badly Cut Toe (2 Wounds): Gain 1 Bleeding Condition.  After the encounter, make a Challenging (+0) Endurance Test.  If you fail, lose 1 toe on your right foot -- Amputation (Average).");
    elif 51<=cw and cw<=55:
        print("Bad Cut (3 Wounds): Gain 2 Bleeding Conditions as a deep wound opens up your right shin.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.");
    elif 56<=cw and cw<=60:
        print("Badly Twisted Knee (3 Wounds): You badly twist your right knee trying to avoid your opponent.  Gain a Torn Muscle (Major) injury.");
    elif 61<=cw and cw<=65:
        print("Hacked Leg (3 Wounds): A cut bites down into the right hip.  Gain 1 Prone and 2 Bleeding Conditions, and suffer a Broken Bone (Minor) injury.  Further, take a Hard (-20) Endurance Test or also gain a Stunned condition from the pain.");
    elif 66<= cw and cw<=70:
        print("Torn Thigh (3 Wounds): Gain 3 Bleeding Conditions as the weapon opens up your left upper thigh.  Pass a Challenging (+0) Endurance Test or gain the Prone Condition.  Until you receive Surgery to stitch up the wound, each time you receive Damage to this Leg, also receive 1 Bleeding Condition.");
    elif 71<= cw and cw<=75:
        print("Ruptured Tendon (4 Wounds): Gain a Prone and Stunned Condition as one of your tendons on your right leg tears badly.  Pass a Hard (-20) Endurance Test or gain the Unconscious Condition.  Your leg is useless (see Amputated Parts).  Suffer a Torn Muscle (Major) injury.");
    elif 76<=cw and cw<=80:
        print("Carved Shin (4 Wounds): The weapon drives clean through your right leg by the knee, slicing into bone and through tendons.  Gain a Stunned and Prone Condition.  Further, suffer a Torn Msucle (Major) and Broken Bone (Minor) injury.");
    elif 81<=cw and cw<=85:
        print("Broken Knee (4 Wounds): The blow hacks into your right kneecap, shattering it into several pieces.  You gain 1 Bleeding, 1 Prone, and 1 Stunned Condition, and a Broken Bone (Major) injury as you fall to the ground, clutching your ruined leg.");
    elif 86<=cw and cw<=90:
        print("Dislocated Knee (4 Wounds): Your right knee is wrenched out of its socket.  Gain the Prone Condition.  Pass a Hard (-20) Endurance Test, or gain the Stunned Condition, which is not removed until you recieve Medical Attention.  After this initial Medical Attention, an Extended Average (+20) Heal Test needing 6 SL is required to reset the knee at which point you regain its use.  Movement is halved, and Tests made using this leg suffer a -10 penalty for d10 days.");
    elif 91<=cw and cw<=93:
        print("Crushed Foot (5 Wounds): The blow crushes your right foot.  Make an Average (+20) Endurance Test; if you fail, gain the Prone Condition and lose 1 toe, plus 1 additional toe for each SL below 0 -- Amputation (Average).  Gain 2 Bleeding Conditions.  If you don't receive Surgery within 1d10 days, you will lose the foot entirely.");
    elif 94<=cw and cw<=96:
        print("Severed Foot (5 Wounds): Your right foot is severed at the ankle and lads 1d10 feet away in a random direction -- Amputation (Hard) (See Scatter).  You gain 3 Bleeding, 2 Stunned, and 1 Prone Condition.");
    elif 97<=cw and cw<=99:
        print("Cut Tendon (5 Wounds): A major tendon at the back of your right leg is cut, causing you to scream out in pain as your leg collapses.  Gain 2 Bleeding, 2 Stunned, and 1 Prone Condition and look on in horor as your leg never works again -- Amputation (Very Hard).");
    elif cw == 100:
        print("Shattered Pelvis (Death): The blow shatters your pelvis, severing one leg then driving through to the next.  You die instantly from traumatic shock.");
