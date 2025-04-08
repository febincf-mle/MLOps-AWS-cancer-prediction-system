import os
import sys
import logging


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir, "logs.log")

print(log_filepath)

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s %(module)s - %(message)s',
    
    handlers = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
    ]
)

logger = logging.getLogger("cancer_prediction")