#  to accept the stock (in kg) and price (of per kg in rupees) of fruits available in fruit market using dictionary and then calculate the total value (in rupees) of fruit market
fruit={}
while 1:
  ch=int(input("\nMENU\n1.Add a fruit\n2.Buy a fruit\n3.Total valuation\n4.Display inventory\n5.Discard fruit\n6.Exit\nYour choice: "))
 
  if ch==1:
    fruitname=input("Enter name of fruit (in lower case): ")
    if fruitname in fruit:
       i=int(input("Enter stock to be added: "))
       fruit[fruitname][0]=fruit[fruitname][0]+i
    else:
      i=int(input("Enter stock to be added: "))
      j=int(input("Enter price of fruit (Rs): "))
      fruit[fruitname]=[i,j]
  elif ch==2:
    buy=input("Enter name of fruit that you want to buy(in lower case): ")
    for fruitname in fruit:
      if buy==fruitname:
        print("Available stock is: ",fruit[fruitname][0])
        q=int(input("Enter the quantity: "))
        if q<=fruit[fruitname][0]:
          print("Your bill is Rs.",q*fruit[fruitname][1])
          fruit[fruitname][0]-=q
        else:
          print("Insufficient Quantity")
        break
      else: 
        print("Fruit not available")
  elif ch==3:
    total=0
    for price in fruit:
     money= fruit[price][1]*fruit[price][0]
     print (price,":",money)
     total=total +money
    print ("The total valuation is Rs.",total)
  elif ch==4:
    print("Our inventory is: ")
    for fruitname in fruit:
      print (fruitname)
      print ("prices/kg: ", fruit[fruitname][1])
      print ("stock: ", fruit[fruitname][0])
  elif ch==5:
    dis=input("Enter name of fruit that you want to buy(in lower case): ")
    for a in fruit[fruitname]:
      if dis==fruitname:
        print("Available stock is: ",fruit[fruitname][0])
        q=int(input("Enter the quantity: "))
        if q<=fruit[fruitname][0]:
          fruit[fruitname][0]-=q
        else:
          print("Insufficient Quantity")
          break
      else: 
          print("Fruit not available")
  elif ch==6:
    break
  else:
    print("Invalid input!!")
