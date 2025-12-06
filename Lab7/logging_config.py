import logging

file_logger = logging.getLogger('currency.log') #tao logger
file_logger.setLevel(logging.INFO)

handler = logging.FileHandler("currency.log", mode="a", encoding="utf-8") #tao file ghi log
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s",
                             datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

file_logger.addHandler(handler)