import derived

class Derived2(derived.Derived):

    def setUp(self):
        super(Derived2,self).setUp()
        print "In derived 2 setup"



d = Derived2()

d.setUp()
