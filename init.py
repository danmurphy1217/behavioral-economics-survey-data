import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib

df = pd.DataFrame(pd.read_csv('Post-Grad Jobs and The Coronavirus.csv'))

print(df.columns)
print(np.mean(list(dict(pd.value_counts(df.jobConcernLevel)).keys())))

fig, ((ax1, ax2) , (ax3, ax4)) = plt.subplots(2, 2, figsize= (12, 10))

sns.set_palette('deep')
fig1 = sns.barplot(data = df, x = ["Yes", "No"], y = [5, 4], ax = ax1)
ax1.set_title("Has Your Job Notified You Yet? (Y/N)")
ax1.set_ylabel("Frequency")
ax1.set_xlabel("Response")
fig2 = sns.barplot(x = list(dict(pd.value_counts(df.effectOnImmediateFamily)).keys()), y = list(dict(pd.value_counts(df.effectOnImmediateFamily)).values()), ax = ax2)
ax2.set_title("How Concerned Are You About Infecting Family? (1 - 10)")
ax2.set_ylabel("Frequency")
ax2.set_xlabel("Response (rated 1 - 10)")
fig3 = sns.barplot(x = list(dict(pd.value_counts(df.healthConcernLevel)).keys()), y = list(dict(pd.value_counts(df.healthConcernLevel)).values()), ax = ax3)
ax3.set_title("How Concerned Are You About Your Health? (1 - 10)")
ax3.set_ylabel("Frequency")
ax3.set_xlabel("Response (rated 1 - 10)")
fig4 = sns.barplot(x = list(dict(pd.value_counts(df.jobConcernLevel)).keys()), y = list(dict(pd.value_counts(df.jobConcernLevel)).values()),  ax= ax4)
ax4.set_title("How Concerned Are You About Your Job Security? (1 - 10)")
ax4.set_ylabel("Frequency")
ax4.set_xlabel("Response (rated 1 - 10)")
plt.savefig("subplots")



df_text = df.highestConcern.str.split(';', expand =True)
[pd.value_counts(df_text[i]) for i in [0, 1, 2, 3, 4]]

response_choices =["losing my job offer", "advancing my career", "safe work environment", "non-job related concerns", "graduate school requirements", "job performance"]
value_counts = [4, 7, 3, 3, 1, 2]

font =  {'size':11}
matplotlib.rc('font', **font)
fig, ax = plt.subplots(1, 1, figsize = (22, 10))
sns.set_palette('dark')
fig1 = sns.barplot(x = value_counts, y = response_choices, ax= ax)
ax.set_title("What is your Highest Concern regarding the Coronavirus?")
ax.set_ylabel("Survey Responses")
ax.set_xlabel("Frequency of Response")
plt.savefig("text-responses")