import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort


filename = "../data/befkbhalderstatkode.csv"

bef_stats_df = np.genfromtxt(filename, delimiter=",", dtype=np.uint, skip_header=1)

##print(type(bef_stats_df),' of size: ',bef_stats_df.size)
##print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])

neighb = {
    1: "Indre By",
    2: "Østerbro",
    3: "Nørrebro",
    4: "Vesterbro/Kgs. Enghave",
    5: "Valby",
    6: "Vanløse",
    7: "Brønshøj-Husum",
    8: "Bispebjerg",
    9: "Amager Øst",
    10: "Amager Vest",
    99: "Udenfor",
}

## Find out how many people lived in each of the 11 areas in 2015

newDict = {}

def getPubInCity():
    for n in neighb:
        mask = (bef_stats_df[:, 1] == n) & (bef_stats_df[:, 0] == 2015)
        sum = np.sum(bef_stats_df[mask][:, 4])
        print(neighb.get(n))
        print(sum)
        newDict.update({n: sum})


# 4. Make a bar plot to show the size of each city area from the smallest to the largest
def getBarWithPubInCity():
    sortedDict = {k: v for k, v in sorted(newDict.items(), key=lambda item: item[1])}
    for n in sortedDict:
        plt.bar([neighb.get(n)], [sortedDict.get(n)], width=0.5, align="center")
        plt.xticks(rotation=45, horizontalalignment="right", fontweight="light")


# 5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015


def peopleAbove65cph2015():
    mask = (
        (bef_stats_df[:, 0] == 2015)
        & (bef_stats_df[:, 2] > 65)
        & (bef_stats_df[:, 1] != 99)
    )
    print("sum all above 65 cph areas = ", np.sum(bef_stats_df[mask][:, 4]))


# 6. How many of those were from the other nordic countries (not dk)
def howManyNotFromDenmark():
    dd = bef_stats_df
    mask = (
        (bef_stats_df[:, 0] == 2015)
        & (bef_stats_df[:, 2] > 65)
        & (dd[:, 3] != 5100)
        & (dd[:, 3] != 5120)
        & (dd[:, 3] != 5110)
    )
    print(
        "sum all above 65 cph areas not from nordic countries = ",
        np.sum(bef_stats_df[mask][:, 4]),
    )


# 7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015


def linePlotting():
    years = list(np.unique(bef_stats_df[:, 0]))
    vesterbroDict = {}
    østerbroDict = {}
    for y in years:
        mask = (bef_stats_df[:, 0] == y) & (bef_stats_df[:, 1] == 4)
        sum = np.sum(bef_stats_df[mask][:, 4])
        vesterbroDict.update({y: sum})
    for y in years:
        mask = (bef_stats_df[:, 0] == y) & (bef_stats_df[:, 1] == 2)
        sum = np.sum(bef_stats_df[mask][:, 4])
        østerbroDict.update({y: sum})

    print(østerbroDict)
    values_vesterbro = list(vesterbroDict.values())
    values_østerbro = list(østerbroDict.values())
    plt.title("befolkningstal gennem årene", fontsize=24)
    plt.ylabel("Befolkningstal", fontsize=12)
    plt.ylabel("Årstal", fontsize=12)
    plt.plot(years, values_vesterbro, label="Vesterbro")
    plt.plot(years, values_østerbro, label="Østerbro")
    plt.legend()
    plt.show()