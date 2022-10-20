import pandas as pd
import matplotlib.pyplot as plt

cinema = pd.read_csv('cinema.csv')

cinema_df = pd.DataFrame(cinema)

print(cinema_df)

print("\nOLD COLUMNS\n\n")
for col in cinema_df.columns:
    print(col)

cinema_df_new = cinema_df[['budget', 'Gross']] / 1000000

cinema_df_new.rename(columns={'budget': 'budget(Million $)',
                              'Gross': 'gross(Million $)'}, inplace=True)

print("\nNEW COLUMNS\n\n")
for col in cinema_df_new.columns:
    print(col)

cinema_df_new['profit'] = cinema_df_new['gross(Million $)'] - \
    cinema_df_new['budget(Million $)']

print("\nTABLE WITH PROFIT\n\n")
print(cinema_df_new)

cinema_by_profit = cinema_df_new.sort_values(by=['profit'], ascending=False)

print("\nSORTED BY PROFIT\n\n")
print(cinema_by_profit)


cinema_first_10 = cinema_by_profit.head(10)

print("\nFIRST 10\n\n")
print(cinema_first_10)

ax1 = cinema_first_10.plot.scatter(x='budget(Million $)',
                                   y='profit', c='DarkBlue')

neg_profit = cinema_by_profit[cinema_by_profit['profit'] < 0]

print("\nNEGATIVE PROFIT\n\n")
print(neg_profit)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax2 = plt.subplots()

cinema_df['genre_1'].value_counts().plot(
    ax=ax2, kind='bar', xlabel='genre', ylabel='frequency')

plt.show()
