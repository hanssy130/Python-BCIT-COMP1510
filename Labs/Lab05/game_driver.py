from Lab05.functions import roll_die, generate_vowel, generate_consonant, generate_syllable, generate_name, \
    create_character, print_character, choose_inventory

#why is print_character doing stuff at the beginning?? nothing's calling it t the beginning
def main():
    #Enter the number of dice and how many sides to roll
    print("Examples of dice rolling:")
    print(roll_die(3,6))
    print(roll_die(3,6))

    #These automatically generate letter(s) once invoked.
    print("Examples of a vowel, a consonant, and then a syllable:")
    print(generate_vowel())
    print(generate_consonant())
    print(generate_syllable())

    #Enter how many syllables you want in your generated name.
    print("Example of a name with 4 syllables:")
    print(generate_name(4))

    #Creates a character with a name consisting of how many syllables you input. Randomly creates attributes.
    print("Example of a character whose name has 4 syllables:")
    print(create_character(4))

    #Prints an example character sheet.
    print("Example of a character's information")
    print_character(create_character(4))

    #Enter
    print("Inventory:")
    print("Bahamut Shackle, Dragon Fang, Gorgon Scale, Chimera Fur, and an Obsidian Fang")
    choice = int(input("Pick 1-5 items from the inventory to use:"))
    print(choose_inventory(["Bahamut Shackle", "Dragon Fang", "Gorgon Scale", "Chimera Fur", "Obsidian Fang"], choice))


if __name__=="__main__":
    main()
