from tg_module import *
from test_model import *
import threading
import datetime
import time


def start_datection(video):
    
    detection_thread = threading.Thread(target=detection_and_mention,
                                        args=(video,))
    detection_thread.start()
    lust_time_abuse = 0
    lust_time_arson = 0
    lust_time_stealing = 0
    lust_time_vandalizm = 0
    while detection_thread.is_alive():
        time_now = datetime.datetime.now().time()
        seconds = (time_now.hour * 60 + time_now.minute) * 60 + time_now.second + 61


        if os.path.exists("./runs/detect/predict/crops/Abuse/") and (seconds - lust_time_abuse > 60):
            time.sleep(0.1)
            img_emergency = os.listdir("./runs/detect/predict/crops/Abuse")[0] 
            send_emergency_message("На 1 камере 2го крыла", "абюзивное отношение", "./runs/detect/predict/crops/Abuse/" + img_emergency)
            lust_time_abuse = seconds
            shutil.rmtree("./runs/detect/predict/crops/Abuse/")


        if os.path.exists("./runs/detect/predict/crops/Arson/") and (seconds - lust_time_arson > 60):
            time.sleep(0.1)
            img_emergency = os.listdir("./runs/detect/predict/crops/Arson")[0]
            send_emergency_message("На 3 камере 2го крыла", "возгарание", "./runs/detect/predict/crops/Arson/" + img_emergency)
            lust_time_arson = seconds
            shutil.rmtree("./runs/detect/predict/crops/Arson/")


        if os.path.exists("./runs/detect/predict/crops/Stealing/") and (seconds - lust_time_stealing > 60):
            time.sleep(0.1)
            img_emergency = os.listdir("./runs/detect/predict/crops/Stealing")[0]
            send_emergency_message("На 3 камере 2го крыла", "возгарание", "./runs/detect/predict/crops/Stealing/" + img_emergency)
            lust_time_stealing = seconds
            shutil.rmtree("./runs/detect/predict/crops/Stealing/")


        if os.path.exists("./runs/detect/predict/crops/Vandalizm/") and (seconds - lust_time_vandalizm > 60):
            time.sleep(0.1)
            img_emergency = os.listdir("./runs/detect/predict/crops/Vandalizm/")[0]
            send_emergency_message("На 3 камере 2го крыла", "возгарание", "./runs/detect/predict/crops/Vandalizm/" + img_emergency)
            lust_time_vandalizm = seconds
            shutil.rmtree("./runs/detect/predict/crops/Vandalizm/")

    shutil.rmtree("./runs/detect/")


if __name__ == "__main__":
    start_datection("./runs/test_images/fire_video.mp4")

