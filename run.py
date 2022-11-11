if __name__ == "__main__":
	try:
		__import__("enc_van").make()
	except Exception as e:
		exit(str(e))
