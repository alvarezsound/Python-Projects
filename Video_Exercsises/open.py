import os


def writeData():
    data = "\nHello, World!"
    with open('test.rtf', 'a') as f:
        f.write(data)
        f.close()

def openFile():
    with open('test.rtf', 'r') as f:
        data = f.read()
        print(data)
        f.close()


if __name__ == "__main__":
    writeData()
    openFile()
