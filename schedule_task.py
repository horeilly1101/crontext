from threading import Thread
import schedule

def hw():
	print("hello, world")

schedule.every(5).seconds.do(hw)

def thread():
	while True:
		schedule.run_pending()

hw_thread = Thread(target=thread, daemon=True)
hw_thread.start()
hw_thread.join()