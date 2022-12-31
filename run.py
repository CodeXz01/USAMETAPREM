if __name__ == "__main__":
	try:
		__import__("enc_tes").security()
	except Exception as e:
		exit(str(e))
