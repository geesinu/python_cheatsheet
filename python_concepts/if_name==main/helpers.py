def greet():
  print("Hello World")

print (__name__)

# acts as a guard, won't be run if gets import from another script
if __name__ == "__main__":
  greet()