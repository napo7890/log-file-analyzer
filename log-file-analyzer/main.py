import pandas as pd
import glob
import os

# Convert titles
data_column_names = ['Date', 'Time', 's-ip', 'Request_Type', 'Requested_URI', 'Requested_Query_String', 'Port',
         'cs-username', 'Requesting_IP', 'Method', 'User_Agent', 'cs_Cookie', 'Requesting_URL', 'Host',
         'Response_Code', 'cs_Sub_Status', 'Response_Time1', 'Response_Time2', 'Time_Taken', '']

# Filter columns
filter_columns = ['Date', 'Time', 'Requested_URI', 'Requested_Query_String', 'Requesting_IP',
            'User_Agent', 'Requesting_URL', 'Host', 'Response_Code', 'Response_Time1', 'Response_Time2']

user_agent_list = (
    'Mozilla/5.0+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)',
    'Mozilla/5.0+AppleWebKit/537.36+(KHTML,+like+Gecko;+compatible;+Googlebot/2.1;++http://www.google.com/bot.html)+Safari/537.36',
    'Googlebot/2.1+(+http://www.google.com/bot.html)',
    'Mozilla/5.0+(Linux;+Android+6.0.1;+Nexus+5X+Build/MMB29P)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/41.0.2272.96+Mobile+Safari/537.36+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)'
)

site = ''
site = input("Which site you'd like to analyze? ".format(site))

def main():
    file_names = get_file_names(site)
    read_file(file_names)


def get_file_names(site_name):
    # Get file names
    path = 'source_files\\' + site_name
    wildcard_pattern = "*"

    root_dir = os.path.join(path, wildcard_pattern)
    file_names = glob.glob(root_dir)
    return file_names

def read_file(file_name):
    for file in file_name:
        df = pd.read_csv(file, delim_whitespace=True, names=data_column_names, usecols=filter_columns, header=0, index_col=0)
        df.index = pd.to_datetime(df.index, errors='coerce')

        print(file)
        print("Number of rows on file #{0} before filtering is: {1}".format(file_name.index(file), df.shape[0]))

        df = df[['.' not in x for x in df.Requested_URI]]
        df = df[['66.249.' in x for x in df.Requesting_IP]]

        # Filter Googlebot hits
        df = df.loc[(
             (df['User_Agent'] == user_agent_list[0]) |
             (df['User_Agent'] == user_agent_list[1]) |
             (df['User_Agent'] == user_agent_list[2]) |
             (df['User_Agent'] == user_agent_list[3])
             )]

        print("Number of rows on file #{0} after filtering is: {1}".format(file_name.index(file), df.shape[0]))

        write_file(df, file_name, file)

        '''
        first_row_check = df.iloc[0][0]
        if first_row_check == 'date':
            print(file)
            print("Number of rows on file #{0} before filtering is: {1}".format(file_name.index(file), df.shape[0]))

            df = df[['.' not in x for x in df.Requested_URI]]
            df = df[['66.249.' in x for x in df.Requesting_IP]]

            # Filter Googlebot hits
            df = df.loc[(
                (df['User_Agent'] == user_agent_list[0]) |
                (df['User_Agent'] == user_agent_list[1]) |
                (df['User_Agent'] == user_agent_list[2]) |
                (df['User_Agent'] == user_agent_list[3])
                )]

            print("Number of rows on file #{0} after filtering is: {1}".format(file_name.index(file), df.shape[0]))

            write_file(df, file_name, file)

        else:
            print('bad file ' + file)
            df.to_csv('data/' + site + '/' + site + '-broken-files.csv', mode='a', header=False)
            continue
        '''
def write_file(df, file_name, file):
    '''
    date_min_day = str(df.index.min().day)
    date_min_month = str(df.index.min().month)
    date_min_year = str(df.index.min().year)
    date_min = date_min_day + '_' + date_min_month + '_' + date_min_year

    date_max_day = str(df.index.max().day)
    date_max_month = str(df.index.max().month)
    date_max_year = str(df.index.max().year)
    date_max = date_max_day + '_' + date_max_month + '_' + date_max_year

    df_200 = df.loc[(df['Response_Code'] == 200)]
    df_301 = df.loc[(df['Response_Code'] == 301)]
    df_302 = df.loc[(df['Response_Code'] == 302)]
    df_404 = df.loc[(df['Response_Code'] == 404)]
    df_503 = df.loc[(df['Response_Code'] == 503)]
    '''
    if file_name.index(file) == 0:
        df.to_csv('data/' + site + '/' + '-test' + site + '-combined-log.csv', mode='a', header=True)
        # df.to_csv('data/' + site + '/' + date_min + '-' + date_max + '-' + site + '-combined-log.csv', mode='a', header=True)
        '''
        with pd.ExcelWriter(
                'data/' + site + '/' + date_min + '-' + date_max + '-' + site + '-combined-log.xlsx') as writer:
            df.to_excel(writer, header=True, sheet_name='Row Data')
            df_200.to_excel(writer, header=True, sheet_name='200 OK Pages')
            df_301.to_excel(writer, header=True, sheet_name='301 Pages')
            df_302.to_excel(writer, header=True, sheet_name='302 Pages')
            df_404.to_excel(writer, header=True, sheet_name='404 Pages')
            df_503.to_excel(writer, header=True, sheet_name='503 Pages')
        '''
    else:
        df.to_csv('data/' + site + '/' + site + '-combined-log.csv', mode='a', header=False)
        # df.to_excel('data/' + site + '/' + site + '-combined-log.xlsx', header=False)

    # return date_min, date_max

if __name__ == '__main__': main()

