from os import listdir
from os.path import isfile, join
import pandas as pd

FILES_FOLDER_PATH = './data/PepitoTheCat-140801102068195328(20111127_153613)-1004221040485158912(20180606_063848)-media'

'''
This function outputs a file with the following columns: tweet_date, img_name, label

There's a csv file with various info: tweets text and file name among them. I'll use that text to label
each image (if the text includes the word 'home', the image will be labeled as 'home', if the text includes
the word 'out', the image will be labeled as 'out').

Tweet dates are saved in case they are useful in the future.
'''
def auto_label_images(file_path='./data/labeled_images.csv'):
    _label_images(_find_csv_file()).to_csv(file_path, index = False)
    
def _label_images(csv_file_path):
    df = pd.read_csv(csv_file_path, usecols=['Tweet date', 'Saved filename', 'Tweet content'])

    homes = df[df['Tweet content'].str.contains('home')][['Tweet date', 'Saved filename', 'Tweet content']].assign(label = 'home')
    outs = df[df['Tweet content'].str.contains('out')][['Tweet date', 'Saved filename', 'Tweet content']].assign(label = 'out')

    df = pd.concat([homes[['Tweet date', 'Saved filename', 'label']], outs[['Tweet date', 'Saved filename', 'label']]])
    
    df.rename(columns={'Tweet date': 'tweet_date', 'Saved filename': 'img_name'}, inplace=True)

    return df

def _find_csv_file():
    return [join(FILES_FOLDER_PATH, f) for f in listdir(FILES_FOLDER_PATH) if isfile(join(FILES_FOLDER_PATH, f)) and f.endswith('.csv')][0]

if __name__ == '__main__':
    auto_label_images()