# Prompt the user for the name of a file
filename = input("File name: ")

# Remove leading & trailing whitespaces & convert to lowercase
filename = filename.strip().lower()

# intialise empty extension for filenames that have no period
extension = ""
i = filename.rfind(".")
end = len(filename) - 1
# if filename has an extension, extract this
if i > 0:
    extension = filename[i:end+1]

match extension:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")