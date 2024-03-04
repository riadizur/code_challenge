# Load necessary libraries
library(forecast) # for time series forecasting
library(ggplot2)  # for data visualization

# Read the preprocessed data
sales_data <- read.csv("sales_data.csv")

# Convert the date column to a Date object
sales_data$date <- as.Date(sales_data$date)

# Convert data to a time series object
sales_ts <- ts(sales_data$sales, frequency = 7) # assuming weekly data

# Plot the time series data
autoplot(sales_ts) + labs(title = "Weekly Sales Data")

# Train-test split
train_percentage <- 0.8
train_size <- floor(train_percentage * length(sales_ts))
train <- window(sales_ts, end = train_size)
test <- window(sales_ts, start = train_size + 1)

# ARIMA model fitting
arima_model <- auto.arima(train)

# Forecasting
forecast_values <- forecast(arima_model, h = length(test))

# Plotting the forecast
autoplot(forecast_values) + labs(title = "Sales Forecast")

# Evaluation
accuracy(forecast_values, test)

# Deployment: You can use the trained model to forecast sales for future periods.
