import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('curso_de_python_avanzado/006-graficas_en_python/app2/data.csv')
    data = list(filter(lambda item : item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.genereate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()