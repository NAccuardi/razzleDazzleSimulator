from board import createboard, printboard
from scoring import oneturn


def main():
    gamedata = {
        "totalPoints": 0,
        "numberOfPrizes": 0,
        "priceToPlay": 1,
        "totalPlays": 0,
        "numberoftimesdoubled": 0
    }

    gameboard = createboard()

    while gamedata["totalPoints"] <= 100:
        oneturn(gameboard, gamedata)
    print(gamedata)


main()
