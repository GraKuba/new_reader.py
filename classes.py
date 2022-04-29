import csv
import json
import pickle

ls = []


class DownloadAndSave:
    def __init__(self, file_download: str, file_save: str):
        self.file_download = file_download
        self.file_save = file_save

    def download_csv(self):
        with open(self.file_download, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                ls.append(line)
            return ls

    def download_pkl_json(self, argument: str):
        if argument == '':
            file_type = json
        else:
            file_type = pickle
        with open(self.file_download, 'r' + argument) as f:
            data = file_type.load(f)
            for line in data:
                ls.append(line)
            return ls

    def dump_csv(self):
        with open(self.file_save, "w") as f:
            writer = csv.writer(f)
            for line in ls:
                writer.writerow(line)

    def dump_pkl_json(self, argument: str):
        if argument == '':
            file_type = json
        else:
            file_type = pickle
        with open(self.file_save, 'w' + argument) as f:
            file_type.dump(ls, f)


class CSVHandler(DownloadAndSave):

    def load_file(self):
        return super().download_csv()

    def dump_file(self):
        return super().dump_csv()


class JSONHandler(DownloadAndSave):

    def load_file(self, argument):
        super().download_pkl_json(argument)

    def dump_file(self, argument):
        super().dump_pkl_json(argument)


class PICKLEHandler(DownloadAndSave):

    def load_file(self, argument):
        super().download_pkl_json(argument)

    def dump_file(self, argument):
        super().dump_pkl_json(argument)
