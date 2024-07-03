#!/usr/bin/env python3

import pyperclip


def change_path(path):
	path = path.replace('"', "")
	path = path.replace("'", "")

	if path.startswith("T:"):
		path = path.replace("\\", "/")
		path = path.replace("T:", "/mnt/t")
	elif path.startswith(("mnt/t", "/mnt/t")):
		path = path.replace("/mnt/t", "T:")
		path = path.replace("/", "\\")
	else:
		return (path)

	return (path)


def main():
	path = pyperclip.paste() # взять путь из буфера
	new_path = change_path(path) # изменить путь
	pyperclip.copy(new_path) # вставить путь в буфер


if __name__ == "__main__":
	main()
