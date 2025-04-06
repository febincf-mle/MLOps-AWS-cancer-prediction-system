import os
import sys
import logging


log_dir = "logs"
log_filepath = os.path.join(log_dir, "logs.log")

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s %(module)s - %(message)s',
    
    handlers = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs.log")
    ]
)

logger = logging.getLogger("cancer_prediction")