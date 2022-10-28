import random # 랜덤 모듈

def cardScore(card): # 카드 숫자의 합을 계산하는 함수
    score = 0
    for n in card:
        if type(n) == int:
            score += n
        elif n == 'A':
            if score <= 10:
                score += 11
                if score > 21:
                    score -= 10
            else:
                score += 1
        elif n == 'J' or 'Q' or 'K':
            score += 10
    return score

def compare(player_score, dealer_score): # 승패를 결정하기 위해 플레이어와 딜러의 점수를 비교하는 함수
    if player_score > 21 and dealer_score > 21:
        return "패배"
    if player_score == dealer_score:
        return "무승부"
    elif dealer_score == 21:
        return "패배"
    elif player_score == 21:
        return "블랙잭! 승리!"
    elif player_score > 21:
        return "패배"
    elif dealer_score > 21:
        return "승리"
    elif player_score > dealer_score:
        return "승리"
    else:
        return "패배"

def play_game(): # 블랙잭 게임 시작
    print("블랙잭!!")

    money = 100 # 플레이어 초기 자금
    while True: # 플레이어 소지 자금이 전부 잃게 되면 게임은 즉시 종료
        if money <= 0:
            print("모든 돈을 잃으셨습니다. 패배!!!")
            break

        deck = []
        player_cards = []
        dealer_cards = []
        game_over = False

        for i in range(4):
            for j in ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'):
                deck.append(j)
        random.shuffle(deck)
        player_cards.append(deck.pop()) # pop 함수를 넣은 이유는 카드를 뽑으면 기존에 있던 덱에 뽑은 카드를 제거하기 위함
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

        while True:
            print(f"소지금액 : {money}")
            bet = input("배팅할 금액을 입력하세요.(단, 숫자만 입력하세요.)")
            if not bet.isdigit(): # 숫자를 판단하는 함수
                print("숫자를 입력하세요.")
            elif int(bet) > money: # 여기서 if 를 넣었을 때 오류가 났음
                print("자신이 소지한 금액보다 큰 금액은 배팅할 수 없습니다.")
            else:
                bet = int(bet)
                money -= bet
                break

        while not game_over:
            player_score = cardScore(player_cards)
            dealer_score = cardScore(dealer_cards)
            print(f"   당신의 카드 : {player_cards}, 카드 점수 : {player_score}")
            print(f"   컴퓨터 카드 : {dealer_cards[0]}, ?")

            if player_score == 21 or dealer_score == 21 or player_score > 21:
                game_over = True
            else:
                player_choice = input("카드 한장을 더 받으려면 'h'를 입력하고 받지 않는다면 's'을 누르세요: ")
                if player_choice == "h":
                    player_cards.append(deck.pop())
                elif player_choice == "s":
                    game_over = True
                else:
                    print("입력이 잘못되었습니다.'h'혹은 's' 키를 눌러주세요")

        while dealer_score < 17:
            dealer_cards.append(deck.pop())
            dealer_score = cardScore(dealer_cards)
            player_score = cardScore(player_cards)

        if compare(player_score, dealer_score) == "패배":
            money = money
        elif compare(player_score, dealer_score) == "무승부":
            money += bet
        else:
            money += bet*2
        print(f"   당신의 최종 카드 : {player_cards}, 최종 점수 : {player_score}, 소지 금액 : {money}")
        print(f"   딜러의 최종 카드: {dealer_cards}, 최종 점수 : {dealer_score}, 소지 금액 : {money}")
        print(compare(player_score, dealer_score))

while input("블랙잭 게임을 하시겠습니까? 'y' or 'n': ") == "y":
    play_game()
