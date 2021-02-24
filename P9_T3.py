##Створіть англо-український словник та програму, що  на його основі будує
##українсько-англійський словник.

translater = {"translate" : "перекласти",
              "to be" : "бути",
              "more" : "більше",
              "carrot" : "морква"
              }

for key, value in translater.items():
    print ("{} - {}".format (value, key))
