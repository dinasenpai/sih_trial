# Declare characters used by this game.
define narrator = Character("Narrator")
define rohan = Character("Rohan")
define drpatel = Character("Dr. Patel")
define rukmini = Character("Rukmini")
define kumar = Character("Kumar")

# The game starts here.
label start:

    # Scene 1: The Village
    scene bg village_day
    play music "bgm_village.ogg"
    
    narrator "Kalagram, a village that has been struggling with water scarcity for years. The once-abundant groundwater has been depleting rapidly, threatening the livelihoods of the villagers."

    # Scene 2: Rohan's Farm
    scene bg farm_day
    play music "bgm_farm.ogg"
    
    show rohan neutral at center
    rohan "Another day, another struggle to find enough water for our crops. I wish there was a way to make our water last longer."
    
    narrator "Rohan's family has been farming this land for generations. But with the water crisis worsening, he's determined to find a solution."

    # Scene 3: Meeting Dr. Patel
    scene bg village_path_day
    play sound "sfx_footsteps.ogg"
    
    show drpatel neutral at right
    show rohan neutral at left
    
    drpatel "Rohan, my boy, I've been studying the water table in Kalagram. We need to take drastic measures to conserve our groundwater. We can't keep relying on traditional farming methods."
    
    rohan "What do you suggest, Doctor? I'm willing to try anything to save our farm."
    
    drpatel "I recommend we implement microirrigation. It's a more efficient way to water your crops, and it will help reduce our water consumption."

    # Choice 1
    menu:
        "Implement microirrigation on your farm":
            jump choices1_a

        "Stick to traditional flood irrigation":
            jump choices1_b

        "Ask Dr. Patel about other options":
            jump choices1_c

label choices1_a:
    narrator "You choose to implement microirrigation, learning about its benefits and starting the process on your farm."
    jump scene4

label choices1_b:
    narrator "You choose to stick with traditional flood irrigation. The groundwater levels deplete faster, and the village faces a severe drought."
    jump drought_ending

label choices1_c:
    narrator "You ask Dr. Patel about other conservation practices but decide not to implement microirrigation immediately."
    jump scene4

label scene4:

    # Scene 4: Implementing Microirrigation
    scene bg farm_day
    play music "bgm_farm.ogg"
    
    show rohan neutral at left
    show drpatel neutral at right
    
    drpatel "First, we need to install a network of pipes and tubes to deliver water directly to the roots of the plants. Then, we'll use a pump to pressurize the water and distribute it evenly."
    
    rohan "That sounds like a lot of work. But if it will save us water, I'm willing to try it."
    
    drpatel "It's worth it, Rohan. Microirrigation can reduce water consumption by up to 50\%. And with the right crops, we can increase our yields and improve the soil quality."

    # Scene 5: Meeting Rukmini
    scene bg farm_day
    play sound "sfx_working.ogg"
    
    show rukmini neutral at right
    show rohan neutral at left
    
    rukmini "Rohan, I'm so proud of you for taking steps to conserve water. But we need to do more. We need to diversify our crops and reduce our reliance on water-intensive crops like paddy and sugarcane."
    
    rohan "I agree, but what can we plant instead?"
    
    rukmini "We can plant millets and pulses. They're more drought-resistant and require less water. Plus, they're nutritious and can improve the soil quality."

    # Choice 2
    menu:
        "Plant millets and pulses":
            jump choices2_a

        "Stick to traditional crops":
            jump choices2_b

        "Ask Rukmini about other options":
            jump choices2_c

label choices2_a:
    narrator "You choose to plant millets and pulses, learning about the benefits of crop diversification and starting the process on your farm."
    jump scene6

label choices2_b:
    narrator "You choose to stick with traditional crops. The water consumption increases, and the groundwater levels deplete faster."
    jump drought_ending

label choices2_c:
    narrator "You ask Rukmini about other conservation practices but decide not to diversify your crops immediately."
    jump scene6

label scene6:

    # Scene 6: Kumar's Offer
    scene bg farm_day
    play sound "sfx_footsteps.ogg"
    
    show kumar neutral at right
    show rohan neutral at left
    show rukmini neutral at center
    
    kumar "Rohan, I'll give you a good price for your groundwater. You can sell it to me, and I'll take care of the rest."
    
    rohan "I don't know, Kumar. I'm not sure I want to sell our water."
    
    kumar "Come on, Rohan. You need the money, and I need the water. It's a win-win situation."
    
    rukmini "Rohan, don't do it. Selling our water will only make things worse. We need to conserve it, not sell it."

    # Choice 3
    menu:
        "Accept Kumar's offer":
            jump choices3_a

        "Reject Kumar's offer":
            jump choices3_b

        "Negotiate with Kumar":
            jump choices3_c

label choices3_a:
    narrator "You choose to accept Kumar's offer. The groundwater levels deplete rapidly, and the village faces severe water scarcity."
    jump drought_ending

label choices3_b:
    narrator "You choose to reject Kumar's offer, learning about the importance of sustainable groundwater management and starting to implement conservation practices."
    jump scene7

label choices3_c:
    narrator "You choose to negotiate with Kumar, learning about the importance of balancing economic and environmental needs."
    jump scene7

label scene7:

    # Scene 7: Artificial Recharge
    scene bg farm_day
    play sound "sfx_construction.ogg"
    
    show drpatel neutral at right
    show rohan neutral at left
    
    drpatel "We can build a recharge well and collect rainwater to replenish the groundwater. It's a simple and effective way to increase our water table."
    
    rohan "That sounds like a great idea, Doctor. Let's do it."
    
    drpatel "Excellent decision, Rohan. Artificial recharge can increase groundwater levels and improve water quality."

    # Scene 8: Watershed Management
    scene bg village_hill_day
    play sound "sfx_nature.ogg"
    
    show rukmini neutral at right
    show rohan neutral at left
    
    rukmini "We can plant trees and grasses on the slopes to reduce runoff and increase infiltration. It's a simple and effective way to manage our watershed."
    
    rohan "That's a great idea, Rukmini. Let's do it."
    
    rukmini "Excellent decision, Rohan. Watershed management can reduce runoff, increase groundwater recharge, and improve the water quality."

    # Scene 9: The Harvest
    scene bg farm_harvest
    play music "bgm_harvest.ogg"
    
    show rohan happy at center
    show rukmini happy at right
    
    rohan "Look, Rukmini! Our crops are thriving! We've never had a better harvest."
    
    rukmini "It's all thanks to our conservation efforts, Rohan. We've reduced our water consumption, and our crops are more resilient to drought."
    
    show drpatel happy at left
    drpatel "Congratulations, Rohan and Rukmini! You've shown that with the right conservation practices, we can manage our groundwater sustainably and improve our livelihoods."

    # Ending
    narrator "The game ends with a message about the importance of sustainable groundwater management and the benefits of conservation practices. The player is encouraged to continue exploring and learning about groundwater conservation."

    # Epilogue
    narrator "As the player continues to explore the game, they can learn more about groundwater conservation and management. They can also experiment with different conservation practices and see the consequences of their choices. The game ends with a sense of hope and empowerment, encouraging the player to take action to protect their own water resources."

    return

label drought_ending:
    
    scene bg drought_farm

    narrator "The village faces a severe drought due to unsustainable practices. The game ends with a message about the consequences of poor water management and the importance of conservation."
    return
