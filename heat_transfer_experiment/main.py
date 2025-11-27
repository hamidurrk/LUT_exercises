import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_BASE_DIR = "heat_transfer_experiment/data/"
data_files = [path for path in os.listdir(DATA_BASE_DIR) if path.endswith('.txt')]
all_file_paths = [os.path.join(DATA_BASE_DIR, file) for file in data_files]
# Time  T1 (°C)  T2 (°C)  T3 (°C)  T4 (°C)  del_T  v (m/s)  P (W)  alpha (W/m²K)  Nu ()  q (W/m²)  Re ()

t1_col = 'T1 (°C)'
t4_col = 'T4 (°C)'
p_col = 'P (W)'
del_t_col = 'del_T'
q_col = 'q (W/m²)'
alpha_col = 'alpha (W/m²K)'
nu_col = 'Nu ()'
re_col = 'Re ()'

def read_file(file_path):
    df = pd.read_csv(file_path, sep='\t', skiprows=3, encoding='cp1252')
    return df

def filter_by_most_frequent(df, column):
    counts = df[column].value_counts()
    max_count = counts.max()
    most_frequent_values = counts[counts == max_count].index
    return df[df[column].isin(most_frequent_values)]

def load_data():
    data_main = {}
    data_filtered = {}

    for file_path in all_file_paths:
        df = read_file(file_path)
        # print(f"Data from {file_path}:")
        # print(df.head())
        
        df.insert(df.columns.get_loc(t4_col) + 1, 'del_T', df[t4_col] - df[t1_col])
        # print("Data with del_T column:")
        # print(df.head())

        data_file_name = file_path.split('/')[-1].replace('.txt', '').replace(' ', '_').lower()

        data_main[data_file_name] = df

        df = filter_by_most_frequent(df, t4_col)
        # print("Filtered Data (most frequent T4 (°C)):")
        # print(df.head())

        data_filtered[data_file_name] = df
    return data_main, data_filtered

def plot_from_dict(data_df_dict, col_x, col_y):
    plt.figure(figsize=(10, 6))
    for label, df in data_df_dict.items():
        print(df.shape)
        label=label.replace('_', ' ').title()
        plt.plot(df[col_x], df[col_y], marker='o', linestyle='', label=label)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f"{col_y} vs {col_x} for all experiments")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

def plot_nu_vs_re(data_df_dict):
    pass

def main():
    data_main, data_filtered = load_data()
    # plot_from_dict(data_main, p_col, t4_col)
    # plot_from_dict(data_main, p_col, 'del_T')
    # plot_from_dict(data_main, p_col, q_col)
    # plot_from_dict(data_filtered, p_col, alpha_col)
    # plot_from_dict(data_main, del_t_col, nu_col)
    # plot_from_dict(data_main, re_col, nu_col)

if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)
    main()
    plt.show()