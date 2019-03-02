import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Get data file names
site = ''
site = input("Which site you'd like to plot? ".format(site))
path = '..\data\\' + site + '\\' + site + '-combined-log.csv'

google_bot_mobile = 'Mozilla/5.0+(Linux;+Android+6.0.1;+Nexus+5X+Build/MMB29P)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/41.0.2272.96+Mobile+Safari/537.36+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)'

df = pd.read_csv(path, usecols=['Date', 'User_Agent', 'Response_Code', 'Requested_URI'], index_col=0)
df_google_mobile = df.loc[(df.User_Agent == google_bot_mobile) & (df.Response_Code == 200)]
ax_google_mobile = df_google_mobile.groupby(['Date', 'Requested_URI']).size().reset_index(name='count').unstack(level=1, fill_value=0)

plt.xlabel("Page", color='Black')
plt.ylabel("Number of GoogleBot Hits", color='Black')

user_agent_legend_dict = {'Googlebot Mobile Hits': 'Green', 'Googlebot Desktop Hits': 'Blue'}
user_agent_colors = user_agent_legend_dict.values()

patch_list_user_agent = []
for key in user_agent_legend_dict:
    data_key = mpatches.Patch(color=user_agent_legend_dict[key], label=key)
    patch_list_user_agent.append(data_key)

plt.legend(handles=patch_list_user_agent, loc='upper right')
plt.title("Googlebot Hits Mobile VS. Desktop", color='Black')

plt.bar(ax_google_mobile['Requested_URI'], ax_google_mobile['count'], color='Green')
plt.show()

# Save graph to PNG
plt.savefig('..\data\\' + site + '\\' + site + '-Google-Bot-Mobile-Hits.png', bbox_inches='tight')
