import csv
import pandas as pd
import tensorflow as tf

f = './data/domainc/train.tsv'


def _read_tsv(input_file, quotechar=None):
    """读取 tsv 的工具方法"""
    fw = open('./test.tsv', 'w', encoding='utf-8')
    with open(input_file, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t", quotechar=quotechar)
        lines = []
        for line in reader:
            new = line[0].replace('   ', '\t')
            fw.write(new + '\n')
            lines.append(line)
    fw.close()
    return lines


if __name__ == '__main__':
    _read_tsv(f)
