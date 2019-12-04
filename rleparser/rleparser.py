
class RLEParser:
    def __init__(self):
        self.parsed = []
        self.input = []
        self.complete = False
    def parse(self,inp):
        self.input = inp.split("\n")
        hasmet = False
        for line in self.input:
            if line.strip()[0] == "#":
                print("Tag line: {}".format(line))
            else:
                if hasmet:
                    print("Data line: {}".format(line))
                else:
                    hasmet = True
                    print("Header: {}".format(line))
     