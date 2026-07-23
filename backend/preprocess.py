import joblib
import pandas as pd


feature_columns = joblib.load("../model/feature_columns.pkl")


def preprocess(data: dict):

    df = pd.DataFrame([data])

    df = df.rename(columns={
        "age": "Delivery_person_Age",
        "rating": "Delivery_person_Ratings",
        "distance": "Distance_Km",
        "weather": "Weatherconditions",
        "traffic": "Road_traffic_density",
        "vehicle_condition": "Vehicle_condition",
        "order_type": "Type_of_order",
        "vehicle_type": "Type_of_vehicle",
        "festival": "Festival",
        "city": "City",
        "order_time": "Order_time",
        "order_date": "Order_Date"
    })



    date = pd.to_datetime(
        df["Order_Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    df["Day_of_Week"] = date.dt.day_name()

    df["Is_Weekend"] = (
        date.dt.dayofweek >= 5
    ).astype(int)

    df["Order_time"] = pd.to_datetime(
    df["Order_time"],
    format="%H:%M"
)

    df["Order_time"] = (
        df["Order_time"].dt.hour +
        df["Order_time"].dt.minute / 60
    )

    df.drop(
        columns=["Order_Date"],
        inplace=True
    )



    df["Peak_hour"] = (
        df["Order_time"].between(12,14) |
        df["Order_time"].between(19,21)
    ).astype(int)


    df["Long_Distance"] = (
        df["Distance_Km"] > 10
    ).astype(int)


    df["Late_Night_Order"] = (
        (df["Order_time"] >= 22) |
        (df["Order_time"] <= 5)
    ).astype(int)


    df["Highly_Rated_Driver"] = (
        df["Delivery_person_Ratings"] >= 4.5
    ).astype(int)


    df["Busy_Rider"] = (
        df["multiple_deliveries"] >= 2
    ).astype(int)


    categorical_cols = [
        "Weatherconditions",
        "Road_traffic_density",
        "Type_of_order",
        "Type_of_vehicle",
        "Festival",
        "City",
        "Day_of_Week"
    ]


    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True,
        dtype=int
    )



    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0


    df = df[feature_columns]


    return df
