import os
import sys
import logging
import argparse
import csv

import xlrd


log = logging.getLogger(__name__)


def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S")

    parser = argparse.ArgumentParser(prog="signal-marker")

    parser.add_argument(
        "-s", "--src", dest="src_dir", type=os.path.abspath, default='./',
        help="Directory to read xls files")

    parser.add_argument(
        "-d", "--dst", dest="dst_dir", type=os.path.abspath, default='./',
        help="Directory to save csv files")

    opts = parser.parse_args()

    src_dir = opts.src_dir
    dst_dir = opts.dst_dir

    if not os.path.isdir(src_dir):
        log.error("ERROR: Source path is not directory: {}".format(src_dir))
        sys.exit(1)
    if not os.path.isdir(dst_dir):
        log.error("ERROR: Destination path is not directory: {}".format(dst_dir))
        sys.exit(1)

    for filename in os.listdir(src_dir):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(src_dir, os.path.basename(filename))
            convert(file_path, dst_dir)


def convert(xls_path, csv_dest_dir):
    log.info("Parse file '{}'".format(xls_path))
    workbook = xlrd.open_workbook(xls_path)

    for sheet_name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(sheet_name)
        log.info("Processing sheet '{}'".format(sheet_name))
        filename = "{}_{}.csv".format(sheet_name, os.path.basename(xls_path))
        file_path = os.path.join(filename, csv_dest_dir)

        log.info('Saving csv file: {}'.format(file_path))
        with open(file_path, 'w') as csv_fd:
            csv_writer = csv.writer(csv_fd, quoting=csv.QUOTE_ALL)

            for row_num in range(sheet.nrows):
                csv_writer.writerow(sheet.row_values(row_num))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as exc:
        log.warning("Process terminated by user input!")
