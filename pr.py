import requests, pyautogui
import keyboard


def main():
	with open('pass.txt', 'r') as f:
		url = f.readline()
	requests.post(url, data={"content": "Стартуем"})
	while True:
		if keyboard.is_pressed('s'):
			image = pyautogui.screenshot()
			image.save("screen.jpg")
			requests.post(url, files={"screenshot": open("screen.jpg", "rb")})
		if keyboard.is_pressed('Esc'):
			requests.post(url, data={"content": "Конец связи"})
			quit()
		if keyboard.is_pressed('l'):
			requests.post(url, data={"content": "Маловато"})
		if keyboard.is_pressed('b'):
			requests.post(url, data={"content": "Не то"})
		if keyboard.is_pressed('n'):
			requests.post(url, data={"content": "Нет"})
		if keyboard.is_pressed('y'):
			requests.post(url, data={"content": "Да"})
		if keyboard.is_pressed('1'):
			requests.post(url, data={"content": "1"})
		if keyboard.is_pressed('2'):
			requests.post(url, data={"content": "2"})
		if keyboard.is_pressed('3'):
			requests.post(url, data={"content": "3"})
		if keyboard.is_pressed('4'):
			requests.post(url, data={"content": "4"})
		if keyboard.is_pressed('4'):
			requests.post(url, data={"content": "5"})


if __name__ == '__main__':
	main()
