import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os

DATA_BASE_DIR = "heat_transfer_experiment/data/"
data_files = [path for path in os.listdir(DATA_BASE_DIR) if path.endswith('.txt')]
all_file_paths = [os.path.join(DATA_BASE_DIR, file) for file in data_files]
# Time  T1 (°C)  T2 (°C)  T3 (°C)  T4 (°C)  del_T  v (m/s)  P (W)  alpha (W/m²K)  Nu ()  q (W/m²)  Re ()

t1_col = 'T1 (°C)'
t4_col = 'T4 (°C)'
p_col = 'P (W)'
del_t_col = 'del_T'
alpha_col = 'alpha (W/m²K)'
q_col = 'q (W/m²)'
r_col = 'R_th'
nu_col = 'Nu ()'
re_col = 'Re ()'

name_dict = {
    'T1 (°C)': 'Ambient Temperature (°C)',
    'T4 (°C)': 'Plate Temperature (°C)',
    'P (W)': 'Power (W)',
    'del_T': 'Temperature Difference (°C)',
    'alpha (W/m²K)': 'Heat Transfer Coefficient (W/m²K)',
    'q (W/m²)': 'Heat Flux (W/m²)',
    'R_th': 'Thermal Resistance (K/W)',
    'Nu ()': 'Nusselt Number',
    'Re ()': 'Reynolds Number'
}

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

        df.insert(df.columns.get_loc(q_col) + 1, 'R_th', (df[t4_col] - df[t1_col]) / df[q_col])

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
        label=label.replace('_', ' ').title()
        plt.plot(df[col_x], df[col_y], marker='o', linestyle='', label=label)
    plt.xlabel(name_dict.get(col_x, col_x))
    plt.ylabel(name_dict.get(col_y, col_y))
    plt.title(f"{name_dict.get(col_y, col_y)} vs {name_dict.get(col_x, col_x)} for all experiments")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

def plot_nu_vs_re(data_df_dict):
    for label, df in data_df_dict.items():
        if 'forced' in label:
            re_forced = np.array(df[re_col])
            nu_forced = np.array(df[nu_col])

            coeffs = np.polyfit(np.log(re_forced), np.log(nu_forced), 1)
            m, c = coeffs
            re_fit = np.linspace(min(re_forced), max(re_forced), 100)
            nu_fit = np.exp(c) * re_fit**m
            plt.loglog(re_forced, nu_forced, 'o', label=f'{label} data')
            plt.loglog(re_fit, nu_fit, '-', label=f'{label} fit: Nu = {np.exp(c):.3f} * Re^{m:.3f}')
    plt.xlabel('Re ()')
    plt.ylabel('Nu ()')
    plt.title('Nusselt Number vs Reynolds Number for Free and Forced Convection')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

def plot_comparison_bar_chart(data_df_dict):
    categories = ['alpha (W/m²K)', 'Nu ()', 'q (W/m²)']
    free_vals_list = []
    forced_vals_list = []

    for col in categories:
        free_vals = []
        forced_vals = []
        for label, df in data_df_dict.items():
            if 'free' in label:
                free_vals.append(df[col].mean())
            elif 'forced' in label:
                forced_vals.append(df[col].mean())
        free_vals_list.append(free_vals)
        forced_vals_list.append(forced_vals)

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    free_bars = []
    forced_bars = []
    for i, (free_vals, forced_vals) in enumerate(zip(free_vals_list, forced_vals_list)):
        for j, val in enumerate(free_vals):
            bar = ax.bar(
                x[i] - width/2 + (j * width / max(1, len(free_vals))),
                val,
                width / max(1, len(free_vals)),
                color='tab:blue',
                alpha=0.7,
                edgecolor='black',
                label='Free Convection' if i == 0 and j == 0 else ""
            )
            if i == 0 and j == 0:
                free_bars.append(bar)
        for j, val in enumerate(forced_vals):
            bar = ax.bar(
                x[i] + width/2 + (j * width / max(1, len(forced_vals))),
                val,
                width / max(1, len(forced_vals)),
                color='tab:orange',
                alpha=0.7,
                edgecolor='black',
                label='Forced Convection' if i == 0 and j == 0 else ""
            )
            if i == 0 and j == 0:
                forced_bars.append(bar)

        if free_vals:
            ax.hlines(np.mean(free_vals), x[i] - width/2, x[i], colors='blue', linestyles='dashed', label='Free Mean' if i == 0 else "")
        if forced_vals:
            ax.hlines(np.mean(forced_vals), x[i], x[i] + width/2, colors='orange', linestyles='dashed', label='Forced Mean' if i == 0 else "")

    ax.set_xlabel('Parameter')
    ax.set_ylabel('Mean Value')
    ax.set_title('Comparison of Free vs Forced Convection')
    ax.set_xticks(x)
    ax.set_xticklabels(['alpha', 'Nu', 'q'])

    handles, labels = ax.get_legend_handles_labels()
    custom_handles = [
        Patch(facecolor='tab:blue', edgecolor='black', label='Free Convection'),
        Patch(facecolor='tab:orange', edgecolor='black', label='Forced Convection'),
        plt.Line2D([0], [0], color='blue', linestyle='dashed', label='Free Mean'),
        plt.Line2D([0], [0], color='orange', linestyle='dashed', label='Forced Mean'),
    ]
    ax.legend(handles=custom_handles)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

def main():
    data_main, data_filtered = load_data()
    plot_from_dict(data_main, p_col, t4_col)
    plot_from_dict(data_main, p_col, del_t_col)
    plot_from_dict(data_main, p_col, q_col)
    plot_from_dict(data_filtered, p_col, alpha_col)
    plot_from_dict(data_main, del_t_col, nu_col)
    plot_from_dict(data_main, re_col, nu_col)
    plot_from_dict(data_main, del_t_col, r_col)
    plot_comparison_bar_chart(data_main)
    # plot_nu_vs_re(data_main)

if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 0)
    pd.set_option('display.max_colwidth', None)
    main()
    plt.show()