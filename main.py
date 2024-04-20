print("Enter the file directory to add comments to.")
filename = input("File Directory>>>")
with open(filename, "r") as f:
    data = f.read().split("\n")
    f.close()

result = []



for i in range(len(data)):
    if "public" in data[i] and "class" not in data[i]:
        result.append("/**")
        result.append(" * ")
        result.append(" * SampleTextSampleText")
        result.append(" * ")
        is_constructor = len(data[i].split("(")[0].replace("    ", "").split(" ")) == 2
        if is_constructor:
            if data[i].split("(")[1][0] != ")":
                arguments = data[i].split("(")[1].split(")")[0].split(",")
                for g in range(len(arguments)):
                    result.append(" * @param " + arguments[g].split(" ")[1])
                    result.append(" *     SampleTextSampleText")
                    result.append(" * ")
        else:
            return_type = data[i].replace("    ", "").split(" ")[1]
            if data[i].split("(")[1][0] != ")":
                arguments = data[i].split("(")[1].split(")")[0].split(",")
                for g in range(len(arguments)):
                    result.append(" * @param " + arguments[g].split(" ")[1])
                    result.append(" *     SampleTextSampleText")
                    result.append(" * ")
            if return_type != "void":
                result.append(" * @return " + return_type)
                result.append(" * ")
        result.append("*/")
    result.append(data[i])



msg = ""

for i in range(len(result)):
    msg += result[i] + "\n"

# print(msg)

with open(filename, "w+") as f:
    f.write(msg)
    f.close()

