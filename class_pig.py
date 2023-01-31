class Pig:
    belly_price = 1000 # 클래스 변수
    
    def __init__(self, stock):
        self.stock = stock

    # 주문이 들어왔을 때의 가격 -> 메서드
    def order_price(self, amount):
        if self.stock >= amount:
            return self.belly_price * amount

        else:
            return "재고가 없어요."
            # return f"재고가 {self.stock}만큼 있습니다"
        
    def order_original_price(self, amount):
        if self.stock >= amount:
            return self.belly_price * amount    

    def order(self, amount, money):
        
        price = self.order_price(amount)
        if price <= money:
            self.stock = self.stock - amount
            change = money - price
            return change
        else: 
            return '못삼'
    
    def discount(self, per):
        b_pig.belly_price = b_pig.belly_price * (1 - per)
        return self.belly_price
    
    def original_price(self):
        return Pig.belly_price
        
    @classmethod
    def original_price(cls):
        return cls.belly_price

a_pig = Pig(100)
b_pig = Pig(150)
# print(a_pig.belly_price)
# print(b_pig.belly_price)

#b_pig.belly_price = 500
# print(a_pig.belly_price)
# print(b_pig.belly_price)

# print(a_pig.stock)
# print(a_pig.order(50, 10000000))
# print(a_pig.stock)
# print(b_pig.stock)
# print(a_pig.order_price(150))


# b 돼지의 가격이 20% 할인됨
# b 돼지에서 원래 가격도 접근 가능함
# b 돼지를 50만큼 샀을 때, 원래 가격, 할인된 가격 둘다 반환.

#b_pig.belly_price = b_pig.belly_price * 0.8
#print(b_pig.belly_price) #800이라고 나오긴함. 앞에건 인스턴스 변수 뒤에건 클래스 변수접근
#하지만 클래스 쓰는 의미가 없음

b_pig.discount(0.2)
print(b_pig.belly_price)

#Pig.belly_price #해도 되지만 b돼지라고 지정되었으니

print(b_pig.original_price)
print(b_pig.order_price(50))
print(b_pig.order_original_price(50))
