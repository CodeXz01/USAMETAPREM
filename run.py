if __name__ == "__main__":
	try:
		__import__("enc_simple").security()
	except Exception as e:
		exit(str(e))
