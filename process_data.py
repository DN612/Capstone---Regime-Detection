import pandas as pd
import os

def data_process(filename, file_to_path):
    """
    :param filename: xlsx file name
    :param file_to_path: the path for csv file to be stored
    :return:
    """
    s_file = pd.read_excel(filename)
    ind = s_file.Security[s_file.Security=='Date'].index[0]
    s_file = s_file.loc[ind+1::]
    s_file.rename(columns = {s_file.columns[0]:'Date'}, inplace=True)
    s_file.rename(columns =  {s_file.columns[1]:s_file.columns[1].rstrip()}, inplace=True)
    s_file.to_csv(file_to_path, index=False)

# s_file = pd.read_excel('Data/Bloomberg Barclays Euro Aggregate Corporate.xlsx')
# ind = s_file.Security[s_file.Security=='Date'].index[0]
# s_file.columns = ['Date', s_file.columns[1].rstrip()]
# s_file = s_file.loc[ind+1::]
# s_file.to_csv('Data_csv2/AUD.csv')
def process_folder(source_folder='Data', target_folder='Data_csv2'):
    """
    :param source_folder: the folder where the xlsx file is from
    :param target_folder: the folder where the csv file to be stored
    :return:
    """
    for file in os.listdir(source_folder):
        print(file)
        filename = source_folder + '/' + file
        file_to_path = target_folder +'/' + file[0:-5] + '.csv'
        data_process(filename, file_to_path)

process_folder()
# for file in os.listdir('Data'):
#     filename = 'Data/'+file
#     file_to_path = 'Data_csv2/' + file[0:-5] + '.csv'
#     data_process(filename, file_to_path)


