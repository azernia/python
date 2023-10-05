def read_file(path):
    file = open(path, "r", encoding="utf-8")
    file_content = file.read()
    print(file_content)
    file.close()


def write_file(path, content):
    file = open(path, "w", encoding="utf-8")
    file.write(content)
    file.close()


if __name__ == "__main__":
    path = "../resources/a.txt"
    read_file(path)
    write_file(path=path, content="new content")
