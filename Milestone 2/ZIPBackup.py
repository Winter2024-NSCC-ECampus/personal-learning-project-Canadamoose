import os
import shutil
from datetime import datetime

def backup_folder(source_dir, backup_dir):

    try:
        # Create backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_name = f"backup_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_name)

        # Create ZIP backup
        shutil.make_archive(backup_path, 'zip', source_dir)

        # Log success
        log_entry = f"{datetime.now()}: SUCCESS - Created {backup_name}.zip\n"
        with open(os.path.join(backup_dir, "backup_log.txt"), 'a') as f:
            f.write(log_entry)

        return True

    except Exception as e:
        # Log failure
        error_entry = f"{datetime.now()}: FAILED - {str(e)}\n"
        with open(os.path.join(backup_dir, "backup_log.txt"), 'a') as f:
            f.write(error_entry)
        return False
    
# CHANGE THESE IF YOU USE ON A DIFFERENT PC
source = r"C:\Users\canad\Code\PROG3010 - Self\Backups"  # Folder to back up
destination = r"C:\Users\canad\Code\PROG3010 - Self\Backedup"  # Where to save backups

backup_folder(source, destination)