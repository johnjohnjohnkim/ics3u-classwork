# Functional Decomposition

## Getting food from a vending machine

### Vending machine from a human perspective

You get a bag of chips from a vending machine
- Approach machine
    -Walk until you are within arm reach
- Determine the number for the flavour of the chips I want
    - Search for the specific flavour 
    - Look below bags for their ID number. (Remember that number)
- Insert appropriate amount of money into machine
    - Look beside the ID number for the cost of the snack
    - Get out some money greater or equal to that amount.
    - Place that money into the intake
- Key-in the number for the flavour of the bag
- Get bag from bottom of machine
    - Bend down
    - Put arm through slot
    - Grab chips
    - Pull your arm out (with the chips)

### Vending Machine from a machine's perspective
- Wait on standby until someone presses any button to start
    - Display "Press any button to start"
- Display price of the corresponding ID number the human presses
    - Display for 3 seconds
- Dispense the item when the correct price is paid
    - Give correct change to customer if more than the required amount is paid
    - Push the item out from the rack to the bottom
    
### Identify where there might be basic programming concepts in your break-down above.
- Variables are each unique ID nummbers, which have different prices
- Loop showing the same messages until a button is pressed
- Conditional Branching
    - If money is paid, dispense correct item, otherwise go back to first step



## People who can't park


### How do you fix this problem?
- Split cookie in half
- Crush cookie into smaller pieces
- Force cookie into glass, even if it breaks
- Flip cup upside down while cookie is stuck in cup

### How can you prevent this problem
- Get a cup with a bigger diameter at the top
- Make/obtain smaller cookie

### How can this problem be solved with an app?
- The app is able to identify the diameter of the cup
- App shows recipes for cookies that vary in legnth
- App identifies the model of the cup and suggests which sized cookie to buy/bake
- User is able to choose a default/favourite cup 
    - When cookie is scanned into the app, they can get recommended to buy or not
- User is also able to choose a default cookie instead, and get recommended cup sizes


## The spoon dropped into the gravy


### How do you fix this problem
- Remove the spoon from the gravy

### How can you prevent this problem? 
- Put lid on gravy when not using gravy
- Use a bigger spoon that's longer than the diagonal length of the gravy container

### How can this problem be solved with a robotic system?
- Use a robotic arm with electromagnets that lifts the fallen spoon from the gravy
- An arm that detects metal and picks up the metal objects with claws
- Robotic system that flips flips the gravy container spilling the gravy out, but also gets the spoon out as well
    - Not ideal
    

## People hogging seats with bags

### How do you fix this problem?
- Remove their bag from the seats
- Require proof of payment for each seat

### How can you prevent this problem?
- Make seats only available after showing your proof-of-payment

### How can this problem be solved with a technological solution?
- Seats are foldable
    - Only unfolds with proof-of-payment inserted
    - Uses camera and heat sensors to identify if the object on the seat is human or not
- Not removing an identified bag from a seat will signal the driver 
