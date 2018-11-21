class Game:
    def __init__(self):
        self.__nCurrent = 0
    def takeTurn(self, sPhone, sInput):
        self.__nCurrent += 1
        return[sInput + " sms from " + sPhone + " answered here " + str(self.__nCurrent)]

