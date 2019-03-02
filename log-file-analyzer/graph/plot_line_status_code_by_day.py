import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Get data file names
site = ''
site = input("Which site you'd like to plot? ".format(site))
path = '..\data\\' + site + '\\' + site + '-combined-log.csv'

response = ''
response = input("Which response code you'd like to plot?\n200 | 301 | 302 | 304 | 400 | 404 | 503  | ALL ".format(response))

df = pd.read_csv(path, usecols=['Date', 'Response_Code'], index_col=0)

plt.xlabel("Date", color='Black')
plt.ylabel("Number of Hits", color='Black')

response_code_legend_dict = {'200': 'Green', '301': 'Purple', '302': 'Blue', '304': 'Gray', '400': 'Yellow', '404': 'Red', '503': 'Brown'}
response_code_colors = response_code_legend_dict.values()

patch_list_response_code = []
for key in response_code_legend_dict:
    data_key = mpatches.Patch(color=response_code_legend_dict[key], label=key)
    patch_list_response_code.append(data_key)

plt.legend(handles=patch_list_response_code, loc='upper right')
plt.title("Daily Hits By Response Code", color='Black')

if response == '200':
    df_response_code_200 = df.loc[(df.Response_Code == 200)]
    ax_200 = df_response_code_200.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_200['Date'], ax_200['count'], marker='o', color='Green')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-200-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '301':
    df_response_code_301 = df.loc[(df['Response_Code'] == 301)]
    ax_301 = df_response_code_301.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_301['Date'], ax_301['count'], marker='o', color='Purple')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-301-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '302':
    df_response_code_302 = df.loc[(df['Response_Code'] == 302)]
    ax_302 = df_response_code_302.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_302['Date'], ax_302['count'], marker='o', color='Blue')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-302-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '304':
    df_response_code_304 = df.loc[(df['Response_Code'] == 304)]
    ax_304 = df_response_code_304.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_304['Date'], ax_304['count'], marker='o', color='Gray')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-304-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '400':
    df_response_code_400 = df.loc[(df['Response_Code'] == 400)]
    ax_400 = df_response_code_400.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_400['Date'], ax_400['count'], marker='o', color='Yellow')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-400-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '404':
    df_response_code_404 = df.loc[(df['Response_Code'] == 404)]
    ax_404 = df_response_code_404.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_404['Date'], ax_404['count'], marker='o', color='Red')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-404-Hits.png', bbox_inches='tight')

    plt.show()

elif response == '503':
    df_response_code_503 = df.loc[(df['Response_Code'] == 503)]
    ax_503 = df_response_code_503.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_503['Date'], ax_503['count'], marker='o', color='Brown')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-503-Hits.png', bbox_inches='tight')

    plt.show()

elif response == 'ALL':
    df_response_code_200 = df.loc[(df['Response_Code'] == 200)]
    ax_200 = df_response_code_200.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_301 = df.loc[(df['Response_Code'] == 301)]
    ax_301 = df_response_code_301.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_302 = df.loc[(df['Response_Code'] == 302)]
    ax_302 = df_response_code_302.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_304 = df.loc[(df['Response_Code'] == 304)]
    ax_304 = df_response_code_304.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_400 = df.loc[(df['Response_Code'] == 400)]
    ax_400 = df_response_code_400.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_404 = df.loc[(df['Response_Code'] == 404)]
    ax_404 = df_response_code_404.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    df_response_code_503 = df.loc[(df['Response_Code'] == 503)]
    ax_503 = df_response_code_503.groupby(['Date', 'Response_Code']).size().reset_index(name='count').unstack(level=1, fill_value=0)

    plt.plot(ax_200['Date'], ax_200['count'], marker='o', color='Green')
    plt.plot(ax_301['Date'], ax_301['count'], marker='o', color='Purple')
    plt.plot(ax_302['Date'], ax_302['count'], marker='o', color='Blue')
    plt.plot(ax_304['Date'], ax_304['count'], marker='o', color='Gray')
    plt.plot(ax_400['Date'], ax_400['count'], marker='o', color='Yellow')
    plt.plot(ax_404['Date'], ax_404['count'], marker='o', color='Red')
    plt.plot(ax_503['Date'], ax_503['count'], marker='o', color='Brown')

    # Save graph to PNG
    plt.savefig('..\data\\' + site + '\\' + site + '-Google-Bot-Mobile-Hits.png', bbox_inches='tight')

    plt.show()

else:
    print('Error')







