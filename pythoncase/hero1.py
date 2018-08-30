import unittest
from herostore import Hero,Boss
class TestHero(unittest.TestCase):
    def test_init_hero(self):
        milo = Hero(name = 'milo',hp = 100,ack = 10)
        self.assertEqual(milo.hp,100)
        self.assertEqual(milo.ack,10)
    def test_hero_say(self):
        hero = Hero()
        x = hero.say()
        self.assertEqual(x,"superman!!!")
    def test_hero_ack(self):
        hero = Hero()
        y = hero.ack
        self.assertEqual(y,10)
    def test_get_hp(self):
        hero = Hero()
        hero.getHP(x = "baozi")
        self.assertEqual(hero.hp,110)
    def test_Boss(self):
        Turtle = Boss()
        self.assertEqual(Turtle.name,'Turtle')
        self.assertEqual(Turtle.hp,60)
        self.assertEqual(Turtle.ack,20)
    def test_hero_ack(self):
        milo = Hero()
        Turtle = Boss()
        milo.ackkk(Turtle)
        self.assertEqual(Turtle.ack,20)
unittest.main()
