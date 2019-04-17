class Test():
	def __len__(self):
		print("len called")
		return True
	
	
	def __bool__(self):
		print("bool called")
		return True


print(bool(Test()))
