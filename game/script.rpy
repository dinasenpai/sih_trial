init python:
    def play_advance_sound():
        renpy.sound.play("audio/click.mp3")  # Replace with your sound file

# $ play_advance_sound()

# Declare characters used by this game.
define mysterious_person = Character("???")
define m = Character("Mira", what_color="#ffc0cb")
define mc = Character("Protagonist", what_color="#ffcc00")
define narrate = Character("Narrator")

# Scene 1: The Past

label start:

    # Play background music
    play music "sad_music.mp3"

    # mysterious_person speaks (replace with character name later if needed)
    mysterious_person "That time… those years of suffering… they still haunt me."
    
    mysterious_person "No matter how much I try to forget, they always find a way back… creeping into my thoughts like the shadows that dance on these walls."

    mysterious_person "Something was lurking..."

    mysterious_person "Something dark, something invisible..."

    mysterious_person "Seeping into the water, poisoning everything it touched."

    mysterious_person "At first, it was just whispers, rumours… someone’s skin had darkened… another’s hands were covered in sores… a child fell ill, and then another."

    # Show a background image (replace with the appropriate background)
    pause 1.0 # Pauses for 1 seconds
    scene father with fade
    pause 1.0 # Pauses for 1 seconds

    mysterious_person "I remember the day my father first showed signs… his hands, strong and capable, now marked with dark spots."

    mysterious_person "At first, he laughed it off, said it was nothing, just the sun playing tricks… but deep down, I saw the fear in his eyes." 
    
    mysterious_person "He knew something was terribly wrong."
    
    mysterious_person "Days turned into weeks… and the sickness spread like wildfire." 
    
    mysterious_person "The wells, the ponds… they were all tainted. We tried to understand… tried to fight back…" 
    
    mysterious_person "But how do you fight what you cannot see? How do you protect yourself from the very water you need to survive?"

    # Show a new background image (e.g. a darkening village or affected environment)
    pause 1.0 # Pauses for 1 seconds
    scene people_suffering with dissolve
    pause 1.0 # Pauses for 1 seconds

    mysterious_person "And then, the tragedy began." 
    
    mysterious_person "My neighbours, my friends… one by one, they fell." 
    
    mysterious_person "The funerals became a daily ritual, the wails of mourning a constant echo through our village."
    
    mysterious_person "Every day, I watched the smoke rise… thick and dark against the sky." 
    
    mysterious_person "I remember the taste of ashes on my tongue… the smell of burning wood, the cries of the grieving… it was all too much."

    mysterious_person "Arsenic… a word that came to define our lives, our deaths… a poison that seeped into our blood, our bones…" 
    
    mysterious_person "…leaving us hollow and broken."

    # Show another background (perhaps a burning pyre or a darkened sky)
    pause 1.0 # Pauses for 1 seconds
    scene sad_bg with fade
    pause 1.0 # Pauses for 1 seconds

    mysterious_person "I watched my father wither away, day by day… his body consumed by pain." 
    
    mysterious_person "My mother, once so strong, was a shadow of herself, trying to hold us together, trying to find hope where there was none."
    
    mysterious_person "And all I could do was watch… helpless… terrified…" 
    
    mysterious_person "…knowing that the same fate awaited us all."

    # Background of a darkened village or sick individuals
    pause 1.0 # Pauses for 1 seconds
    scene people_suffering_2 with dissolve
    pause 1.0 # Pauses for 1 seconds

    mysterious_person "Years passed, but the scars remain… in the land, in our hearts… in our memories." 
    
    mysterious_person "I still hear their cries… those who were lost… those who suffered… because of something we never saw coming."
    
    mysterious_person "Over 20 million people suffered in West Bengal, 10 million in Bihar… all victims of the unseen poison." 
    
    mysterious_person "Arsenic in the water brought severe pain – skin lesions, cancers of the skin, bladder, and lung, hearts that failed, children born with poisoned blood."

    mysterious_person "Thousands died; countless more suffered with arsenicosis – darkened skin, gangrene, cancers." 
    
    mysterious_person "The poison was relentless… spreading silently, claiming lives and destroying dreams." 
    
    mysterious_person "Our homes turned into graves; our bodies marked by the water we once trusted." 
    
    mysterious_person "This was not just a tragedy…" 
    
    mysterious_person "It was a slow, cruel massacre."

    # Show a final background representing loss and emptiness (perhaps an empty village or a desolate landscape)
    pause 1.0 # Pauses for 1 seconds
    scene sad_bg with fade
    pause 1.0 # Pauses for 1 seconds

    mysterious_person "But this… this was just one story… one of many." 
    
    mysterious_person "Across our land, such tragedies have played out again and again…" 
    
    mysterious_person "Different places, different people, but the same fate…" 
    
    mysterious_person "…the same suffering."
    
    mysterious_person "And I… I wish… oh, how I wish…" 
    
    mysterious_person "That I could go back… back to that time… to those days before it all began…" 
    
    mysterious_person "To warn them… to save them… to change what happened."

    mysterious_person "But I cannot… I am bound by time, by fate… and all I have left are these memories…"
    
    mysterious_person "…memories of a tragedy that took everything from us."

    stop music fadeout 1.0

    scene black

    pause 2.0

