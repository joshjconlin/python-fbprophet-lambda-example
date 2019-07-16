import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('./examples/example_wp_log_peyton_manning.csv')
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

forecast.to_csv("./output/peyton_manning.csv", encoding='utf-8', index=False)

# def my_handler(event, context):
#     message = 'Hello world!'
#     return {
#         'message': message
#     }

# to run
# docker run --rm -it -v /Users/joshconlin/development/prophet-lambda:/var/task lambci/lambda:build-python3.6 bash
# . venv/bin/activate
