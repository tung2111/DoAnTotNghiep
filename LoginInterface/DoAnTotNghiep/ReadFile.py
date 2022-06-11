Index = 0
TocalCalo = 0
ListMeal = ['','','','','','','','','']
FOOD= []
FRUIT= []
OTHER = []
CheckboxMeal=[False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
counter = 0
jumper = 10
progress_val = 0
user = ""
password = ""
confirmpassword = ""
i = 0
status = False
func = 0
func_yoga=0
rep = 0
ui = ''
cp = 0
img = ''
Image_TimeTable = 0
flagRight = 1  # 1 la co the bac RIGHT
check = False  # kiem tra yoga dung sai
check2 = False  # khong che nhac
giay_tt = False

checkbox = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox.txt","r")
ListMealWidget = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal.txt","r")
for indexCheckbox in range(69):
    if checkbox.readline() == 'True\n':
        CheckboxMeal[indexCheckbox] =    True
    else:
        CheckboxMeal[indexCheckbox] =    False

        #
for indexmeal in range(10):
    LoadMealFromFile = ListMealWidget.readline().strip('\n')
    if LoadMealFromFile != '':
        ListMeal[indexmeal] = LoadMealFromFile
    else:
        break
print(ListMeal)
del ListMeal [ 1 : 9]
print(ListMeal)
#close file
checkbox.close()
ListMealWidget.close()