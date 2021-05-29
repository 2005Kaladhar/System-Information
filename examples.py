import time
import psutil

def on_calculate_speed(self, interface):
    dt = 1 # I find that dt = 1 is good enough

    t0 = time.time()

    try:
        counter = psutil.net_io_counters(pernic=True)[interface]
    except KeyError:
        return []

    tot = (counter.bytes_sent, counter.bytes_recv)
    while True:
        last_tot = tot
        time.sleep(dt)
        try:
            counter = psutil.net_io_counters(pernic=True)[interface]
        except KeyError:
            break
        t1 = time.time()
        tot = (counter.bytes_sent, counter.bytes_recv)
        ul, dl = [
            (now - last) / (t1 - t0) / 1000.0
            for now, last
            in zip(tot, last_tot)
        ]
        return [int(ul), int(dl)]
        t0 = time.time()

while SomeCondition:
   # "wlp2s0" is usually the default wifi interface for linux, but you
   # could use any other interface that you want/have.
   interface = "wlp2s0"
   result_speed = on_calculate_speed(interface)
   if len(result_speed) < 1:
      print("Upload: - kB/s/ Download: - kB/s")
   else:
      ul, dl = result_speed[0], result_speed[1]
      print("Upload: {} kB/s / Download: {} kB/s".format(ul, dl))