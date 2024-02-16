# use the open function to read from a file
file = open("test_file.txt")
# now we have an io object, we can use it to read the content of the file
content = file.read()  # the read function will read all the content of the file

print(content)

# important to close
file.close()

FILE = "test_file.txt"

# we can use with keyword to automatically close and open files
with open(FILE) as file:
    content = file.read()
    # now we can parse the data
    content_list = content.split(",\n")
    print(content_list)
    content_dict = {}
    for element in content_list:
        split = element.split(":")
        content_dict[split[0].lower()] = int(split[1])

    print(content_dict)
    print(content_dict["first"])
