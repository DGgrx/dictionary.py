import json
from difflib import get_close_matches

# Banner
print("""  _____  _      _ _   _                              
 |  __ \(_)    (_) | (_)                             
 | |  | |_  ___ _| |_ _  ___  _ __   __ _ _ __ _   _ 
 | |  | | |/ __| | __| |/ _ \| '_ \ / _` | '__| | | |
 | |__| | | (__| | |_| | (_) | | | | (_| | |  | |_| |
 |_____/|_|\___|_|\__|_|\___/|_| |_|\__,_|_|   \__, |
                                                __/ |
                                               |___/ 
""")

data = json.load(open("dictionary.json", "r"))
x = input("Enter the Word you want to search: ").lower()
similar = get_close_matches(x, list(data.keys()))
print("\n")

# print(similar)


def disp(output):
    for i in range(0, len(output)):
        print(f"{i+1}. {output[i]}")
    print("")


def translate():
    if x in data:
        output = data[x]
        disp(output)
    elif x.title() in data:
        output = data[x.title()]
        disp(output)
    elif x.upper() in data:
        output = data[x.upper()]
        disp(output)
    elif len(similar) != 0:
        print(f"Did you mean: {similar[0]}")
        output = data[similar[0]]
        disp(output)
    else:
        print("Word not found !\n")


translate()

choice = input("Do you want to search another word ? \n Type 'y' or 'n' : ")
while(choice != "n"):
    if choice == "y":
        x = input("\nEnter the Word you want to search: ").lower()
        print("\n")
        similar = get_close_matches(x, list(data.keys()))
        translate()
    else:
        print("\nPlease type 'y' or 'n' only. . .\n")
    choice = input(
        "Do you want to search another word ? \n Type 'y' or 'n' : ")
