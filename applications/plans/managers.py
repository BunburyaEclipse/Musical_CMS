from django.db import models

class plansManager(models.Manager):
    def get_piano(self):
        return self.filter(instrument=1).last()
    
    def get_sing(self):
        return self.filter(instrument=2).last()
    
    def get_guitar(self):
        return self.filter(instrument=3).last()

    def get_drumps(self):
        return self.filter(instrument=4).last()

    def get_bass(self):
        return self.filter(instrument=6).last()
    
    def get_violin(self):
        return self.filter(instrument=5).last()
