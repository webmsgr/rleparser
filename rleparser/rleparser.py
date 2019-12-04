
class RLEParser:
    def __init__(self):
        self.parsed = []
        self.input = []
        self.deathrules = []
        self.liverules = []
        self.width = 0
        self.height = 0
        self.complete = False
    def _parsedataline(self,line):
        lines = line.split("$")
        linefound = 0
        for line in lines:
            amt = ""
            t = []
            linefound += 1
            foundthis = 0
            for char in line:
                if char in "bo":
                    if amt == "":
                        amt = "1"
                    amountof = int(amt)
                    print((" " if char == "b" else "o")*amountof,end="")
                    t += [char=="o"]*amountof
                    foundthis += amountof
                    amt = ""
                elif char == "!":
                    pass
                elif char in "0123456789":
                    amt += char
                else:
                    pass
            print(" "*(self.width-foundthis))
            t += [False]*(self.width-foundthis)
            self.parsed.append(t)
        blank = " "*self.width + "\n"
        print(blank*(self.height-linefound))
    def _parseheader(self,line):
        things = line.split(",")
        for thing in things:
            thing = thing.strip()
            thing = thing.split("=")
            thing = [u.strip() for u in thing if u.strip() != ""]
            if thing[0] == "x":
                self.width = int(thing[1])
            elif thing[0] == "y":
                self.height = int(thing[1])
            elif thing[0] == "rule":
                rules = thing[1].split("/")
                for rule in rules:
                    rule = list(rule)
                    print("{} -> {}".format(rule.pop(0),rule))
                
        #print(things)
    def parse(self,inp):
        self.input = inp.strip().split("!")[0].split("\n")
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
                    self._parseheader(line)
def main():
    data = open("glidergun.rle").read()
    parser = RLEParser()
    parser.parse(data)
    print(parser.__dict__)
if __name__ == "__main__":
    main()
