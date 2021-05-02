from datetime import datetime, timedelta
import time
import json
import subprocess

hour = timedelta(hours=1).total_seconds()

while True:
    out = subprocess.check_output(["hdfs", "dfs", "-count", "/datafiles/jk"])

    out = out.strip().split()

    ret = out[1].decode('utf-8')
    if int(ret) > 0:
        with open("secrets.json", "r") as f:
            info = json.load(f)

        master = "spark://{}:{}".format(info['host'], info['spark_info']['port'])
        subprocess.call(["spark-submit", "--master", master, "preprocess.py"])

    print(datetime.today(), ret)
    
    time.sleep(int(hour))
