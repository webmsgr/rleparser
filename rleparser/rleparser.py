
class RLEParser:
    def __init__(self):
        self.parsed = []
        self.input = []
        self.complete = False
    def _parsedataline(self,line):
        lines = line.split("$")
        for line in lines:
            amt = ""
            print()
            for char in line:
                if char in "bo":
                    if amt == "":
                        amt = "1"
                    amountof = int(amt)
                    print(char*amountof)
                    amt = ""
                elif char == "!":
                    pass
                elif char in "0123456789":
                    amt += char
                else:
                    pass
    def parse(self,inp):
        self.input = inp.strip().split("\n")
        hasmet = False
        for line in self.input:
            if line.strip()[0] == "#":
                print("Tag line: {}".format(line))
            else:
                if hasmet:
                    print("Data line: {}".format(line))
                    self._parsedataline(line)
                else:
                    hasmet = True
                    print("Header: {}".format(line))
def main():
    data = open("glider.rle").read()
    parser = RLEParser()
    parser.parse(data)
if __name__ == "__main__":
    main()
