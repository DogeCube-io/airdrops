import numpy as np
import pandas as pd
import os

stake_requirement = 100
participants_file = 'results/participants.csv'

if os.path.exists(participants_file):
    os.remove(participants_file)

swappers_df = pd.read_csv('swappers.csv')
stakers_df = pd.read_csv('stakers.csv')

merged_df = swappers_df.merge(stakers_df, how='inner', left_on=['user'], right_on=['address'])

merged_df = merged_df[merged_df.total_staked >= stake_requirement]

merged_df.drop('total_staked', axis=1, inplace=True)
merged_df.drop('address', axis=1, inplace=True)
merged_df.drop('swaps', axis=1, inplace=True)

merged_df['entries'] = merged_df['XRD_Volume'].div(5000)\
    .apply(np.floor).add(1)\
    .apply(lambda x: 5 if x > 5 else x)\
    .astype(np.int8)

print("Total Participants: " + str(merged_df.shape[0]))
print("Total Entries: " + str(merged_df['entries'].sum()))

merged_df.drop('XRD_Volume', axis=1, inplace=True)
merged_df.to_csv(participants_file, index=False)

print("File saved")
