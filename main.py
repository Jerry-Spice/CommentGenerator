import sys
import re
import json
from configgenerator import *

"""
def figure_multi_line_comment_string(filename)
 * filename:
 -> This function figures out what the multiline comment is for a given file
"""
def figure_file_information(filename):
    extension = filename.split(".")[-1]
    with open("/home/jerryspice/Documents/CodingProjects/CommentGenerator/config.json","r") as file:
        json_config = json.loads(file.read(), strict=True)
        file.close()
    try:
        configInfo = [json_config["extensions"][0][extension]["comment"], json_config["extensions"][0][extension]["function"], json_config["extensions"][0][extension]["structure"]]
        return configInfo
    except KeyError:
        if (input("Config for filetype '." + extension + "' not found...\nWould you like to create one [y/n]? ").strip().lower() == "y"):
            createConfigEntry("/home/jerryspice/Documents/CodingProjects/CommentGenerator/config.json", extension)
            return figure_file_information(filename)
        else:
            print("Wrote no comments")
            exit(-2) # Err wrote no comments
    else:
        print("Something horribly wrong happened")
        exit(-10) # Something  horribly wrong happened.



"""
def file_lines(filename)
 * filename:
 -> This function reads a file and splits the function data up into lines
"""
def file_lines(filename):
    f = open(filename,"r")
    data = f.read().split("\n")
    f.close()
    return data

"""
def write_output(filename,  content)
 * filename
 * content:
 -> This function takes in a filename and some content and writes the content to the file
"""
def write_output(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

"""
def check_pattern(data,  pattern)
 * data
 * pattern:
 -> This function takes in a string and regex pattern and checks if the pattern is in the string
"""
def check_pattern(data, pattern):
    result = re.search(pattern, data)
    if result is not None:
        return [result.span()[0],result.span()[1]]
    return None

"""
def write_comments(function,  multiline_comment)
 * function
 * multiline_comment:
 -> This function takes in a function string and the string for a multiline comment and then writes the comment structure for that function
"""
def write_comments(function, multiline_comment, comment_structure):
    function = function.split(")")[0]
    functionType = function.split("(")[0].split(" ")[0]
    functionName = function.split("(")[0].split(" ")[1]
    functionArguments = function.split("(")[1]
    functionArguments = functionArguments.split(",")

    msg = multiline_comment[0] + '\n'
    msg += comment_structure.replace("FUNCTION", function + ")").replace("DESCRIPTION", "blah blah blah")
    arg_structure = comment_structure.split("\n")[1]

    msg = msg.replace(arg_structure, (arg_structure+"\n")*len(functionArguments))

    for i in range(len(functionArguments)):
        msg = msg.replace("ARG", functionArguments[i].strip(), 1)

    msg += multiline_comment[1]

    return msg

def process_file(filename):
    print("\n----------\n")
    spots = []
    lines = file_lines(filename)
    newFileData = ""
    print("Figuring format from Config...")
    comment_info = figure_file_information(filename)
    multiline_comment = comment_info[0]
    function_regex = comment_info[1]
    comment_structure = comment_info[2]
    print("Writing Comments...")
    for g in range(len(lines)):
        result = check_pattern(lines[g], function_regex)
        if result is not None:
            newFileData += write_comments(lines[g], multiline_comment, comment_structure) + "\n"
        newFileData += lines[g] + "\n"

    write_output(filename, newFileData)
    print("Done with " + filename + "!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Err too few inputs. Please enter a filename to parse")
        exit(-1) # Too Few Input
    for i in range(1, len(sys.argv), 1):
        process_file(sys.argv[i])
