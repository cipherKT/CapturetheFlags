import os 

def auto(name):
    os.system('git add .')
    os.system(f'git commit -m \"{name} done\"')
    os.system('git push -u origin main')

def main():
    name = input("Enter the question which is just completed : ")  
    auto(name)

if __name__ == "__main__":
    main()