# Scene 2: Waking Up

label Waking_Up:
    
    # Female voice gradually getting louder
    mysterious_person "…ir"
    pause 1.0
    mysterious_person "…Sir"
    pause 1.0
    mysterious_person "SIR !!!"
    pause 1.0
    
    # Show waking up background
    scene wake_up with fade

    # Background music
    play music "peace_music.mp3"
    pause 1.0
    
    # Mira's dialogue
    mysterious_person "Again? Really, you’ve done it again… another night without sleep?"
    
    # Protagonist slowly waking up
    
    pause 1.0
    narrate "(You slowly wake up.)"
    pause 1.0
    mc "Hm… what? Oh, it's you, Mira..."
    mc "Just… just a few more minutes." 
    mc "I was so close to connecting these data points from last year’s reports."
    
    # Mira responds
    m "Data points? You mean another ‘brilliant idea’ you had at 3 a.m.?" 
    m "Doctor, you need to rest! You can’t solve any crisis on three hours of sleep."
    narrate "(Mira sits beside you.)"
    pause 1.0
    
    # Play sound of chair being pulled
    play sound "chair_pull.mp3"
    
    # Show background of Mira sitting beside the protagonist
    pause 1.0
    scene scene1 with dissolve
    pause 1.0

    show old_mc1 at Position(xpos=0.25, ypos=1.0) with dissolve
    show assistant at Position(xpos=0.75, ypos=1.0) with dissolve

    # Protagonist responds
    mc "Come on, Mira, you know how it is… once you start digging through those old surveys and charts, it’s hard to stop."
    mc "There's always one more variable to consider or another trend to analyse."
    mc "But I know… I know." 
    mc "I’ve been at it a bit too long."
    
    # Mira worried
    m "A bit? You look like you’ve aged ten years overnight." 
    m "And don’t think I haven’t noticed the reports piling up in the corner or those letters from the council you’ve yet to open."
    m "We’re supposed to be working on the awareness campaign for the town hall meeting…" 
    m "…the one where you convince people not to dig their wells any deeper?"
    
    # Protagonist focused on the research
    mc "Yes, yes, the campaign. I promise I’ll focus… after I finish this analysis."
    mc "Just think, Mira… if we can show them the rate of depletion over the last decade, how we’re draining the aquifers faster than they can recharge—"
    
    # Mira interrupts
    m "Yes, I know. The ‘draining the veins of the earth’ speech. I’ve heard it a hundred times…" 
    m "But you’re not going to convince anyone if you collapse in the middle of it."
    m "Look, I’m worried about you. You’re not just some machine that can run on numbers and research alone."
    
    # Protagonist remains persistent
    mc "I’m fine, Mira. Really. I just… can’t help myself sometimes."
    mc "There’s too much at stake." 
    mc "People don’t realize… the water table’s dropping, and nobody’s paying attention."
    mc "And if I don’t do it, then who will?"
    
    # Mira reassures the protagonist
    m "I know… I know. But promise me you’ll take a break today? At least long enough to eat something."
    
    # Protagonist agrees
    mc "Alright, I promise. A break… but only if you promise to help me with these charts later."

    hide assistant with dissolve
    hide old_mc1 with dissolve
    
    # Mira responds
    
    show assistant at center with dissolve
    m "Deal. But breakfast first."
    
    # Sound of Mira pulling the protagonist by the arm
    pause 1.0
    play sound "rustle.mp3"
    pause 1.0
    
    # Scene of protagonist standing reluctantly
    narrate "(She pulls you by the arm.)"

    hide assistant with dissolve
    show old_mc1 at center with dissolve

    narrate "(You stand, reluctantly being pulled away from your desk, with your eyes lingering on the research papers.)"

    hide old_mc1 with dissolve
    
    
    # Fade out
    pause 1.0
    scene black with fade
    pause 1.0

    # Monologue - Protagonist reflecting on daily struggles
    mc "Each day feels like a race against an invisible clock."
    mc "The mornings come early, the light breaking over the skyline while I’m already pouring over yesterday’s reports, looking for patterns, searching for answers."
    mc "Coffee grows cold as I juggle calls, meetings, and presentations… officials nod politely but their eyes glaze over." 
    mc "School children seem more interested, but their parents remain sceptical."
    mc "Afternoon turns into a blur of voices, discussions in crowded community halls, on dusty streets, under the scorching sun… trying to make them care."
    mc "I feel the weight of their disbelief, their dismissive smiles."
    mc "And when the sun sets, my workday is far from over." 
    mc "Back to the office, more research and hopes pinned on the next big idea."

    stop music fadeout 1.0

    # End scene

