"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    villager_data=open(filename)
    species = set()
    for line in villager_data:
        new_line=line.split("|")
        species_type= new_line[1]
        species.add(species_type)

    return species

# print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    villager_data = open(filename)
    for line in villager_data:
        new_line = line.split('|')
        if search_string == new_line[1]:
            villagers.append(new_line[0])
        elif search_string == "All":
            villagers.append(new_line[0])

    return sorted(villagers)

#print(get_villagers_by_species('villagers.csv', search_string = 'Dog'))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    villager_data = open(filename)
    fitness_list = []
    nature_list = []
    education_list = []
    music_list = []
    fashion_list = []
    play_list = []
    for line in villager_data:
        new_line = line.split("|")
        name = new_line[0]
        hobby = new_line[3]
        if hobby == "Fitness":
            fitness_list.append(name)
        elif hobby == "Nature":
            nature_list.append(name)
        elif hobby == "Education":
            education_list.append(name)
        elif hobby == "Music":
            music_list.append(name)
        elif hobby == "Fashion":
            fashion_list.append(name)
        elif hobby == "Play":
            play_list.append(name)

    return [sorted(fitness_list), sorted(nature_list), sorted(education_list), sorted(music_list), sorted(fashion_list), sorted(play_list)]
    
# print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    villager_data = open(filename)
    all_data = []
    for line in villager_data:
        line=line.rstrip()
        new_line = line.split('|')
        all_data.append((new_line[:]))

    return all_data

# print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    villager_data = open(filename)
    for line in villager_data:
        line = line.rstrip()
        new_line = line.split("|")
        name = new_line[0]
        villager_motto = new_line[4]
        if villager_name == name:
            return villager_motto

# print(find_motto("villagers.csv","Bec"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    villager_data = open(filename)
    same_personality = set()
    for line in villager_data:
        new_line = line.split("|")
        name = new_line[0]
        if name == villager_name:
            personality = new_line[2]
    villager_data.close()

    villager_data = open(filename)
    for other_line in villager_data:    
        other_new_line = other_line.split("|")
        name = other_new_line[0]
        if personality == other_new_line[2]:
            same_personality.add(name)
    villager_data.close()
    return same_personality
    
#print(find_likeminded_villagers("villagers.csv", "Cyrano"))