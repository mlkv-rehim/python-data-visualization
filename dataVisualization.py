import pandas as pd
import matplotlib.pyplot as plt

openness_data = {
    "Category": ["Currently Using", "Interested", "Not Interested"],
    "Percentage": [45, 35, 20]
}
df_openness = pd.DataFrame(openness_data)

fig = plt.figure(1)
fig.canvas.manager.set_window_title("Figure 1 – User Openness to Mental Health Applications")
plt.bar(df_openness["Category"], df_openness["Percentage"], color=["#4CAF50", "#2196F3", "#FFC107"])
plt.title("User Openness to Mental Health Applications")
plt.ylabel("Percentage (%)")
plt.xlabel("User Group")
plt.show()

barriers_data = {
    "Barrier": ["Privacy Concerns", "Lack of Effectiveness", "High Cost", "Prefer Face-to-Face"],
    "Percentage": [30, 25, 20, 25]
}
df_barriers = pd.DataFrame(barriers_data)

fig = plt.figure(2)
fig.canvas.manager.set_window_title("Figure 2 – Barriers to Mental Health App Adoption")
plt.pie(
    df_barriers["Percentage"],
    labels=df_barriers["Barrier"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#FF7043", "#29B6F6", "#66BB6A", "#AB47BC"]
)
plt.title("Barriers to Mental Health App Adoption")
plt.show()

features_data = {
    "Feature": [
        "Personalized Recommendations",
        "AI Chat Support",
        "Mood Tracking",
        "Journaling",
        "Community Support"
    ],
    "Preference (%)": [40, 30, 20, 25, 15]
}
df_features = pd.DataFrame(features_data)

fig = plt.figure(3)
fig.canvas.manager.set_window_title("Figure 3 – Desired Features in Mental Health Applications")
plt.bar(
    df_features["Feature"],
    df_features["Preference (%)"],
    color=["#3F51B5", "#009688", "#FF9800", "#9C27B0", "#795548"]
)
plt.title("Most Desired Features in Mental Health Applications")
plt.ylabel("User Preference (%)")
plt.xticks(rotation=30, ha="right")
plt.show()

gender_trends = {
    "Year": [2020, 2021, 2022, 2023],
    "Female Users (%)": [55, 58, 60, 62],
    "Male Users (%)": [45, 42, 40, 38]
}
df_gender = pd.DataFrame(gender_trends)

fig = plt.figure(4)
fig.canvas.manager.set_window_title("Figure 4 – Gender-Based Mental Health App Usage Trends")
plt.plot(df_gender["Year"], df_gender["Female Users (%)"], label="Female Users (%)", color="#E91E63")
plt.plot(df_gender["Year"], df_gender["Male Users (%)"], label="Male Users (%)", color="#2196F3")
plt.title("Gender-Based Mental Health App Usage Trends")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend()
plt.show()

market_growth = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Market Size (Billion USD)": [3.7, 4.2, 5.1, 6.0, 6.8]
}
df_market = pd.DataFrame(market_growth)

fig = plt.figure(5)
fig.canvas.manager.set_window_title("Figure 5 – Global Mental Health App Market Growth")
plt.plot(df_market["Year"], df_market["Market Size (Billion USD)"], color="#2E7D32")
plt.title("Global Mental Health App Market Growth")
plt.xlabel("Year")
plt.ylabel("Market Size (Billion USD)")
plt.show()

