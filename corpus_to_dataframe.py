import os
import pandas as pd

from tqdm import tqdm

DIR_DATA = './data/raw'


def main():
    list_results = []
    for target in tqdm(os.listdir(DIR_DATA)):
        for text in os.listdir(f'{DIR_DATA}/{target}'):
            with open(f'{DIR_DATA}/{target}/{text}', 'r') as f:
                list_results.append({'target': target, 'text': f.read()})

    df_result = pd.DataFrame(list_results)
    df_result.to_csv('20newsgroup_raw.csv', sep=';', index=False)


if __name__ == '__main__':
    main()
