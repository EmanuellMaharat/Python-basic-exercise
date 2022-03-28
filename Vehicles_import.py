class Cars:
    def __init__(self,model,color,num_wheels, multimedia):
        self.model = model
        self.color = color
        self.num_wheels = num_wheels
        self.multimedia = multimedia

class Bycicle:
    def __init__(self,weight,color, cost ):
        self.weight = weight
        self.color_bycicle = color
        self.cost = cost

class Airplane:
    def __init__(self ,wings , model , cost ):
        self.wings = wings
        self.model_airplane = model
        self.cost_airplane = cost


from Vehicles import Cars

suzuki_swift = Cars (2014 ,'Black' , 4 , 'android' )
print(suzuki_swift.color)

from Vehicles import  Bycicle
bmx = Bycicle(2,'Red' , '200ILS')
print(bmx.color_bycicle)

from Vehicles import  Airplane

boeing = Airplane (4 , 'White' , '1,000,000 ILS')
print (boeing.cost_airplane)