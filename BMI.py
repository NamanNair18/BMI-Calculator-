def caluculate_bmi(weight, height):
    return weight / (height**2)

def get_bmi_category(BMI):
    if BMI < 18.5:
        return 'Underweighted'
    elif 18.5 <= BMI < 25:
        return "Normal Weighted"
    elif 25<= BMI < 30:
        return "OverWeighted"
    else:
        return "Obese"
    
def main ():
    try:
        weight = float(input("Enter the Weight in kilograms"))
        Height = float(input("Enter the Height in meters"))

        if weight <= 0 or Height <= 0:
            print("Weight and Height must be a positive numbers. ")
            return
        