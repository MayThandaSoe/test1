class Invoice:
    
    def __init__(self,partno,desc,quantity,price):
          self.partno = partno
          self.desc = desc
          self.quantity = quantity
          self.price   = price
          
    def set__my_attribute(self,value):
        self.__my_data=value
        return self.__my_data       
          
         
  def  calculate_invoice(self):
         print("Calculate Invoice",self.quantity * self.price)
      



def main():
      p1= Invoice("1 ","description",54,5000) 
      p1.calculate_invoice()
     

 main()









