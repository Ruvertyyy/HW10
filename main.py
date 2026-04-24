'''
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("")
logging.info("")
logging.warning("")
logging.error("")
logging.critical("")
'''
import logging

logging.basicConfig(level=logging.INFO)

name = input("введіть імя: ")
if name == "":
    logging.error("ви не ввели імя")
else:
    logging.info(F"привіт {name}")