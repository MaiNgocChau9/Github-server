from datetime import datetime
import pytz

timezone = pytz.timezone("Asia/Ho_Chi_Minh")
print(datetime.now(timezone))