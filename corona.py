import termplotlib as tpl
from covid import Covid

class CovidReport:
  """

  This is a class that will contain all the methods
  Attributes:
    select_country(string)

  """
  covid = Covid()

  def __init__(self):
    """
    This is a constructor that will ask user to select the want a report from

    Attributes:
      user_input: String

    """
    print('----------------------WELCOME TO COVID-19 REPORT-----------------------------')
    self.select_country = input('Please select one of the following countries: ---- [Kenya, Rwanda, Uganda, Tanzania, Mauritius] : ')

  def get_all_countries(self):
    """
    This is a method that checks user input country and return the data

    """
    if(self.select_country.lower() == 'kenya'):
      return self.get_country_data('kenya')

    if(self.select_country.lower() == 'rwanda'):
      return self.get_country_data('rwanda')

    if(self.select_country.lower() == 'uganda'):
      return self.get_country_data('uganda')

    if(self.select_country.lower() == 'tanzania'):
      return self.get_country_data('tanzania')

    if(self.select_country.lower() == 'mauritius'):
      return self.get_country_data('mauritius')

  def get_data(self, country):
    """
    This is a method that fetch countries data.
    The method returns confirmed, active, recovered, deaths data.

    """
    change_case_to_lower = self.select_country.lower()
    if( change_case_to_lower != country or change_case_to_lower == ''):
      print('Invalid input -- Please select the correct country name')
    else:
      country_cases = self.covid.get_status_by_country_name(country)
      confirmed, active, recovered, deaths = [country_cases[k] for k in ('confirmed', 'active', 'recovered', 'deaths')]
      print(f' Total Confirmed cases: {confirmed} \n Total Active cases: {active} \n Total Recovered cases: {recovered} \n Total Deaths: {deaths}')
    print('-----------------------------------------------------------------')
    descriptive_data = input('Do you want a descriptive report? Press (y/n): ')
    print('-----------------------------------------------------------------')
    if(descriptive_data.lower() == 'y' or descriptive_data == 'yes'):
      active_cases_in_percentage = (active / confirmed) * 100
      recovered_cases_in_percentage = (recovered / confirmed) * 100
      case_fatality_ratio = (deaths / confirmed) * 100
      print(f' Active Cases in %: {active_cases_in_percentage}% \n Recovered Cases in %: {recovered_cases_in_percentage}% \n Fatality Ratio: {case_fatality_ratio}%')

      print('-----------------------------------------------------------------')

      fig = tpl.figure()
      fig.barh(
          [active, confirmed, deaths, recovered],
          ['Active', 'Confirmed', 'Fatality', 'Recovered'],
          force_ascii=True
      )
      fig.show()
    else:
      print('Bye Bye!!! Thank you for checking with us!')

  def get_country_data(self, country):
    """
    This is a method that return Country Covid-19 data

    """
    return self.get_data(country)

def main():
  report = CovidReport()
  report.get_all_countries()


if __name__ == "__main__":
  main()


