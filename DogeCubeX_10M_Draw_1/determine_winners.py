import random
import os
import numpy as np
import pandas as pd

winners_file = 'results/winners.csv'
last_trade_time = 1661763115788
prizes = ([250_000] * 7) + ([125_000] * 26) + ([75_000] * 67)
print("Total prizes: " + str(np.sum(prizes)))

random.seed(last_trade_time)
if os.path.exists(winners_file):
    os.remove(winners_file)
participants_df = pd.read_csv('results/participants.csv')

print(participants_df)


winners_df = pd.DataFrame({
    'User': [''] * len(prizes),
    'Prize': prizes
})
print(winners_df)

for idx, prize in enumerate(prizes):
    pool = participants_df['user'].repeat(participants_df['entries']).tolist()

    winner = random.choice(pool)
    print(winner)

    winners_df.iloc[idx, 0] = winner
    participants_df = participants_df[participants_df['user'] != winner]

unique_winners = len(winners_df['User'].unique())

print("Unique Winners: " + str(unique_winners))
assert unique_winners == len(prizes)



winners_df.to_csv(winners_file, index=False)

print("File saved")
