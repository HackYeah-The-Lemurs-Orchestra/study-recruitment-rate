import tabula
import matplotlib.pyplot as plt

important_columns_strategy_1 = [
    "Unnamed: 0",
    "I tura"
]

important_columns_strategy_2 = [
    "Kierunek studiów",
    "I tura"
]

file_names = {
    "2019.pdf": important_columns_strategy_1,
    "2020.pdf": important_columns_strategy_1,
    "2021.pdf": important_columns_strategy_1,
    "2022.pdf": important_columns_strategy_2
}

data = [[tabula.read_pdf(file_name, pages="1")[0].loc[:, strategy], strategy] for file_name, strategy in file_names.items()]

subjects = set()

for item in data:
    data_frame = item[0]
    important_columns = item[1]
    for index, row in data_frame.iterrows():
        subjects.add(row[important_columns[0]])

chart_data = {subject: [] for subject in subjects}

for subject in subjects:
    for item in data:
        data_frame = item[0]
        important_columns = item[1]
        selected_row = data_frame.loc[data_frame[important_columns[0]] == subject]
        if not selected_row.empty:
            chart_data[subject].append(float(selected_row[important_columns[1]].iloc[0].replace(",", ".")))


def all_years_data_is_available(pair):
    return len(pair[1]) == 4


chart_data = dict(filter(all_years_data_is_available, chart_data.items()))
for i in chart_data.keys():
    print(i)

for subject, points in chart_data.items():
    if len(points)==4:
        plt.plot([2019, 2020, 2021, 2022], points, label=subject)


plt.legend()
plt.show()

