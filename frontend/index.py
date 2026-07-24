import streamlit as st

import datetime
import requests


st.set_page_config(
    page_title="Devta",
    page_icon="🍕",
    layout="centered"
)
st.title("🍕 DEVTA")

st.markdown(
    "<h4 style='text-align:center; color:#555;'>"
    "Know when your food will arrive."
    "</h4>",
    unsafe_allow_html=True
)

st.write("")

st.markdown("""
<div style="text-align:center; max-width:700px; margin:auto; color:#555;">
Devta predicts your food delivery time using a Machine Learning model
trained on more than <b>40,000</b> real delivery records.
</div>
""", unsafe_allow_html=True)


st.subheader("Fill your delivery details in the below form :")


vehicle_map = {
    "Very Bad": 0,
    "Bad": 1,
    "Good": 2,
    "Excellent": 3
}

with st.form("delivery form"):
    age = st.number_input(
        "Delivery Person Age (18-60)",help="Enter the age of the delivery partner. Valid range: 18 to 60 years.",
        step=1
    )

    rating = st.slider(
        "Delivery ratings",
        min_value=1.0,
        max_value=5.0,
        step=0.1,
        help="The average rating of the delivery person"
    )

    distance = st.number_input("Distance (Km) (Less Than 40 km)",step=0.1,help="Distance of restaurant from your house ")

    weather = st.selectbox("Select the Weather conditions",['Sunny',
            "Cloudy",
            "Windy",
            "Stormy",
            "Fog",
            "Sandstorms"],
        )

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
        ],help="The vehicle condtion of the delivery person"
    )

    order_type = st.selectbox(
        "What's your order type?",
        [
            "Snack",
            "Meal",
            "Drinks",
            "Buffet"
        ],help='Type of food you ordered'
    )

    vehicle_type = st.selectbox(
        "What is the vehicle type? ",
        [
            "motorcycle",
            "scooter",
            "electric_scooter",
            "bicycle"
        ],help="Vehicle type of the delivery person"
    )

    multiple_deliveries = st.segmented_control(
        "Do he have multiple deleveries?",
        [0,1,2,3],default=0,help="The number of orders pending of the delivery person"
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


    if submit:
        data = {
            "age": age,
            "rating": rating,
            "distance": distance,
            "weather": weather,
            "traffic": traffic,
            "vehicle_condition": vehicle_map[vehicle_condition],
            "order_type": order_type,
            "vehicle_type": vehicle_type,
            "multiple_deliveries": multiple_deliveries,
            "festival": festival,
            "city": city,
            "order_time": order_time.strftime("%H:%M"),
            "order_date": order_date.strftime("%d-%m-%Y")

        }

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json = data
        )

        if response.status_code == 200:
            result = response.json()
            with st.container(border=True):

                st.subheader("🍕 Prediction Result")

                st.metric(
                    "Estimated Delivery Time",
                    f"{result['predicted_delivery_time_min']} min"
                )

                st.write(
                    f"Your food is expected to arrive in approximately **{result['predicted_delivery_time_min']} minutes**."
                )

                st.caption(
                    f"Usually takes {result['expected_min']}–{result['expected_max']} minutes."
                )

                with st.expander("💡 Why this estimate?"):
                    for reason in result["reasons"]:
                        st.write(f"• {reason}")
        else:
            st.error(response.text)





st.markdown("""
<style>
    .stApp{
        background: linear-gradient(
            135deg,
            #FFF8F0 0%,
            #FFEFD9 100%
    );
    }
</style>
""", unsafe_allow_html=True)

st.title("🍕 DEVTA")

st.markdown(
    "<h4 style='text-align:center; color:#555;'>"
    "Know when your food will arrive."
    "</h4>",
    unsafe_allow_html=True
)

st.write("")