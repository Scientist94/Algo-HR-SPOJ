from pythonds.basic.queue import Queue
import random

class Printer:

	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timestamp


def simulation(numSec, pagePerMin):

	labprinter = Printer(pagePerMin)
	printQueue = Queue()
	waitingTime = []

	for currentSecond in range(numSec):

		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingTime.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)

		labprinter.tick()

	averageWait = sum(waitingTime)/len(waitingTime)
	print ("Average Wait %f secs %d tasks remaining."%(averageWait, printQueue.size()))

def newPrintTask():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	else:
		return False

for i in range(20):
	simulation(3600, 5)




