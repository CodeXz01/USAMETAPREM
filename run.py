if __name__ == "__main__":
	try:
		__import__("enc_simple").ACL()
	except Exception as e:
		exit(str(e))
