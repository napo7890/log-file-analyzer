import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Get data file names
site = ''
site = input("Which site you'd like to plot? ".format(site))
path = '..\data\\' + site + '\\' + site + '-combined-log.csv'

df = pd.read_csv(path)

response_code = list(df.Response_Code.unique())

sty_response_code = {}
for i in response_code:
    x = len(df[df.Response_Code == i])
    sty_response_code.update({i: x})

print(sty_response_code)
response_code_values = sty_response_code.values()

response_code_legend_dict = {'200': 'Green', '302': 'Purple', '301': 'Blue', '404': 'Red', '500': 'Brown'}
response_code_colors = response_code_legend_dict.values()

patch_list = []
for key in response_code_legend_dict:
    data_key = mpatches.Patch(color=response_code_legend_dict[key], label=key)
    patch_list.append(data_key)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v}'.format(v=val)
    return my_autopct

plt.pie(response_code_values, colors=response_code_colors, startangle=90, radius=0.4, center=(0.2, 0.2),
        pctdistance=0.7, autopct=make_autopct(response_code_values), labels=sty_response_code)

plt.legend(title='Response Code', handles=patch_list, loc='upper left')
plt.title("Log File - Response Code", color='Black')

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

# Save graph to PNG
plt.savefig('..\data\\' + site + '\\' + site + '-Google-Bot-Response-Code.png', bbox_inches='tight')

plt.show()
