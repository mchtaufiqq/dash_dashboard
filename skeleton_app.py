
# import library disini 
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# masukan semua data wrangling disini 
acc_reach = pd.read_csv('data_input/reach.csv', parse_dates=True)
acc_reach['date'] = acc_reach['date'].astype('datetime64')

content = pd.read_csv('data_input/content.csv')
content['post_time'] = content['post_time'].astype('datetime64')
content['posted_hour'] = content['post_time'].dt.hour
content_hour = content.groupby('posted_hour').mean()
content_hour = content_hour.reset_index()

# sampai disini data wranggiling 

app.title = "Dashboard Social Media Analytics"

app.layout = html.Div(
    children=[
        html.Div(
            className="header",
            children=[
                html.H1(children = "Social Media Analytics",
                className = "header-title"),
                html.P(children = "Dashboard ini untuk menganalisa instagram dan facebook "
                ""
                "dari akun PT XYZ"
                ""
                ""
                , className = "header-description")


            ]
        ),

        html.Div(
            className="wrapper",
            children=[
                # ini untuk isi body 
                html.Div(children = [
                    dcc.Graph(figure = px.line(acc_reach,
                                        x="date", 
                                        y=["facebook","instagram"],
                                        title= "reach instagram dan facebook"),
                                        id = "reach"
                                        )
                    ],
                    className = "card"
                ),
                html.Div(children = [
                    dcc.Graph(figure = px.bar(content_hour,x="posted_hour", y = "reach"),
                                        id = "hours"
                                )   
                    ],
                    className = "card"
                )
            ],
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)