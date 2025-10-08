def display_heroes():
    heroes = read_heroes()

    for hero in heroes:
        hero_name = hero.split(',')[0]
        hero_power = hero.split(',')[1]
        print("\nSuperhero:",f"{hero_name} \nFirst_appearance: {hero_power}\n\n--------------------")


def read_heroes():
    file_path = str(input("Enter the path to the superheroes file: "))
    try:
        with open(file_path, 'r') as heroes:
            heroes = [line.strip() for line in heroes.readlines()]
        return heroes
    except FileNotFoundError:
        print("File does not exist - exiting")
    except: # catch all other exceptions
        print("An error occurred - exiting")
    else:
        file.close()
    finally:
        print("Goodbye!")

display_heroes()