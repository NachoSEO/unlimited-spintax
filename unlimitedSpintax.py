import spintax
import pandas as pd
#from google.colab import files

def spin(string, repeat):
  text_spinned = []
  
  for i in range(repeat):
    spin = (spintax.spin(string))
    text_spinned.append(spin)
  
  df = pd.DataFrame({
    "text":text_spinned 
  })
  
  df.to_csv("spinned_texts.csv")
  #files.download("spinned_texts.csv")

text = "{Writing|Creating} {articles|stories} is a {lot of fun|rewarding experience}." #Sample text
spin(text,5)
