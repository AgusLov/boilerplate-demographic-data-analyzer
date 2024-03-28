# Importa la librería pandas

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leer los datos desde un archivo CSV
    df = pd.read_csv('adult.data.csv')
    # Número de personas de cada raza
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Porcentaje de personas con título de Bachiller
    percentage_bachelors = round(len(df[df['education']== 'Bachelors'])/len(df['education'])*100, 1)
    

    # Porcentaje de personas con educación avanzada (Bachiller, Maestría o Doctorado) que ganan más de $50K
    # Porcentaje de personas sin educación avanzada que ganan más de $50K
    
    # Con y sin Bachiller, Maestría u Doctorado
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Porcentaje con salario >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # Cantidad mínima de horas que una persona trabaja a la semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de personas que trabajan el mínimo de horas y ganan >50K
    num_min_workers = df[df['hours-per-week']==min_work_hours]

    rich_percentage =  round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # País con mayor porcentaje de personas que ganan >50K
    count_country = df['native-country'].value_counts()
    rich_country_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    
    highest_earning_country = (rich_country_count/count_country*100).idxmax()
    
    highest_earning_country_percentage = round((rich_country_count/count_country*100).max(),1)

    # Ocupaciones más populares en la India para personas que ganan >50K
    rich_indians = df[(df['native-country']=='India')  & (df['salary']=='>50K')]
    
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()



    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
