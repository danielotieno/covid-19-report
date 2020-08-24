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
    print('---------------WELCOME TO COVID-19 REPORT--------------')
    self.select_country = input('Please select one of the following countries: ---- [Kenya, Rwanda, Uganda, Tanzania, Mauritius] : ')

  def get_all_countries(self):
    if(self.select_country.lower() == 'kenya'):
      return self.get_kenya_data()
    if(self.select_country.lower() == 'rwanda'):
      return self.get_rwanda_data()

  def get_kenya_data(self):
    change_case_to_lower = self.select_country.lower()
    if( change_case_to_lower != 'kenya' or change_case_to_lower == ''):
      print('Invalid input -- Please select the correct country name')
    else:
      kenya_cases = self.covid.get_status_by_country_name("kenya")
      confirmed, active, recovered, deaths = [kenya_cases[k] for k in ('confirmed', 'active', 'recovered', 'deaths')]
      print(f' Total Confirmed cases: {confirmed} \n Total Active cases: {active} \n Total Recovered cases: {recovered} \n Total Deaths: {deaths}')

  def get_rwanda_data(self):
    change_case_to_lower = self.select_country.lower()
    if( change_case_to_lower != 'rwanda' or change_case_to_lower == ''):
      print('Invalid input -- Please select the correct country name')
    else:
      rwanda_cases = self.covid.get_status_by_country_name("rwanda")
      confirmed, active, recovered, deaths = [rwanda_cases[k] for k in ('confirmed', 'active', 'recovered', 'deaths')]
      print(f' Total Confirmed cases: {confirmed} \n Total Active cases: {active} \n Total Recovered cases: {recovered} \n Total Deaths: {deaths}')




def main():
  demo = CovidReport()
  demo.get_all_countries()


if __name__ == "__main__":
  main()


