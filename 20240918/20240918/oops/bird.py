class bird :
    def fly(self):
        return 'crow is flyinggggg'
    
class parot(bird):
    def fly(self):
        return 'parot is flying'    


class eagle(bird):
    def fly(self):
        return 'eagle is flying'

def test_fly(bird):
      print(bird.fly())            

print(test_fly(parot))      