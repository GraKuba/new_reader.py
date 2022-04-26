import csv
import json
import pickle

temporary_list = []


class DownloadAndSave:
    def __init__(self, file_download, file_save):
        self.file_download = file_download
        self.file_save = file_save

    def download_csv(self):
        with open(self.file_download, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                temporary_list.append(line)
        return temporary_list

    def download_pkl_json(self, argument, file_type):
        with open(self.file_download, 'r' + argument) as f:
            file_type.load(temporary_list, f)
        return temporary_list

    def dump_csv(self):
        with open(self.file_save, "w") as f:
            writer = csv.writer(f)
            for line in temporary_list:
                writer.writerow(line)

    def dump_pkl_json(self, argument, file_type):
        with open(self.file_save, 'w' + argument) as f:
            file_type.dump(temporary_list, f)


class CSVHandler(DownloadAndSave):
    file_type = csv

    def load_file(self):
        return super().download_csv()

    def dump_file(self):
        return super().dump_csv()


class JSONHandler(DownloadAndSave):

    def load_file(self):
        super().download_pkl_json('', json)

    def dump_file(self):
        super().dump_pkl_json('', json)


class PICKLEHandler(DownloadAndSave):

    def load_file(self):
        super().download_pkl_json('b', pickle)

    def dump_file(self):
        super().download_pkl_json('b', pickle)


