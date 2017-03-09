import base

class Derived(base.MyBase):

    def __init__(self):
        super(Derived, self).__init__()
        print "Derviced class object "

    def get_stuff(self):
        print self.name
        print self.number


    def setUp(self):
        super(Derived, self).setUp()
        print "In derived setup"
