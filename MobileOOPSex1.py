class Mobile: 

    def __init__(self): 

        self.brandName = "Samsung" 
        self.color= "Black" 

    def calling(self): 
        print("call the number") 
    
    def cameraclick(self): 
        print("click the photo") 

 

M1 = Mobile()  # init function is initialised as soon as object is created 
print(M1.calling()) 
print(M1.cameraclick()) 
M2=Mobile() 
print(M2.calling()) 
print(M2.cameraclick()) 