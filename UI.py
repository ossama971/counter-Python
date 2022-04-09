from operator import truediv
import logic
def userInput():
    value=input("please enter the action number as follow\n \
    1 for increment\n \
    2 for decrement\n \
    3 for reset\n \
    4 for display\n \
    5 to exit\n"
    )
    return int(value)

def main ():
    cnt = 0
    ok = True
    while ok:
        input = userInput()
        if input==1:
            cnt=logic.increment(cnt)
        elif input==2:
            cnt=logic.decrement(cnt)
        elif input ==3:
            cnt=logic.reset()
        elif input ==4:
            print("counter ==> ", cnt)
        elif input==5:
            ok=False
    print("Final Number ==>",cnt)
main()

