import streamlit as st
import pandas as pd

listings = pd.read_csv('data:sample_listings.csv', skiprows=1)
waitlist = pd.read_csv('data:wa_waitlist.csv', skiprows=1)
df = pd.merge(listings, waitlist, on="suburb")

st.title("Housing Affordability Analysis")
st.write("A simple application to analyze housing affordability in WA based on rental prices and waitlist data.")


# Budget filter
budget = st.slider("Max rent per week", 200, 500, 350)
filtered = df[df['price_weekly'] <= budget]

st.subheader("Listings under budget")
st.table(filtered)

# Most affordable suburbs
best = filtered.sort_values(by='price_weekly').head(5)
if not best.empty:
    st.success(f"Most affordable suburb: {best.iloc[0]['suburb']} with average rent ${best.iloc[0]['price_weekly']}/week")
