from foroshgah_db_fun import customer, create_tables, items, check_manager, add_sabad_kharid, namayessh_daryaft, show_sabad_kharid, hazine_fun, payment_fun,add_orders,charge_wallet
from password import generate_password
create_tables()


def manager_fun():
    while True :
        work  = int(input("""what are you here for ?
1.add item
2.delet item
3.edit item
4.cheak taskbar
5.exit 
    """))
        if work == 1 :
            name = input("enter the name of the item : ")
            price = input("enter the price of the item : ")
            description = input("write a description for the item : ")
            topic = input("chose a topic : ")
            new_item = items(name , price , description , topic)
            items.add_item(new_item)
            print("item added successfully")
        elif work == 2 :
            name = input("enter the name : ")
            id = input("enter the id : ")
            delete = items.delete_item(id , name)
            if delete == True:
                print("item deleted successfully")
            else:
                print("try again")
        elif work == 3 :
            topics = ["name" , "price" , "description" , "topic"]
            id = input("enter the id : ")
            topic = input("what are you going to change (name / price / description / topic ) : ")
            while topic in topics :
                new_data = input("enter the new data : ")
                update = items.update(id , topic, new_data)
                if update == True:
                    print("data updated")
                    break
                else:
                    print("not ok ")
        elif work == 4 :
            with open ("orders.txt" , "r")as file:
                taskbar = file.read()
                print(taskbar)
            pass
        elif work == 5 :
            break


def customer_fun(customer_id,username):
    while True:
        kar = int(input("""what are you here for ?
1.see items
2.sabad khrid
3.charge wallet
4.history
5.exit
"""))
        if kar == 1 :
            cheak_topic = int(input("""chose a topic : 
1.cloth
2.technology
3.food
4.show me all of theme . 
"""))
            if cheak_topic == 1 :
                topic = "cloth"
                namayessh_daryaft(customer_id , topic)
            elif cheak_topic == 2 : 
                topic = "technology"
                namayessh_daryaft(customer_id , topic)
            elif cheak_topic == 3 :
                topic = "Food"
                namayessh_daryaft(customer_id , topic)
            elif cheak_topic == 4 :
                list = items.show_all_items()
                for i in list :
                    print(i)
                add_item = input("do yoy want to add any item into your sabadkharid (y/n): ")
                if add_item.lower() == "y" :
                    item_id = input("enter the item id : ")
                    tedad = input("how many ? ")
                    add_sabad_kharid(customer_id, item_id, tedad)
                    print("added to the sabad kharid")
                elif add_item.lower() == "n":
                                pass

            
        elif kar == 2 :
            sabad = show_sabad_kharid(customer_id)
            if len(sabad) == 0:
                print("its empty")
                print("You should choose items first")
                pass
            else:
                for i in sabad:
                    print(i)
                hazine_kol = hazine_fun(customer_id)
                cheak_payment = input("Do you want to pay (y/n)? ")
                if cheak_payment == "y":
                    payment = payment_fun(username, customer_id,hazine_kol)
                    print("Payment successful.")
                    add_orders(customer_id,username)
                else:
                    pass
   
            
                
        elif kar == 3 :
            meghdar = int(input("how much are you going to charge ? : "))
            charge = charge_wallet(customer_id,username,meghdar)  
            if charge :
                print("wallet charged")
            
            pass

        elif kar == 4 :
            print("not ready yet !")
            pass
        elif kar == 5 :
            break


def ghabl_vorod():
    while True: 
        darkhast = int(input("""1.singup
2.login
3.exit
"""))
        if darkhast == 1 :
            name = input("enter your name : ")
            last_name = input("enter your last_name : ")
            username = input("choose a username for your self : ")
            while True :
                try:
                    phone_number = int(input("enter the phone number : "))
                    break
                except:
                    print("mojadad talash konid")
            pass_sug = int(input("""do you want us to suggest you a password or you are going to make it yourself ?  
1.us
2.myself
"""))
            if pass_sug == 1 :
                password = generate_password(8)
                print(f"your password is : {password}")
            elif pass_sug == 2 :
                password = input("enter your pass : ")
            wallet = input("how much are you going to charge your wallet ? : ")
            new_customer = customer(name, last_name, phone_number, username, password, wallet)
            print(customer.add_customer(new_customer))
            print("     \\\welcome///    ")
            customer_id = customer.id_funder(new_customer.username)[0]
            
            customer_fun(customer_id,new_customer.username)
        
        if darkhast == 2 :
            try:
                man_cust = int(input("""you are a manager or a customer ?
1.manager
2.customer
"""))
            except:
                print("enter number")
            if man_cust == 1 :
                x = 1
                while x < 4:
                    username = input("enter your username: ")
                    password = input("enter your password: ")
                    if check_manager(username, password):
                        print("manager exists.")
                        manager_fun()
                        break 
                    else:
                        print("Invalid username or password.")
                        x = x + 1
                        if x == 4:
                            print("Too many failed attempts. Please try again later.")

            if man_cust == 2 :
                x = 1
                while x < 4:
                    username = input("enter your username: ")
                    password = input("enter your password: ")
                    if customer.check_customer(username, password):
                        print("User exists.")
                        customer_id = customer.id_funder(username)[0]
                        customer_fun(customer_id, username)
                        break 
                    else:
                        print("Invalid username or password.")
                        x = x + 1
                        if x == 4:
                            print("Too many failed attempts. Please try again later.")
        if darkhast == 3 :
            break
        
ghabl_vorod()