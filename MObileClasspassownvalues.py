Class Mobile:
    def__init__(self,BrandNm,color,isJack):
        self.brandName = BrandNm
        self.color = color
        self.isJack = isJack
    def calling(self):
        print("calling")
    def clicking(self):
        print("have clicked for a photo")
    
M1 = Mobile("Samsung","Orange",False)
print(M1.brandName)
print(M1.color)
print(M1.isJack)
M2 = Mobile("OnePlus","Blue",True)
print(M2.brandName)
print(M2.color)
print(M2.isJack)
