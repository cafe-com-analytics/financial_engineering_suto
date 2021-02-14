# https://www.udemy.com/course/ai-finance
import random
import pandas as pd
import os
from glob import glob


symbols = []

files = glob('data/raw/*.csv')

for f in files:
  df = pd.read_csv(f)
  symbol = f.split('/')[-1].split('.')[0]
  symbols.append(symbol)

small_symbols = {'MMM', 'ABT', 'ABBV', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES',
  'AFL', 'AKAM', 'IBM', 'GOOG', 'SBUX', 'AAPL', 'SPY'}

sample = random.sample(symbols, 100)

small_symbols = small_symbols | set(sample)

full_df = None
for symbol in small_symbols:
  f = f"data/raw/{symbol}.csv"
  if os.path.exists(f):
    df = pd.read_csv(f)
    df['Name'] = symbol
    if full_df is None:
      full_df = df
    else:
      full_df = full_df.append(df, ignore_index=True)

full_df.to_csv('data/interim/sp500sub.csv', index=False)

