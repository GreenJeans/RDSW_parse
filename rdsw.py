import re
from tkinter.filedialog import askopenfilename


def main():
    # define a store for the list of parsed results from RDSW
    database = []
    # open the file (prompt for location)
    filename = askopenfilename()
    file = open(filename)
    # read the file, parse lines into usable chunks
    for line in file.readlines():
        raw_data = re.split(
            'ENCOUNTER: | eID: | Time: | Player: |Difficulty: |raidSize: |Outcome: | INT: | MST: | HST: | CRT: | VRS: | ", --',
            line)
        # only parse successful kills, because it just seems right
        if len(raw_data) > 5 and "KILL" in raw_data[7]:
            data = {"Encounter": raw_data[1], "INT": float(raw_data[8]), "MST": float(raw_data[9]),
                    "HST": float(raw_data[10]), "CRT": float(raw_data[11]), "VRS": float(raw_data[12])}
            database.append(data)

    # give the average over all entries:
    # crt = 0
    # hst = 0
    # int = 0
    # mst = 0
    # vrs = 0
    # for entry in database:
    #     crt += entry["CRT"]
    #     hst += entry["HST"]
    #     int += entry["INT"]
    #     mst += entry["MST"]
    #     vrs += entry["VRS"]
    # print(
    #     '( Pawn: v1: "Resto-RDSW_all": CritRating={}, MasteryRating={}, HasteRating={}, Intellect={}, Versatility={} )'
    #         .format(round(crt / len(database), 2), round(mst / len(database), 2), round(hst / len(database), 2), round(int / len(database), 2), round(vrs / len(database), 2)))

    # give the average over the last 10
    crt = 0
    hst = 0
    int = 0
    mst = 0
    vrs = 0
    for entry in database:
        if database.index(entry) > len(database) - 11:
            crt += entry["CRT"]
            hst += entry["HST"]
            int += entry["INT"]
            mst += entry["MST"]
            vrs += entry["VRS"]
    print(
        '( Pawn: v1: "Resto-RDSW_last10": CritRating={}, MasteryRating={}, HasteRating={}, Intellect={}, Versatility={} )'
            .format(round(crt / 10, 2), round(mst / 10, 2), round(hst / 10, 2), round(int / 10, 2), round(vrs / 10, 2)))

    # give the average over the last 5
    crt = 0
    hst = 0
    int = 0
    mst = 0
    vrs = 0
    for entry in database:
        if database.index(entry) > len(database) - 6:
            crt += entry["CRT"]
            hst += entry["HST"]
            int += entry["INT"]
            mst += entry["MST"]
            vrs += entry["VRS"]
    print(
        '( Pawn: v1: "Resto-RDSW_last5": CritRating={}, MasteryRating={}, HasteRating={}, Intellect={}, Versatility={} )'
            .format(round(crt / 5, 2), round(mst / 5, 2), round(hst / 5, 2), round(int / 5, 2), round(vrs / 5, 2)))
    # and just the last one
    print(
        '( Pawn: v1: "Resto-RDSW_last": CritRating={}, MasteryRating={}, HasteRating={}, Intellect={}, Versatility={} )'
            .format(round(database[-1]["CRT"], 2), round(database[-1]["MST"], 2), round(database[-1]["HST"], 2), round(database[-1]["INT"], 2), round(database[-1]["VRS"], 2)))

if __name__ == "__main__":
    main()
