import Image, ImageDraw


def rysuj():
   image = Image.new('RGBA', (200, 200))
   draw = ImageDraw.Draw(image)
   draw.ellipse((20, 20, 180, 180), fill = 'yellow', outline ='black')
   draw.point((100, 100), 'red')
   image.show()

def zapisz(fileName):
   image = Image.new('RGBA', (200, 200))
   image.save(fileName)

	
# Nalezy stworzyc klase "Kolo" oraz jej metody, 
# tak aby dzialal ponizszy kod:

kolo = Kolo()
kolo.rysuj()
kolo.zapisz("kolo.jpg")

