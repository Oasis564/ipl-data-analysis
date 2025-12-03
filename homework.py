import pandas as pd

# Read IPL data CSV
df = pd.read_csv("ipl_data.csv")

# Display first five rows
print("---- First 5 Records ----")
print(df.head())

# Highest total runs
highest_runs = df.loc[df['TotalRuns'].idxmax()]
print("\nHighest Run Scorer:")
print(highest_runs[['PLAYER', 'TotalRuns']])

# Highest batting average
highest_avg = df.loc[df['Avgerage'].replace("-", 0).astype(float).idxmax()]
print("\nHighest Batting Average:")
print(highest_avg[['PLAYER', 'Avgerage']])

# Player with most 100s
most_100s = df.loc[df['X100'].idxmax()]
print("\nMost 100s:")
print(most_100s[['PLAYER','X100']])

# Top 5 strike rates
df['StrikeRate'] = df['StrikeRate'].astype(float)
top_sr = df.sort_values(by='StrikeRate', ascending=False).head()
print("\nTop 5 Strike Rates:")
print(top_sr[['PLAYER','StrikeRate']])

# Filter batsmen with 400+ runs
top_batsmen = df[df['TotalRuns'] > 400][['PLAYER','TotalRuns','Avgerage']]
print("\nBatsmen with 400+ Runs:")
print(top_batsmen)

# Filter bowlers with 15+ wickets
df['Wkts'] = pd.to_numeric(df['Wkts'], errors='coerce').fillna(0)
top_bowlers = df[df['Wkts'] >= 15][['PLAYER','Wkts','Economy']]
print("\nBowlers with 15+ Wickets:")
print(top_bowlers)

def get_player_runs(name):
    player = df[df['PLAYER'].str.lower() == name.lower()]
    if len(player) == 0:
        return "Player not found in dataset."
    return int(player['TotalRuns'].values[0])

# Example:
print("Virat Kohli Total Runs:", get_player_runs("Virat Kohli"))

import pandas as pd

data = {
    "Year": ["Class 1", "Class 5", "Class 10", "Class 12"],
    "Math": [85, 92, 88, 90],
    "Science": [80, 89, 93, 87],
    "English": [90, 88, 85, 91]
}

df_marks = pd.DataFrame(data)
df_marks.to_csv("my_scores.csv", index=False)

print("CSV Saved!")

df = pd.read_csv("my_scores.csv")

print("---- Score Sheet ----")
print(df)

# Average score each year
df['Average'] = df[['Math','Science','English']].mean(axis=1)
print("\nYear-wise Average:")
print(df[['Year','Average']])

# Subject-wise average scores
subject_avg = df[['Math','Science','English']].mean()
print("\nSubject-wise Average:")
print(subject_avg)

# Highest score each year
print("\nHighest Score Each Year:")
print(df[['Year','Math','Science','English']].max(axis=1))

# Overall topper subject
top_subject = subject_avg.idxmax()
print("\nBest Performing Subject:", top_subject)
