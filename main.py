

def main():
    print("Project_Xray, V0.0")

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
    #         be able to fork a group, duplicating it while renaming it

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


class SourceGroup:
    def __init__(self):
        pass
