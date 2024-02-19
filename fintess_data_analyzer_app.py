def calculate_bmi(weight, height):  # The most important functions in this program alongside with the main function.
    """Calculate the Body Mass Index (BMI)."""
    body_mass_index = weight / height ** 2  # a.k.a. BMI

    return body_mass_index


def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""

    burned_calories_per_minute = 6.67  # This is just an average statistic.
    estimated_burned_calories = burned_calories_per_minute * duration

    return estimated_burned_calories


def filter_underweight_people(people_data):
    """Filter underweight people based on BMI."""
    underweight_people = []

    for person in people_data:
        BMI = calculate_bmi(person['weight'], person['height'])  # Body mass index. Calls the function "calculate_bmi".

        # People that have a BMI lower than 18.5 are considered underweight.
        if BMI < 18.5:
            underweight_people.append(person)

    return underweight_people


def filter_normal_weight_people(people_data):
    """Filter normal weight people based on BMI."""
    normal_weight = []

    for person in people_data:
        BMI = calculate_bmi(person['weight'], person['height'])  # Body mass index. Calls the function "calculate_bmi".

        # People that have a BMI greater than or equal to 18.5 and under 25 are considered overweight
        if 18.5 <= BMI < 25:
            normal_weight.append(person)

    return normal_weight


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []

    for person in people_data:
        BMI = calculate_bmi(person['weight'], person['height'])  # Body mass index. Calls the function "calculate_bmi".

        # People that have a BMI greater or equal to 25 and under 30 are considered overweight.
        if 25 <= BMI < 30:
            overweight_people.append(person)

    return overweight_people


def filter_obese_people(people_data):
    """Filter overweight people based on BMI."""
    obese_people = []

    for person in people_data:
        BMI = calculate_bmi(person['weight'], person['height'])  # Body mass index. Calls the function "calculate_bmi".

        # People that have a BMI greater or equal to 30 are considered obese.
        if BMI >= 30:
            obese_people.append(person)

    return obese_people


# Main program

def main():
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    print()

    while True:
        name = input("Enter person's name: ").strip()

        if not name:
            break

        weight = float(input("Enter person's weight in kilograms: "))
        height = float(input("Enter person's height in meters: "))
        duration = float(input("Enter exercise duration in minutes: "))
        person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}

        people_data.append(person)
        print()  # For more readability in the console.

    print("\nFitness Analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        calories_burned = calculate_calories_burned(person['duration'])

        print(f"{person['name']}: BMI = {bmi:.1f}, Calories burned(average) = {calories_burned}")

    underweight_people = filter_underweight_people(people_data)
    normal_weight_people = filter_normal_weight_people(people_data)
    overweight_people = filter_overweight_people(people_data)
    obese_people = filter_obese_people(people_data)

    print("\nUnderweight People:")
    for person in underweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])

        print(f"{person['name']}: BMI = {bmi:.1f}")

    print("\nNormal weight People:")
    for person in normal_weight_people:
        bmi = calculate_bmi(person['weight'], person['height'])

        print(f"{person['name']}: BMI = {bmi:.1f}")

    print("\nOverweight People:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])

        print(f"{person['name']}: BMI = {bmi:.1f}")

    print("\nObese People:")
    for person in obese_people:
        bmi = calculate_bmi(person['weight'], person['height'])

        print(f"{person['name']}: BMI = {bmi:.1f}")


if __name__ == "__main__":
    main()
