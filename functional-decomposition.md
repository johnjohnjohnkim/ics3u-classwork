# Functional Decomposition

## Getting food from a vending machine

#### Vending machine from a human perspective

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

#### Vending Machine from a machine's perspective
- Wait on standby until someone presses any button to start
    - Display "Press any button to start"
- Display price of the corresponding ID number the human presses
    - Display for 3 seconds
- Dispense the item when the correct price is paid
    - Give correct change to customer if more than the required amount is paid
    - Push the item out from the rack to the bottom
    
#### Identify where there might be basic programming concepts in your break-down above.
- Variables are each unique ID nummbers, which have different prices
- Loop showing the same messages until a button is pressed
- Conditional Branching
    - If money is paid, dispense correct item, otherwise go back to first step


#
