import json

def createConfigEntry(configFile, fileExtension):
    commentDeclaration = input("Multiline Comment Declarations (enter both start and end declaration for multiline comments seperated by a comma): ").strip().split(",")
    functionType = input("Function Declaration (type 'default' to use the default identification '[A-Za-z0-9_*]{3,20} [A-Za-z0-9_]{1,50}?[\\(]'): ")
    commentStructure = input("Comment Structure (use 'FUNCTION', 'ARG', and 'DESCRIPTION' to mark out where each section should go. type 'default' for default structure 'FUNCTION\\n @param ARG\\n @description DESCRIPTION\\n'): ")

    if functionType.lower().strip() == "default":
        functionType = "[A-Za-z0-9_*]{3,20} [A-Za-z0-9_]{1,50}?[\\(]"

    if commentStructure.lower().strip() == "default":
        commentStructure = "FUNCTION\n @param ARG\n @description DESCRIPTION\n"

    newEntry = {
        "comment": commentDeclaration,
        "function": functionType,
        "structure": commentStructure
    }

    with open(configFile,"r") as file:
        try:
            json_config = json.load(file)
        except json.JSONDecodeError:
            print("File contents: "+ file.read())
            exit(-3)
        else:
            pass
        file.close()

    json_config["extensions"][0][fileExtension] = newEntry

    with open(configFile, "w+") as f:
        f.write(json.dumps(json_config, indent=2))
        f.close()
