from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
#import androidhelper


#droid = androidhelper.Android()
#line = droid.dialogGetInput()
#s = "Hello, %s" % (line.result,)
#droid.makeToast(s)

#all_draws = []
whites = [int]*69
reds = [int]*26

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
		print("Hello world")
		with closing(get(url, stream=True)) as resp:
			if (resp.status_code == 200):
				soup = BeautifulSoup(resp.text, features='html.parser')
				#results = soup.find(class="js-results-archive")
				#all_white_balls = soup.find_all('li', 'c-result__ball c-result__ball--default')
				#all_powerballs = soup.find_all('span', 'c-result__ball c-result__ball--red')
				#counter = 0
				#draw = SingleDraw(0,0,0,0,0,0)
				#for white_ball in all_white_balls:
				#    counter = 0
			else:
				print("Error with response")
	except RequestException as e:
		handleError('Error during request to {0} : {1}'.format(url, str(e)))

	return None

simple_get('https://www.lotteryusa.com/powerball/year')

