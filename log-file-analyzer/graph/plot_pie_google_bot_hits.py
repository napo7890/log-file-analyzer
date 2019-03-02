import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Get data file names
site = ''
site = input("Which site you'd like to plot? ".format(site))
path = '..\data\\' + site + '\\' + site + '-combined-log.csv'

df = pd.read_csv(path)

user_agent = list(df.User_Agent.unique())

sty_user_agent = {}
for i in user_agent:
    x = len(df[df.User_Agent == i])
    sty_user_agent.update({i: x})
print(sty_user_agent)
user_agent_values = sty_user_agent.values()

user_agent_legend_dict = {'Googlebot Mobile Hits': 'Green', 'Googlebot Desktop Hits': 'Purple'}
user_agent_colors = user_agent_legend_dict.values()

patch_list_user_agent = []
for key in user_agent_legend_dict:
    data_key = mpatches.Patch(color=user_agent_legend_dict[key], label=key)
    patch_list_user_agent.append(data_key)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v}'.format(v=val)
    return my_autopct

plt.pie(user_agent_values, colors=user_agent_colors, startangle=90, radius=0.4, center=(0.2, 0.2),
        pctdistance=0.7, autopct=make_autopct(user_agent_values), labels=sty_user_agent)

plt.legend(title='Googlebot Hits Mobile VS. Desktop', handles=patch_list_user_agent, loc='upper left')
plt.title("Googlebot Hits Mobile VS. Desktop", color='Black')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

# Save graph to PNG
plt.savefig('..\data\\' + site + '\\' + site + '-Google-Bot-Hits-Pie.png', bbox_inches='tight')

plt.show()
