import streamlit as st

import datetime
import requests


st.set_page_config(
    page_title="Devta",
    page_icon="ṭ⭐",
    layout="centered"
)



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
st.markdown("""
<h1 style="
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: #FF6B35;
    letter-spacing: 2px;
    margin-bottom: 0;
">
DEVTA
</h1>
""", unsafe_allow_html=True)

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


st.subheader("📝 Delivery Details")


vehicle_map = {
    "Very Bad": 0,
    "Bad": 1,
    "Good": 2,
    "Excellent": 3
}

with st.form("delivery form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Delivery Person Age (18-60)",
            step=1,
            help="Enter the age of the delivery partner. Valid range: 18 to 60 years."
        )

        rating = st.slider(
            "Delivery Ratings",
            min_value=1.0,
            max_value=5.0,
            step=0.1,
            help="The average rating of the delivery person"
        )

        distance = st.number_input(
            "Distance (Km) (Less Than 40 km)",
            step=0.1,
            help="Distance of restaurant from your house"
        )

        weather = st.selectbox(
            "Select the Weather conditions",
            [
                "Sunny",
                "Cloudy",
                "Windy",
                "Stormy",
                "Fog",
                "Sandstorms"
            ]
        )

        traffic = st.selectbox(
            "How's the Traffic ?",
            [
                "Low",
                "Medium",
                "High",
                "Jam"
            ]
        )

        festival = st.radio(
            "Is there a festival today?",
            ["Yes", "No"],
            horizontal=True
        )

    with col2:

        vehicle_condition = st.selectbox(
            "Vehicle Condition",
            [
                "Very Bad",
                "Bad",
                "Good",
                "Excellent"
            ],
            help="The vehicle condition of the delivery person"
        )

        order_type = st.selectbox(
            "What's your order type?",
            [
                "Snack",
                "Meal",
                "Drinks",
                "Buffet"
            ],
            help="Type of food you ordered"
        )

        vehicle_type = st.selectbox(
            "What is the vehicle type?",
            [
                "motorcycle",
                "scooter",
                "electric_scooter",
                "bicycle"
            ],
            help="Vehicle type of the delivery person"
        )

        multiple_deliveries = st.segmented_control(
            "Do he have multiple deliveries?",
            [0, 1, 2, 3],
            default=0,
            help="The number of orders pending of the delivery person"
        )

        city = st.selectbox(
            "City Type",
            [
                "Metropolitan",
                "Urban",
                "Semi-Urban"
            ]
        )

    st.markdown("##### 🕒 Order Time")

    time_col1, time_col2 = st.columns(2)

    with time_col1:
        order_hour = st.selectbox(
            "Order Hour",
            list(range(24))
        )

    with time_col2:
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

    submit = st.form_submit_button(
        "🚀 Predict Delivery Time",
        use_container_width=True
    )

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
            st.error("Couldn't generate prediction. Please check your inputs or try again.")



st.markdown("""
<style>

.stApp{
    background: #FFF8F0;
}


div[data-testid="stForm"]{
    background: #FFE8CC;
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #FFD3A4;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

div[data-testid="stVerticalBlockBorderWrapper"]{
    background: #FFD9B3;
    border-radius: 18px;
    border: 1px solid #FFC58A;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.stButton > button{
    background: #FF6B35;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 17px; 
    transition: 0.25s ease;
}

.stButton > button:hover{
    background: #E85D2A;
    transform: scale(1.02);
}


input,
textarea{
    border-radius: 10px !important;
}


div[data-baseweb="select"]{
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align:center; color:#6B7280; padding:10px;">

<p style="font-size:16px;">
<i>Because waiting is hard enough.</i>
</p>

<p style="font-size:14px;">
Made with ❤️ by <b>Arav</b>
</p>

</div>
""", unsafe_allow_html=True)