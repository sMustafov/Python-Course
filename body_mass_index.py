def body_mass_index(weight, height):
    return weight / (height ** 2)

def shape_of(weight, height):
    bmi = body_mass_index(weight, height)
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi > 18.5 and bmi <= 25:
        return 'Healthy weight'
    elif bmi > 25 and bmi <= 30:
        return 'Overweight'
    elif bmi > 30 and bmi <= 35:
        return 'Obesity I'
    elif bmi > 35 and bmi <= 40:
        return 'Obesity II'
    elif bmi > 40:
        return 'Extreme Obesity'
