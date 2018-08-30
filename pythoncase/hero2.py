from herostore import *
import time
def main():
    milo = Hero()
    boss = Boss()
    print("now {} are walking".format(milo.name))
    print("遇到大Boss")
    while milo.hp > 0 and boss.hp > 0:
          print(milo.say())
          milo.ackkk(boss)
          print(boss.say("疼"))
          time.sleep(0.1)
if __name__ == "__main__":
    main()
