def cal_BMI(h,w):
    bmi = w/(h**2)
    return bmi

def main():

    h = float(input("Enter your heigthin meters:"))

    w = float(input("Enter your weight in kg:"))

    bmi = cal_BMI(h,w)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("Your weight is normal.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()
