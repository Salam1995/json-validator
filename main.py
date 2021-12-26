"""Main file consuming report Class"""

from src.report import Report


def main():
    
    from lib import logger
    log = logger.get_logger()

    report = Report(file_path='./data/input.json', logger=log)
    report.GenerateReport()


if __name__ == "__main__":
    main()
