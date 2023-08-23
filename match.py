name=input("What's your name? ")

match name:
    case "Harry"| "Hermione"| "Ron":
        print("gryffindor")
    
    case "Draco":
        print("Slyhterin")

    case _:
        print("Who? ")