from pyscript import document, display
# This is the list of non-metal elements where the button would be searching for elements in
elements = {"BORON": ('B', 5, 10.81),
           "CARBON":('C', 6, 12.01),
           "NITROGEN":('N', 7, 14.007),
           "OXYGEN": ('O', 8, 15.999),
           "FLUORINE": ('F', 9, 18.998),
           "HELIUM": ('He', 4, 4.002602),
           "NEON": ('Ne', 10, 20.1797),
           "SILICON" : ('Si', 14 ,28.085),
           "PHOSPHORUS" : ('P', 15 ,30.974),
           "SULFUR": ('S', 16, 32.06),
           "CHLORINE" : ('Cl', 17, 35.45),
           "ARGON" : ('Ar', 13 ,39.948),
           "GERMANIUM": ('Ge', 32, 72.630),
           "ARSENIC": ('As  ', 33 ,74.9216 ),
           "SELENIUM" : ('Se',34 ,78.971),
           "BROMINE" : ('Br', 35, 79.904),
           "KRYPTON" : ('Kr', 36, 83.798),
           "ANTIOMY" : ('Sb', 51, 121.76),
           "TELLERIUM": ('Te', 52, 127.60),
           "IODINE": ('I', 53 ,126.904),
           "XENON" : ('Xe', 54, 131.293),
           "ASTATINE" : ('At', 85, 210),
           "RADON": ('Rn', 86, 222),
           "TENNESSINE": ('Ts',117 ,294),
           "OGANESSON": ('Og', 118 , 294),
           "HYDROGEN": ('H', 1 ,1.008)

            }


#this is gonna be the function of the button when finding the element
def search_element(e):

    element_1 = document.getElementById("element1").value.upper()
    #retrieve information from the dictionary
    result = elements.get(element_1, ('Element not found', "-", "-"))

    #Display the result in html
    document.getElementById("name").innerText = element_1
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]