# Scene: Late Night

label Late_Night:

    # Background image for the street (replace 'bg_street_night' with your own image)
    scene empty_streets with fade

    # Footsteps sound
    play sound "footsteps.mp3"  # Replace with actual file

    show old_mc1 at center with dissolve

    # Dialogue of mc
    mc "Tomorrow’s speech… it has to reach them."
    mc "I need to find the right words…" 
    mc "Something to break through their apathy and make them understand that this isn’t just about numbers on a chart."

    hide old_mc1 with dissolve

    # Footsteps slow down and background sound of wind
    play sound "wind_blows.mp3"  # Optional, replace with actual sound

    # mc notices the eerie street
    narrate "(You turn at a corner, footsteps slowing down as you look around the deserted street, with a hint of unease across your face.)"
    
    # A strange sound emerges
    play music "suspense.mp3"
    
    pause 1.0
    scene message with dissolve
    pause 2.0

    scene empty_streets with fade
    pause 1.0

    show old_mc1 at center with dissolve

    mc "What… what was that?"

    hide old_mc1 with dissolve

    narrate "(You look in all directions, peering into the shadows cast by the streetlights.)"

    show old_mc1 at center with dissolve

    mc "Hello? Who’s there?"

    hide old_mc1 with dissolve

    narrate "(There’s no response, just the hum growing slightly louder, then fading into the night air.)"

    show old_mc1 at center with dissolve

    mc "Must be my mind playing tricks… too many late nights must be giving me stress."

    hide old_mc1 with dissolve

    stop music fadeout 1.0

    # mc reaches the apartment
    narrate "(You try to dismiss the unease, and continue walking, reaching your apartment building a few minutes later.)"

    play sound "footsteps_small.mp3"

    narrate "(You fumble with the keys, glancing over your shoulder one last time before entering.)"

    # Scene: Inside the Apartment
    scene apartment with dissolve

    pause 1.0

    play sound "door_unlock.mp3"

    play music "night_music.mp3"

    show old_mc1 at center with dissolve

    mc "Finally... home."

    hide old_mc1 with dissolve
    
    narrate "(You sit down, rubbing your temples, muttering to yourself as you pick up a sheet of paper filled with scribbles.)"

    show old_mc1 at center with dissolve
    
    mc "Alright… focus… the speech. Just need to get it right. I need something that cuts deep… something that leaves them no choice but to listen."
    
    mc "The water we waste today… no, no… that’s too weak… we need… we need to hit them with the numbers… remind them of what’s already lost…"

    hide old_mc1 with dissolve

    # Show time passing, and fading to later hours
    narrate "(Time passes, the clock ticks loudly on the wall as you're lost in thought, with the night stretching on.)"
    
    narrate "(The scene darkens slightly and it's already 4 a.m.)"

    show old_mc1 at center with dissolve
    
    mc "4 am… again… Mira’s going to kill me."

    mc "Just need a few hours of sleep… got to be sharp for tomorrow… got to make them care."

    hide old_mc1 with dissolve

    stop music fadeout 1.0

    # mc goes to bed
    narrate "(You collapse onto the bed, your body sinking into the mattress. Your eyes close almost immediately...)"

    # The strange sound returns
    narrate "(...but as soon as you do, the strange sound returns – a low hum, then a whisper, barely audible but distinct.)"

    pause 1.0
    scene message with dissolve
    pause 2.0

    scene apartment with dissolve
    pause 1.0

    play music "mystical_music.mp3"

    show old_mc1 at center with dissolve

    mc "What…? Is that…?"
    mc "Who’s there?!"
    
    # The sound grows louder and the room begins to warp
    pause 1.0
    scene message with dissolve
    pause 2.0

    scene apartment with dissolve
    pause 1.0
    
    narrate "(You jump up, looking around wildly, but the room is the same – familiar yet now filled with an eerie, unexplainable tension.)"
    narrate "(Your breath quickens, eyes darting from corner to corner.)"

    show old_mc1 at center with dissolve
    
    mc "Show yourself! Who are you?! What do you want?!"

    hide old_mc1 with dissolve
    
    # The room starts to warp
    pause 1.0
    scene apartment_warped with dissolve
    
    pause 2.0
    scene message_complete with dissolve
    
    pause 2.0
    scene apartment_warped with dissolve
    pause 1.0

    narrate "(The voice grows louder, the walls seeming to pulse with the sound.)"
    narrate "(The room begins to warp, the edges blurring, as if reality itself is bending around him.)"

    pause 1.0
    scene black with dissolve
    pause 1.0
    
    mc "What… what is happening? Am I… am I dreaming?"
    
    pause 1.0

    narrate "(You blink rapidly, trying to clear your vision, but when your eyes open again, the sight leaves you utterly dumbfounded.)"
    narrate "(The room has transformed – into a place you do not recognize, filled with blinding light and shadow, a different presence all around.)"

    stop music fadeout 1.0

    return
