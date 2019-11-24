# Bitcoin Mining Game
Simple Bitcoin mining game designed to model the decision to invest in computer power or hold Bitcoin.

# Rules
This is a single player game where you compete to earn the highest score possible. The game plays out over 10 rounds.
1. You start of with $1000 in your bank account
2. At the start of round 1, you decided how much of your money to spend on computer power. Computer power is purchases as cloud mining contracts and is in units of TH/$
3. At the end of the first round, you find out how much Bitcoins you've earned.
4. At the start of round n, you decided how many Bitcoins to sell and how much computer power to purchase before the round starts.
5. At the end of the round, you find out how many Bitcoins you've earned and what the current exchange price of Bitcoin is.
6. At the end of round 10, all the bitcoins you have are sold and a final score is calcualted based on the amount of US dollars you have in your bank account.

# Assumptions
1. The difficulty, exchange price of Bitcoin, and cost of computer power is exogenous and your actions in the game have no impact on their values.
