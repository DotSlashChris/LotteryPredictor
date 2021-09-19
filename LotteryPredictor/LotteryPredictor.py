from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#all_draws = []
#whites = [int]*69
whites = [0 for i in range(70)] 
#reds = [int]*26
reds = [0 for i in range(27)] 

class SingleDraw:
	def __init__(self, ball1, ball2, ball3, ball4, ball5, pb):
		self.Ball1 = ball1
		self.Ball2 = ball2
		self.Ball3 = ball3
		self.Ball4 = ball4
		self.Ball5 = ball5
		self.PB = pb

def handleError(e):
	print(e)  

def simple_get(url):
	try:
		# Collect white balls
		with closing(get(url, stream=True)) as resp:
			if (resp.status_code == 200):
				soup = BeautifulSoup(resp.text, features='html.parser')
				allWhiteBalls = soup.find_all('li', class_='c-ball c-ball--default c-result__item')
				for whiteBall in allWhiteBalls:
					whites[int(whiteBall.get_text("|", strip=True))] += 1
					#print(whiteBall.get_text("|", strip=True))
			else:
				print("HTML Error with response")
		
		# Collect red balls
		with closing(get(url, stream=True)) as resp:
			if (resp.status_code == 200):
				soup = BeautifulSoup(resp.text, features='html.parser')
				allPowerBalls = soup.find_all('li', class_='c-result__item c-result__bonus-ball')
				for powerBall in allPowerBalls:
					reds[int(powerBall.get_text("", strip=True)[:-2])] += 1
					#print(powerBall.get_text("", strip=True)[:-2])
			else:
				print("HTML Error with response")
	except RequestException as e:
		handleError('Error during request to {0} : {1}'.format(url, str(e)))

	return None

def simple_get_local(path):
	try:
		# Collect white balls
		with open(path) as filePath:
			soup = BeautifulSoup(filePath, features='html.parser')
			allWhiteBalls = soup.find_all('li', class_='c-ball c-ball--default c-result__item')
			for whiteBall in allWhiteBalls:
				whites[int(whiteBall.get_text("|", strip=True))] += 1
				#print(whiteBall.get_text("|", strip=True))

		# Collect red balls
		with open(path) as filePath:
			soup = BeautifulSoup(filePath, features='html.parser')
			allPowerBalls = soup.find_all('li', class_='c-result__item c-result__bonus-ball')
			for powerBall in allPowerBalls:
				reds[int(powerBall.get_text("", strip=True)[:-2])] += 1
				#print(powerBall.get_text("", strip=True)[:-2])
	except:
		return None

	return None

#simple_get('https://www.lotteryusa.com/powerball/year')
simple_get_local('C:/Projects/LotteryPredictor/LotteryPredictor/Lottery')

# Print counts of Whites 
counter = 0
for whiteBall in whites:
	print(str(counter) + "=" + str(whiteBall))
	counter += 1

# Print counts of Reds
counter = 0
for redBall in reds:
	print(str(counter) + "=" + str(redBall))
	counter += 1