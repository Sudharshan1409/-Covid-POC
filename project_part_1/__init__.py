def find_top_confirmed(n = 15):
    
  import pandas as pd
  corona_df = pd.read_csv('project_part_1/dataset1.csv')
  by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
  cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
  return cdf

import folium
import pandas as pd
corona_df = pd.read_csv('project_part_1/dataset1.csv')

corona_df=corona_df.dropna()

m=folium.Map(location=[34.223334,-82.461707],
            tiles='Stamen toner',
            zoom_start=8)

def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2])*10,
                 color="red",
                 popup='{}\n confirmed cases:{}'.format(x[3],x[2])).add_to(m)
corona_df[['Lat','Long_','Confirmed','Combined_Key']].apply(lambda x:circle_maker(x),axis=1)

html_map=m._repr_html_()
from flask import render_template, Blueprint
part1 = Blueprint('part1', __name__,
                        template_folder='templates')
@part1.route('/part1')
def home():
    cdf = find_top_confirmed()
    return render_template("home.html",table=cdf, cmap=html_map,pairs=[(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])])
