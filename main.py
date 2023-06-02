source_list = 'sourceList.txt'  # Specify the file where sources are stored and read from


class SourceGroup:
    name = ""  # Stores name of group
    sources = None  # list of sources within group

    def __init__(self, name):
        self.name = name


def main():
    print("Project_Xray: V0.0")

    # Create a list of groups
    groups = []

    # Import from file:
    f = open(source_list, "r+", encoding='utf-8')  # Open file for reading
    for line in f:  # For all lines
        if line[0] == '#':  # If the line starts with a # [group declaration], create a new group.
            groups.append(SourceGroup(line[2:]))

    for group in groups:
        print(group.name)

    # Feature Overview:
    #     Has a list of sources, read from a file, which can be put into arbitrary groups
    #     Each source in each group has a 'weight'
    #     When pulling from sources, each item from will be ordered by its age, times its weight, ascending
    #     Everything stored to a file, such that it will be preserved. File structure currently undecided.
    #     View each group, and add or remove sources from it, as well as view and change weight's within a group
    # Options:
    #     Mark off items, hiding them
    #     Open each item as a link to view its content
    #     Future/Less necessary:
    #         be able to fork a group, duplicating while renaming it
    # Interaction Mockup/Description:
    #   Opens, maybe show's some debug text for a second, and them generates a list of groups, shown as:
    #       | [Number, formatted to say three digits]: [Unread items, formatted to 4 digits] [Name]
    #   When one is selected, via entering the number of the group [maybe add some text explaining hwo to do this]
    #   Display ~10/20 entries, and ask for either u/d to go up or down the entries, h to toggle hiding read entries, -
    #       -a h preceding a number [ex. h5] to hide/unhidden an entries, and just entering a number to open it, -
    #       -[should this make it mark it as hidden? as well? possibly open it, and bring you to another temp screen, -
    #       -where you can type y/n to mark it read if desired?

    # Todo List:
    #   File i/o
    #   Pull new items from sources and add them to group
    #   Viewer for sources, done as a cli
    #   Ability to mark items as 'read' and hide them from viewer -- intentionally left till later

if __name__ == '__main__':
    main()
