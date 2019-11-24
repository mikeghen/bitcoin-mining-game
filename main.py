import numpy as np

def main():

    welcome_message()

    """
    Difficulty, exchange price, and computer power costs are
    set to logorithms where difficulty and exchange price increase
    while computer power cost decreases
    """
    # Current: 12 x 10 ^ 12
    difficulty = np.logspace(1,13,10)
    reward = [50,50,50,25,25,25,12.5,12.5,12.5,6.25]
    # Current: ~$10,000
    exchange_price = np.logspace(-2,5,10)
    # Current: ~0.02 $/TH/s
    computer_power_cost = np.logspace(8,-2,10)

    """
    You start of with $1000 in your bank account
    """
    account = [{
        "usd": 1000,
        "bitcoins": 0,
        "computer_power": 0
    }]

    for i in range(0, 10):
        print("--------------------------")
        print("Round", i)
        print("--------------------------")

        account_balance, account_bitcoins, computer_power = round_loop(account[i], \
                    difficulty[i], reward[i], exchange_price[i], computer_power_cost[i])
        account.append({
            "usd": account_balance,
            "bitcoins": account_bitcoins,
            "computer_power": computer_power
        })

    return


def round_loop(account, difficulty, reward, exchange_price, computer_power_cost):
    """
    Choose how much computer power to buy
    """

    print("Current Exchange Price: ${0}".format(exchange_price))
    print("How much of your {0} BTC would you like to sell?"\
            .format(account["bitcoins"]))
    sell = None
    while sell == None or sell > account["bitcoins"] or sell < 0:
        sell = float(input("Enter a value between 0 and {0}: ".format(account["bitcoins"])))
    account_balance = account["usd"] + sell * exchange_price

    print("Computer Power Cost: {0} $/TH".format(computer_power_cost))
    print("How much of your ${0} would you like to use to buy computer power?"\
            .format(account_balance))
    spend = None
    while spend == None or spend > account_balance or spend < 0:
        spend = float(input("Enter a value between 0 and {0}: ".format(account_balance)))

    computer_power = spend / computer_power_cost
    account_balance = account_balance - spend

    print("The current difficulty is {0}".format(difficulty))
    print("You have purchased {0} TH/s for this round.".format(computer_power))
    print("Your current account balance is {0}".format(account_balance))

    """
    Simulate mining Bitcoins over 1 year,
    miner earns a share of reward proportional to their
    hashrate and total hashrate.
    """
    hashrate =  difficulty * 2**32 / 600
    total_rewards = reward * (6 * 24 * 365)
    proportion = (computer_power * 10**12) / hashrate
    account_bitcoins = total_rewards * proportion

    print("You mined {0} Bitcoins worth ${1}!".format(account_bitcoins, account_bitcoins * exchange_price))

    return account_balance, account_bitcoins, computer_power

def welcome_message():
    print("""

.______    __  .___________.  ______   ______    __  .__   __.
|   _  \  |  | |           | /      | /  __  \  |  | |  \ |  |
|  |_)  | |  | `---|  |----`|  ,----'|  |  |  | |  | |   \|  |
|   _  <  |  |     |  |     |  |     |  |  |  | |  | |  . `  |
|  |_)  | |  |     |  |     |  `----.|  `--'  | |  | |  |\   |
|______/  |__|     |__|      \______| \______/  |__| |__| \__|

.___  ___.  __  .__   __.  __  .__   __.   _______
|   \/   | |  | |  \ |  | |  | |  \ |  |  /  _____|
|  \  /  | |  | |   \|  | |  | |   \|  | |  |  __
|  |\/|  | |  | |  . `  | |  | |  . `  | |  | |_ |
|  |  |  | |  | |  |\   | |  | |  |\   | |  |__| |
|__|  |__| |__| |__| \__| |__| |__| \__|  \______|

  _______      ___      .___  ___.  _______
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__
|  | |_ |   /  /_\  \   |  |\/|  | |   __|
|  |__| |  /  _____  \  |  |  |  | |  |____
 \______| /__/     \__\ |__|  |__| |_______|


    """)

main()
