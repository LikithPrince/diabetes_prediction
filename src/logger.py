import logging
import os


log_file = "log.log"
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path, exist_ok= True)

log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(
   filename=log_file_path,
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s',
   datefmt='%Y-%m-%d %H:%M:%S'
)

# if __name__ == "__main__":
#    logging.info("Starting...")