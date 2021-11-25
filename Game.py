import random

class Game:
    def __init__(self):
        self.__nCurrent = -1
    def takeTurn(self, sInput):
        if(self.__nCurrent == -1):
            self.__nCurrent = 0
            return["Welcome to 20 + 1",
                   "in this game the object is to make the computer count 21",
                   "you count from 1-4 steps on the way to 21"
                ]
        else:
            aNumbers = sInput.split(",")
            for n in aNumbers:
                self.__nCurrent += 1
            if self.__nCurrent > 15:
                if self.__nCurrent == 20:
                    self.__nCurrent = -1
                    return["21", "you win"]
                else:
                    sNumbers = ""
                    while self.__nCurrent < 20:
                        if sNumbers != "":
                            sNumbers += ", "
                        self.__nCurrent += 1
                        sNumbers += str(self.__nCurrent)
                    self.__nCurrent = -1
                    return[sNumbers, "I win ... ha"]
            else:
                nCount = random.randint(1,4)
                sNumbers = ""
                for n in range(0, nCount):
                    if sNumbers != "":
                        sNumbers += ", "
                    self.__nCurrent += 1
                    sNumbers += str(self.__nCurrent)
                return[sNumbers]
                
if __name__ == '__main__':
    oGame = Game()

    while True:
        sInput = input("> ")
        sReturn = oGame.takeTurn(sInput)
        print(sReturn)
