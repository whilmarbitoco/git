import os

def main():
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  os.system(f'git config --global user.name "{name}"')
  os.system(f'git config --global user.email "{email}"')
  
  winlin = input("Are you using [1] Windows or [2] Linux:")
  if winlin == "1":
    os.system("git config --global core.autocrlf true")
  elif winlin == "2":
    os.system("git config --global core.autocrlf input")
  else:
    print("Please select [1] Windows or [2] Linux")
    
  editor = input("Enter the text editor you use (optional): ")
  if editor:
    os.system(f'git config --global core.editor "{editor}"')
  else:
    print("Editor not set")

if __name__ == "__main__":
  main()
  print("Set Up Complete")
