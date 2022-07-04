import csv
def writer(text, file,delim):
    with open(file,'a+', newline="",encoding="utf-8") as f:
        file_writer = csv.writer(f, delimiter = delim, lineterminator="\r")
        file_writer.writerow (text)