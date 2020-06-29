import speedtest
import datetime
import time

def getSpeed():
	servers = []
	threads = None
	s = speedtest.Speedtest()
	s.get_servers
	s.get_best_server()
	s.download(threads=threads)
	s.upload(threads=threads)
	s.results.share()
	results_dict = s.results.dict()
	return results_dict['download']

def getTime():
	return datetime.datetime.now()


def main():
	
	running = True
	i = 0
	while(running):
		try:
			output = str(getTime()) +  "," + str(getSpeed()) + "\n"
			log = open("log.txt","a")
			log.write(output)
			print (str(i) + '         ' + output)
			log.close()
			time.sleep(30 * 60)
			i += 1
		except:
			print("ERROR: Retrying connection")
			
if __name__ == "__main__":
	main()