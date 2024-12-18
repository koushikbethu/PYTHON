#  (*args) Positional variable-Length ARguments

def greet(*names):
  for name in names:
    print(f"Hello, {name}")
    
greet("kanna","papa","Ammu")
print() 
greet("sri","Krishna","Koushik")
print()

# (**kwargs)  Keyword Variable - length Arguments

def print_details(**details):
  for key,value in details.items():
    print(f"{key}:{value}")
    
print_details(name="Kanna",Age=17,city="Gujarat")
