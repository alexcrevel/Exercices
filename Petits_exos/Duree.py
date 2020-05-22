class Duree:
  def __init__(self, min=0, sec=0):
    self.min = min
    self.sec = sec
  def __str__(self):
    return "{0:02}:{1:02}".format(self.min, self.sec)

d1 = Duree(3, 7)
print(d1)