import csv


class Characters:

    def getBrawlersID():
        BrawlersID = []
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    #print(row.index("Hero"))
                    if row[25] == 'Hero' and row[2].lower() != 'true' and (line_count - 2 < 80):
                        BrawlersID.append(line_count - 2)
                    line_count += 1

            return BrawlersID