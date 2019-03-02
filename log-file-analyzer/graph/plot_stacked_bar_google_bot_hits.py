import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter

def main():
    plot_stacked_bar()

def plot_stacked_bar():
    # Get data file names
    site = ''
    site = input("Which site you'd like to plot? ".format(site))
    path = '..\data\\' + site + '\\' + site + '-combined-log.csv'

    google_bot_mobile = 'Mozilla/5.0+(Linux;+Android+6.0.1;+Nexus+5X+Build/MMB29P)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/41.0.2272.96+Mobile+Safari/537.36+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)'

    df = pd.read_csv(path, usecols=['Date', 'User_Agent', 'Response_Code'], index_col=0)

    df_google_mobile = df.loc[(df.User_Agent == google_bot_mobile) & (df.Response_Code == 200)]
    df_google_mobile = df_google_mobile.groupby(['Date']).size()

    df_google_desktop = df.loc[(df.User_Agent != google_bot_mobile) & (df.Response_Code == 200)]
    df_google_desktop = df_google_desktop.groupby(['Date']).size().sort_values()

    df = pd.concat([df_google_mobile, df_google_desktop], axis=1)

    df['Sum'] = df_google_mobile + df_google_desktop
    df['Hits from Google Bot Mobile'] = df_google_mobile / df['Sum']
    df['Hits from Google Bot Desktop'] = df_google_desktop / df['Sum']

    df = df.drop([0, 1, 'Sum'], axis=1)

    user_agent_legend_dict = {'Googlebot Mobile Hits': 'Green', 'Googlebot Desktop Hits': 'Purple'}
    user_agent_colors = user_agent_legend_dict.values()

    df.plot(kind='bar', stacked=True, title='Google Bot Hits Mobile VS. Desktop', color=user_agent_colors)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-Stacked-Bar-Google-Bot-Mobile-Hits.png', bbox_inches='tight')

if __name__ == '__main__': main()
