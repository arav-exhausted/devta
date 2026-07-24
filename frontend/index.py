import streamlit as st

import datetime



st.set_page_config(
    page_title="Devta",
    page_icon="🍕",
    layout="centered"
)

st.title("🍕 Devta")
st.subheader("Predict your food arrival time")

st.write(
    """
    Devta is a Machine Learning based food delivery time prediction system.
    It is trained on more than 40K samples and uses an XGBoost model to
    estimate the time required for your food to reach your plate.
    """
)



st.subheader("Fill your delivery details in the below form :")


vehicle_map = {
    "Very Bad": 0,
    "Bad": 1,
    "Good": 2,
    "Excellent": 3
}

with st.form("delivery form"):
    age = st.number_input("Delivery Person Age (18-60)")

    rating = st.slider(
        "Delivery ratings",
        min_value=1.0,
        max_value=5.0,
        step=0.1
    )

    distance = st.number_input("Distance (Km) (Less Than 40 km)")

    weather = st.selectbox("Select the Weather conditions",['Sunny',
            "Cloudy",
            "Windy",
            "Stormy",
            "Fog",
            "Sandstorms"])

    traffic = st.selectbox("How's the Traffic ?",
        ["Low",
        "Medium",
        "High",
        "Jam"]
    )

    vehicle_condition = st.selectbox(
        "Vehicle Condition",
        [
            "Very Bad",
            "Bad",
            "Good",
            "Excellent"
        ]
    )

    order_type = st.selectbox(
        "What's your order type?",
        [
            "Snack",
            "Meal",
            "Drinks",
            "Buffet"
        ]
    )

    vehicle_type = st.selectbox(
        "What is the vehicle type? ",
        [
        "Metropolitan",
        "Urban",
        "Semi-Urban"
        ]
    )

    multiple_deliveries = st.segmented_control(
        "Do he have multiple deleveries?",
        [0,1,2,3]
    )

    festival = st.radio(
        "Is there a festival today? ",
        ["Yes","No"],
        horizontal=True
    )

    city = st.selectbox(
        "City Type",
        [
            "Metropolitan",
            "Urban",
            "Semi-Urban"
        ]
    )

    order_hour = st.selectbox(
    "Order Hour",
    list(range(24))
    )

    order_minute = st.selectbox(
        "Order Minute",
        list(range(60))
    )

    order_time = datetime.time(
        hour=order_hour,
        minute=order_minute
    )

    order_date = st.date_input(
        "Order Date",
        datetime.date.today()
    )
    submit = st.form_submit_button("Predict!")




with st.container(border=True):

    st.subheader("🍕 Prediction Result")

    st.metric(
        "Estimated Delivery Time",
        "28 min"
    )

    st.write(
        "Your food is expected to arrive in approximately **28 minutes**."
    )

    st.caption("Usually takes 23–33 minutes.")
    
