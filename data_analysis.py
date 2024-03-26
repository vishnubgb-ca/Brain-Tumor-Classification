from data_extraction import extract_data

def analyse():
   try:
      url = extract_data()
      print(url)
   except:
      print("Error")

analyse()
