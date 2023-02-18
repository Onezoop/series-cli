from func_commands import *

class Series:
	def __init__(self,in_c, first, second, init_gen = 1):
		self.c =  in_c
		self.map = {1:first, 2:second}
		self.keys = list(self.map)
		self.values = [self.map[x] for x in self.map]
		self.series_gen(init_gen)
	def series_gen(self, inp):
		if inp in self.map:
			return self.map[inp]
		for i in range(3, inp+1)		:
			self.map[i]=(self.map[i-1]+self.map[i-2])/(self.map[i-1]*self.c)
		self.keys = list(self.map)
		self.values = [self.map[x] for x in self.map]
		return self.map[inp]
	def dump(self, types, amt):
		self.series_gen(amt)
		cases = {"A":self.map,"V":self.values,"K":self.keys}
		if types in cases:
			return cases[types]
		else:
			return "Invalid Type"
		
series_dict = {"basic": Series(2, 1, 4)}
current_series_key = "basic"


running = True
while running:
	current_series = series_dict[current_series_key]
	user = input(f"input ({current_series_key}): ").strip()
	output = ""
	command = False
	
	try:
		user = int(user)
	except ValueError:
		command = True

	if command:
		if user in ("exit", "q"):
			running = False
		
		elif user == "change series":
			new_series_key = input("What series would you like to change to? ")
			if new_series_key in series_dict:
				current_series_key = new_series_key
				print("successfully changes series!")
			else:
				print("operation stopped; series does not exist")
	
		elif user in ("new series", "create new series", "create series"):
			new_series_name = input("what would you like the name of this new series to be? ")
			new_series_c = float(input("what should the C value be? "))
			new_series_first = int(input("what should the first value be? "))
			new_series_second = int(input("what should the second value be? "))
			if new_series_name in series_dict:
				ovrd = input("series with this name already exists, overwrite this series? (y/n) ").strip()
				if "y" in ovrd:
					pass
				elif "n" in ovrd:
					print("operation aborted.")
			series_dict[new_series_name] = Series(new_series_c, new_series_first, new_series_second)
			current_series_key = new_series_name
			
			print(f"operation success! Now in {new_series_name}")
		elif user in ("gen up", "gen to"):
			gen_max = input("Generate series up to what? ")
			for i in range(1, int(gen_max)):
				current_series.series_gen(i)
				
		elif user in ("pwd", "current series", "current_series", "series?", "series", "which series"):
			
			print(current_series_key)
		elif user in ("info", "constants", "consts"):
			print(f"{current_series_key}: \n c:{current_series.c}, \n first:{current_series.map[1]}, \n second:{current_series.map[2]}")
			
		elif user in ("w/o", "wo", "w", "write", "save"):
			print("not implemented")
		
		elif user == "dump":
			type_ops = input("dump values, keys, or all? (V/K/A) ").strip().upper()
			amt_ops = int(input("dump up to what amount? ").strip())
			print(current_series.dump(type_ops, amt_ops))
		
		
		
		
		
		
		
		
		
		
		
		else:
			print("command not recognized")
				
	else:
		if user > 0:
			if user in current_series.map:
				output = current_series.map[user]
			else:
				output = current_series.series_gen(user)
			print(output)
		else: print("entry has to be a non-zero positive number")
