import os 

def auto(message):
    os.system('git add .')
    os.system(f'git commit -m \"{message}\"')
    os.system('git push -u origin main')
def question(name):
    os.system('git add .')
    os.system(f'git commit -m \"{name} done\"')
    os.system('git push -u origin main')


def main():
    option = int(input("Choose option \n1. Enter a message \n2. Completed a question \nany other key to quit \ninput : "))
    while(True):
        if(option == 1):
            message = input("Enter the commit message : ")  
            auto(message)
        elif(option == 2):
            name = input("Enter the name of the question : ")
            question(name)
        else:
            break
         

if __name__ == "__main__":
    main()
