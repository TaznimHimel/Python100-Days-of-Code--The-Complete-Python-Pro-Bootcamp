print("W e l c o m e     t o     T r e a s u r e     I s l a n d.")
print("Y o u r     m i s s i o n     i s     t o     f i n d     t h e     t r e a s u r e.")
choice1 = input('You\'re at a cross road, where do you want to go? Type "Left" or "Right"?\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').lower()
    if choice2 == "wait":
        #Game will continue
        choice3 = input('You\'ve arrived at the Island unharmed. There is house with 3 doors. One Red, one Yellow and one Blue. Which color do you choose?\n').lower()
        if choice3 ==  "red":
            print("I t ' s     a     r o o m     f u l l     o f     f i r e .    G a m e     o v e r! ")
        elif choice3 == "yellow":
            print("Y o u     h a v e     w i n     t h e     g a m e!!     Y o u     g o t     t h e     h i d d e n     t r e a s u r e     o f     t h e     i s l a n d.    E n j o y! ")
        elif choice3 == "blue":
            print("I t ' s     a     r o o m     f u l l     o f  b e a s t s.    G a m e     O v e r!")
        else:
              print("Y o u ' v e     c h o o s e d     a     d o o r     t h a t     d o e s n ' t     e v e n     e x i s t. G a m e     o v e r! ")
    else:
        print("Y o u r ' r e     a t t a c k e d     b y  a n     a n g r y     c r o c o d i l e!")
else:
    print("Y o u     f e l l     i n t o     a     h o l e.    G a m e     O v e r!")
