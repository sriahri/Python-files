if __name__ == '__main__':
    countries = []
    cities = []
    temperatures = []
    country_name = ""
    while country_name != "-1":
        country_name = input("Enter the country name: ")
        if country_name != "-1":
            countries.append(country_name)
        else:
            break
        city_name = ""
        temp = []
        while city_name != "-1":
            city_name = input("Enter the city name: ")
            if city_name != "-1":
                temp.append(city_name)
            else:
                break
            temperature = 0
            temp_temp = []
            while temperature != -1:
                temperature = int(input("Enter the temperature: "))
                if temperature != -1:
                    temp_temp.append(temperature)
            temperatures.append(temp_temp)
        cities.append(temp)
    total, count = 0, 0
    print(temperatures)
    print(cities)
    print(countries)
    for i in range(len(countries)):
        for j in range(len(cities[i])):
            total += sum(temperatures[i])
            count += len(temperatures[i])

    print("The average is {}".format(total / count))
