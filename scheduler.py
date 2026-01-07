import schedule
import time
from alert_service import check_alerts

schedule.every().day.at("10:00").do(check_alerts)

while True:
    schedule.run_pending()
    time.sleep(60)
