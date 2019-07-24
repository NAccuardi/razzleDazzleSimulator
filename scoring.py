import random


def throwmarbles(numberofmarbles):
    random.seed()
    return random.sample(range(1, 120), numberofmarbles)


def getscore(board, marblepostions):
    score = 0
    for x in marblepostions:
        score += board[x]
    return score


def addpoints(score):
    return{
        8: 100,
        9: 100,
        10: 50,
        11: 30,
        12: 50,
        13: 50,
        14: 20,
        15: 15,
        16: 10,
        17: 5,
        39: 5,
        40: 5,
        41: 15,
        42: 20,
        43: 50,
        44: 50,
        45: 30,
        46: 50,
        47: 100,
        48: 100
    }.get(score, 0)


def translatescore(score, data):
    if 18 <= score <= 21:
        data["numberOfPrizes"] += 1
    elif score == 29:
        data["numberOfPrizes"] += 1
        data["priceToPlay"] *= 2
        data["numberoftimesdoubled"] +=1
    elif 35 <= score <= 38:
        data["numberOfPrizes"] += 1
    else:
        data["totalPoints"] += addpoints(score)


def oneturn(board, data):
    data["totalPlays"] += 1
    score = getscore(board, throwmarbles(8))
    translatescore(score, data)
