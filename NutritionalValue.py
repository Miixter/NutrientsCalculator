import Ingredients

def calc_ingredients(ingredienser):
    kcal = 0
    fett = 0
    kolhydrat = 0
    protein = 0
    list = ingredienser.split(" ")
    for element in list:
        for ingredienser in Ingredients.Ingredient_dict:
            element_separation = element.split(",")
            if element_separation[0].lower() == ingredienser:
                kcal = kcal + float(Ingredients.Ingredient_dict[ingredienser][0])/100*float(element_separation[1])
                fett = fett + float(Ingredients.Ingredient_dict[ingredienser][1])/100*float(element_separation[1])
                kolhydrat = kolhydrat + float(Ingredients.Ingredient_dict[ingredienser][2])/100*float(element_separation[1])
                protein = protein + float(Ingredients.Ingredient_dict[ingredienser][3])/100*float(element_separation[1])
    return [kcal, fett, kolhydrat, protein]

def calc_meals(måltider):
    kcal = 0
    fett = 0
    kolhydrat = 0
    protein = 0
    list = måltider.split(" ")
    for element in list:
        for ingredienser in Ingredients.Måltider_dict:
            if element.lower() == ingredienser:
                kcal = kcal + Ingredients.Måltider_dict[ingredienser][0]
                fett = fett + Ingredients.Måltider_dict[ingredienser][1]
                kolhydrat = kolhydrat + Ingredients.Måltider_dict[ingredienser][2]
                protein = protein + Ingredients.Måltider_dict[ingredienser][3]
    return [kcal, fett, kolhydrat, protein]


def welcome():
    print("***")
    print("Välkommen. Med detta skript kan du räkna ut ditt dagliga intag av kalorier, fett, kolhydrater och protein!")
    print("***")
    print("Vi sätter igång direkt!")
    print(" ")
    run()

def run():    
    print("Ange ifall du vill lägga in ingredienser direkt, eller välja en redan färdigkomponerad måltid. Skriv 'visa' för att se tillgängliga ingredienser/måltider. För att avsluta programmet, skriv 'exit'. ")
    message = input("Skriv antingen 'M', 'I', 'visa' eller 'exit': ")
    print("***")
    handle_input(message)
    
def handle_input(message):
    if message == "visa":
        print("***INGREDIENSER TILLGÄNGLIGA***")
        for ingrediens in Ingredients.Ingredient_dict:
            print(ingrediens)
        print("")
        print("***MÅLTIDER TILLGÄNGLIGA***")
        for måltider in Ingredients.Måltider_dict:
            print(måltider)
        print("***")
        run()
    if message == "I":
        list2 = [0,0,0,0]
        ingredienser = input("Skriv upp samtliga ingredienser som du använt i din måltid, följt av antalet gram. Exempelvis 'kvarg,100 rostmackor,75':\n")
        message2 = input("Vill du lägga till måltider också? Y/N:")
        if message2 == "Y":
            måltider = input("Skriv de måltider du vill lägga till. Exempelvis 'köttfärssås carbonara': \n")
            list2 = calc_meals(måltider)
        list1 = calc_ingredients(ingredienser)
        total_values = [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2], list1[3]+list2[3]]
        print("***")
        print(f"antal kalorier: {total_values[0]} \nantal gram fett: {total_values[1]} \nantal gram kolhydrater: {total_values[2]} \nantal gram protein: {total_values[3]}")
        if sum(total_values) == 0:
            print("Hmm, 0 på allt verkar fel. Se till att inputen har rätt syntax, och att varje namn finns med i ingrediens- eller måltidsdictionaryt!")
        print("***")
        run()
        
    
    elif message == "M":
        list2 = [0,0,0,0]
        måltider = input("Skriv de måltider du vill lägga till. Exempelvis 'köttfärssås carbonara': \n")
        message2 = input("Vill du lägga till ingredienser också? Y/N:")
        if message2 == "Y":
            ingredienser = input("Skriv de inredienser du vill lägga till. Exempelvis 'kvarg,100 ägg,100': \n")
            list2 = calc_ingredients(ingredienser)
        list1 = calc_meals(måltider)
        total_values = [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2], list1[3]+list2[3]]
        print("***")
        print("DITT INTAG AV NÄRINGSÄMNEN FÖR DET DU HAR MATAT IN:")
        print(f"antal kalorier: {total_values[0]} g \nantal gram fett: {total_values[1]} g \nantal gram kolhydrater: {total_values[2]} g \nantal gram protein: {total_values[3]} g")
        if sum(total_values) == 0:
            print("Hmm, 0 på allt verkar fel. Se till att inputen har rätt syntax, och att varje namn finns med i ingrediens- eller måltidsdictionaryt!")
        print("***")
        run()
    
    elif message == "exit":
        quit()
    
    else:
        print("***")
        message3 = input("Otillåten input. SKriv antingen 'I', 'M', eller 'exit': ")
        handle_input(message3)


def main():
    welcome()

main()
