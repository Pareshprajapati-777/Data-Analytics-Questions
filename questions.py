import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

# python -m streamlit run questions.py
st.set_page_config(page_title="Pandas Questions Solver", page_icon="🐼", layout="wide")

st.sidebar.title("Pandas Questions Solver 🐼")



Q = [
    "--  select  --",
    "Q1.  Remove Null rows ",
    "Q2.  Remove rows only if ALL values are NaN",
    "Q3.  Drop NULL columns",
    "Q4.  Remove outliers",
    "Q5.  Remove duplicates & Reset index",
    "Q6.  Remove mpg & cylinders columns",
    "Q7.  Heights Weights Analysis",
    "Q8.  IPL Analysis",
    "Q9.  Spotify Analysis",
    "Q10. Car Dataset Analysis",
    "Q11. data_result.csv Analysis",
    "Q12. Movies Analysis",
    "Q13. IPL Advanced Analysis",
    "Q14. Sort Employees",
    "Q15. Apply & Grade Column",
    "Q16. Replace Absent with 0",
    "Q17. Concatenate & Outer Join",
    "Q18. Outer Merge with Indicator",
    "Q19. GroupBy Dept - Mean/Median/Max",
    "Q20. Range per Team using GroupBy",
    "Q21. Detect & Remove Outliers (IQR)",
    "Q22. Unique Cities & Random Employee per Dept",
    "Q23. TotalAmount Column & Sort",
    "Q24. GroupBy Dept - Total & Avg Salary",
    "Q25. Employees per Dept & Max Experience",
    "Q26. House Data Analysis (kc_house_data.csv)",
    "Q27. Supermarket Sales Analysis",
]

search = st.sidebar.text_input(
    "🔍 Search Question",
    placeholder="Q10, IPL, Spotify..."
)

filtered_questions = [
    q for q in Q
    if search.lower() in q.lower()
]

Q = st.sidebar.selectbox(
    "Select Question",
    filtered_questions if filtered_questions else Q
)

if Q == "--  select  --":
    st.title("Data Analysis Question Solver 📈")
    tab1 , tab2 = st.tabs(["features","About me"])
    with tab1:
        st.markdown("""
        <div style="
        padding:15px;
        border-radius:10px;
        background: linear-gradient(90deg, #0f0c29, #302b63, #24243e);
        color:white;
        text-align:center;
        margin-bottom:30px;
        ">
        <h2>🐍 Question Solver Dashboard</h2>
        <p>Interactive Data Science & Pandas Practical Solutions</p>
        </div>
        """,unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)

        col1.markdown("""
        <div style="background:#1b1b3a; border:1px solid #4f46e5; text-align:center;">
        <h3>📚 27+</h3>
        <p>Questions</p>
        </div>
        """, unsafe_allow_html=True)

        col2.markdown("""
        <div style="background:#1b1b3a; border:1px solid #4f46e5; text-align:center;">
        <h3>📂 10+</h3>
        <p>Datasets</p>
        </div>
        """, unsafe_allow_html=True)

        col3.markdown("""
        <div style="background:#1b1b3a; border:1px solid #4f46e5; text-align:center;">
        <h3>🐼 4+</h3>
        <p>Libraries</p>
        </div>
        """, unsafe_allow_html=True)

        col4.markdown("""
        <div style="background:#1b1b3a; border:1px solid #4f46e5; text-align:center;">
        <h3>📈 12+</h3>
        <p>Charts</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        st.subheader("🛠 Technologies Used")
        st.markdown("""
        ✅ Python        
        ✅ Streamlit
        """)
        st.markdown("---")
        st.subheader("🐼 Libraries")
        st.markdown("""
        ✅ Pandas        ✅ NumPy    ✅ Matplotlib✅ Seaborn  
        """)
        st.divider()
        st.markdown("""
        ### 🚀 Features

        ✅ Data Cleaning  
        ✅ Outlier Detection  
        ✅ IPL Analysis  
        ✅ Spotify Analysis  
        ✅ Car Dataset Analysis  
        ✅ Interactive Dashboard  
        ✅ Dataset Upload Support
        """)

    with tab2:
        st.markdown("""
        <div style="text-align:left;">
            <img src="https://github.com/Pareshprajapati-777.png"
                style="
                    width:140px;
                    height:140px;
                    border-radius:50%;
                    object-fit:cover;
                    border:4px solid #60a5fa;
                    box-shadow:0 0 25px rgba(59,130,246,0.6);
                    margin-bottom:30px;
                ">
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="
        background:linear-gradient(135deg,#0f172a,#1e293b);
        padding:30px;
        border-radius:15px;
        color:white;
        ">
        
        <h1>👨‍💻 Paresh Prajapati</h1>
        
        <h4>BSc IT Student | Data Science Enthusiast | Future Data Analyst</h4>

        <p>
        I am currently pursuing <b>BSc IT at Swarnim University</b> and have a strong interest
        in <b>Data Science, Artificial Intelligence, Machine Learning, and Python Development</b>.
        </p>

        <p>
        I enjoy working with real-world datasets, building interactive dashboards,
        performing data analysis, and creating projects that solve practical problems.
        </p>

        <p>
        My goal is to start my career in the field of Data Science and Analytics,
        where I can apply my technical skills and continuously learn new technologies.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.subheader("🚀 Skills")
        st.markdown("""
        ✅ Python
        ✅ Pandas
        ✅ NumPy
        ✅ Matplotlib
        ✅ Seaborn
        ✅ Streamlit
        ✅ C & C++
        ✅ Data Analysis
                    
        ✅ Machine Learning Basics
        """)

        st.divider()

        st.subheader("🎯 Career Objective")

        st.info("""
        Seeking opportunities in Data Science, Data Analytics,
        and Python Development where I can contribute my skills,
        gain industry experience, and grow as a technology professional.
        """)

        st.divider()

        st.subheader("🌐 Connect With Me")

        st.markdown("""
        🔗 GitHub: https://github.com/Pareshprajapati-777

        💼 LinkedIn: https://www.linkedin.com/in/pareshprajapati-co

        📧 Email: pareshprajapati999b@gmail.com
        """)

elif Q == "Q1.  Remove Null rows ":
    st.subheader("Q1. Create a DataFrame and remove all rows containing at least one NaN value")

    data = {"Name": ["Deepak", "Meet", np.nan, "Pritam"],
            "Age":  [20, np.nan, 21, 30],
            "sem":  [5, 6, 8, 6]}
    df = pd.DataFrame(data)
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    clean = df.dropna()
    st.subheader("DataFrame after removing Null rows")
    st.dataframe(clean)

    if st.checkbox("Show Code", key="q1"):
        st.code("""
data = {"Name": ["Deepak", "Meet", np.nan, "Pritam"],
        "Age":  [20, np.nan, 21, 30],
        "sem":  [5, 6, 8, 6]}
df = pd.DataFrame(data)
df.dropna()
        """)


elif Q == "Q2.  Remove rows only if ALL values are NaN":
    st.subheader("Q2. Remove rows only if ALL of their values are NaN")

    data = {"Name": ["Deepak", np.nan, np.nan, "Pritam"],
            "Age":  [20, np.nan, 21, 30],
            "sem":  [6, np.nan, 2, 3]}
    df = pd.DataFrame(data)
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    clean = df.dropna(how="all")
    st.subheader("DataFrame after removing rows with all NaN values")
    st.dataframe(clean)

    if st.checkbox("Show Code", key="q2"):
        st.code("""
df.dropna(how='all')
        """)


elif Q == "Q3.  Drop NULL columns":
    st.subheader("Q3. Drop all columns that contain at least one NaN")

    data = {"Name": ["Deepak", "Meet", "", "Pritam"],
            "Age":  [20, np.nan, 21, 30],
            "sem":  [6, 2, 2, 3]}
    df = pd.DataFrame(data)
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    clean = df.dropna(axis=1)
    st.subheader("DataFrame after dropping columns with any NaN values")
    st.dataframe(clean)

    if st.checkbox("Show Code", key="q3"):
        st.code("""
df.dropna(axis=1)
        """)

elif Q == "Q4.  Remove outliers":
    st.subheader("DataFrame with outliers")

    data={"Name":["Paresh","Meet","Pritam","Rahul"],
    "Age":[20,22,21,100],
    "sem":[6,2,2,3]}
    df = pd.DataFrame(data)
    st.dataframe(df)

    Q1 = df['Age'].quantile(0.25)
    Q3 = df['Age'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - (1.5 * IQR)
    upper = Q3 + (1.5 * IQR)
    clean = df[(df['Age'] >= lower) & (df['Age'] <= upper)]

    st.subheader("DataFrame after removing outliers")
    st.dataframe(clean)            
    if st.checkbox("Show_Code", key="q4"):
        st.code("""
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)
clean = df[(df['Age'] >= lower) & (df['Age'] <= upper)]
        """)


elif Q == "Q5.  Remove duplicates & Reset index":
    st.subheader("Q5. Remove duplicate rows and reset the index")

    data = {
        "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
        "B": [50, 40, 40, 30, 50],
        "C": [True, False, False, False, True]
    }
    df = pd.DataFrame(data)
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    st.write(f"**Duplicate count:** `{df.duplicated().sum()}`")

    clean = df.drop_duplicates().reset_index(drop=True)
    st.write("**After `drop_duplicates().reset_index(drop=True)`:**")
    st.dataframe(clean)

    if st.checkbox("Show Code", key="q5"):
        st.code("""
df.duplicated().sum()                        # count duplicates
df.drop_duplicates().reset_index(drop=True)  # remove & reset
        """)


elif Q == "Q6.  Remove mpg & cylinders columns":
    st.subheader("Q6. Drop 'mpg' and 'cylinders' columns from auto-mpg dataset")

    data = st.file_uploader("Upload auto-mpg.csv", type=["csv"])
    if data is not None and data.name == "auto-mpg.csv":
        df = pd.read_csv(data)
        st.write("**Original DataFrame:**")
        st.dataframe(df)

        clean = df.drop(columns=["mpg", "cylinders"])
        st.write("**After dropping 'mpg' and 'cylinders':**")
        st.dataframe(clean)

    elif data is not None and data.name != "auto-mpg.csv":
        st.error("Please upload the correct file: auto-mpg.csv")

    if st.checkbox("Show Code", key="q6"):
        st.code("""
df.drop(columns=['mpg', 'cylinders'])
        """)


elif Q == "Q7.  Heights Weights Analysis":
    st.subheader("Q7. Heights & Weights Analysis (heights_weights.csv)")
    data = st.file_uploader("Upload heights_weights.csv", type=["csv"])
    if data is not None and data.name == "heights_weights.csv":
        df = pd.read_csv(data)

        with st.expander("1. Convert to DataFrame"):
            st.dataframe(df)
            if st.checkbox("Show Code", key="q7_1"):
                st.code("df = pd.read_csv('heights_weights.csv')")

        with st.expander("2. Basic info (memory & data types)"):
            buf = io.StringIO()
            df.info(buf=buf)
            st.text(buf.getvalue())
            if st.checkbox("Show Code", key="q7_2"):
                st.code("df.info()")

        with st.expander("3. Basic statistics"):
            st.dataframe(df.describe())
            if st.checkbox("Show Code", key="q7_3"):
                st.code("df.describe()")

        with st.expander("4. Correlation table — Height vs Weight"):
            corr = df.corr(numeric_only=True)
            st.dataframe(corr)
            val = corr.loc["Height", "Weight"]
            st.write(f"**Correlation (Height ↔ Weight) = {val:.3f}**")
            if val > 0.7:
                st.success("Strong Positive Correlation")
            elif val > 0.3:
                st.info("Moderate Positive Correlation")
            else:
                st.warning("Weak Correlation")
            if st.checkbox("Show Code", key="q7_4"):
                st.code("df.corr(numeric_only=True)")

        with st.expander("5. Outlier detection (Boxplot)"):
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df[["Height", "Weight"]], ax=ax)
            ax.set_title("Boxplot of Height and Weight")
            st.pyplot(fig)
            plt.close()
            st.info("Points outside the whiskers represent outliers.")
            if st.checkbox("Show Code", key="q7_5"):
                st.code("""
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(data=df[["Height","Weight"]], ax=ax)
                """)
    elif data is not None and data.name != "heights_weights.csv":
        st.error("Please upload the correct file: heights_weights.csv")


elif Q == "Q8.  IPL Analysis":
    st.subheader("Q8. IPL Matches Analysis (ipl-matches.csv — 2008 to 2022)")
    data = st.file_uploader("Upload ipl-matches.csv", type=["csv"])
    if data is not None and data.name == "ipl-matches.csv":
        df = pd.read_csv(data)
        buf = io.StringIO(); df.info(buf=buf)
        with st.expander("Dataset Info"):
            st.text(buf.getvalue())

        with st.expander("1. Matches gone in Super Over"):
            st.dataframe(df[df["SuperOver"] == "Y"])
            if st.checkbox("Show Code", key="q8_1"):
                st.code('df[df["SuperOver"] == "Y"]')

        with st.expander("2. Matches won by Kolkata Knight Riders at Kolkata"):
            count = df[(df["City"] == "Kolkata") & (df["WinningTeam"] == "Kolkata Knight Riders")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q8_2"):
                st.code('df[(df["City"]=="Kolkata") & (df["WinningTeam"]=="Kolkata Knight Riders")].shape[0]')

        with st.expander("3. Matches where MS Dhoni is Player of Match vs Mumbai Indians"):
            count = df[(df["Player_of_Match"] == "MS Dhoni") & (df["Team2"] == "Mumbai Indians")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q8_3"):
                st.code('df[(df["Player_of_Match"]=="MS Dhoni") & (df["Team2"]=="Mumbai Indians")].shape[0]')

        with st.expander("4. Gujarat Titans won Toss, elected to Bat, and won the match"):
            count = df[(df["TossWinner"] == "Gujarat Titans") & (df["TossDecision"] == "bat") & (df["WinningTeam"] == "Gujarat Titans")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q8_4"):
                st.code("""
df[(df["TossWinner"]=="Gujarat Titans") &
   (df["TossDecision"]=="bat") &
   (df["WinningTeam"]=="Gujarat Titans")].shape[0]
                """)

        with st.expander("5. All matches won by Gujarat Titans"):
            st.dataframe(df[df["WinningTeam"] == "Gujarat Titans"])
            if st.checkbox("Show Code", key="q8_5"):
                st.code('df[df["WinningTeam"] == "Gujarat Titans"]')
    elif data is not None and data.name != "ipl-matches.csv":
        st.error("Please upload the correct file: ipl-matches.csv")


elif Q == "Q9.  Spotify Analysis":
    st.subheader("Q9. Spotify Dataset Analysis (spotify.csv)")
    data = st.file_uploader("Upload spotify.csv", type=["csv"])
    if data is not None and "spotify" in data.name.lower():
        df = pd.read_csv(data)

        with st.expander("1. Convert to DataFrame"):
            st.dataframe(df)
            if st.checkbox("Show Code", key="q9_1"):
                st.code("df = pd.read_csv('spotify.csv')")  
        with st.expander("2. Basic info"):
            buf = io.StringIO(); df.info(buf=buf); st.text(buf.getvalue())
            if st.checkbox("Show Code", key="q9_2"):
                st.code("""
df.info()
                """)
        with st.expander("3. Basic statistics"):
            st.dataframe(df.describe())
            if st.checkbox("Show Code", key="q9_3"):
                st.code("""
df.describe()
                """)
        with st.expander("4. Correlation — danceability vs energy"):
            corr = df.corr(numeric_only=True)
            st.dataframe(corr)
            val = corr.loc["danceability", "energy"]
            st.write(f"**Correlation (danceability ↔ energy) = {val:.3f}**")
            if st.checkbox("Show Code", key="q9_4"):
                st.code("""
df.corr(numeric_only=True)
                """)        
        with st.expander("5. First 5 rows"):
            st.dataframe(df.head(5))
            if st.checkbox("Show Code", key="q9_5"):
                st.code("""
df.head(5)  
                """)                         
        with st.expander("6. Last 5 rows"):
            st.dataframe(df.tail(5))
            if st.checkbox("Show Code", key="q9_6"):
                st.code("""
df.tail(5)  
                """)
        with st.expander("7. Rows 15 to 39 (iloc[15:40])"):
            st.dataframe(df.iloc[15:40])
            if st.checkbox("Show Code", key="q9_7"):
                st.code(""" 
df.iloc[15:40]
                """)
        with st.expander("8. Last 5 rows — last 5 columns"):
            st.dataframe(df.tail(5).iloc[:, -5:])
            if st.checkbox("Show Code", key="q9_8"):
                st.code("""
df.tail(5).iloc[:, -5:]
                """)

        with st.expander("9. Shape of dataset"):
            st.write(f"**Rows × Columns:** `{df.shape}`")
            if st.checkbox("Show Code", key="q9_9"):
                st.code("""
df.shape
                """)
        with st.expander("10. Missing values"):
            st.dataframe(df.isna().sum().rename("Missing Count"))
            if st.checkbox("Show Code", key="q9_10"):
                st.code("""
df.isna().sum()
                """)
        with st.expander("11. Outliers in 'popularity' (IQR)"):
            q3 = df["popularity"].quantile(0.75)
            q1 = df["popularity"].quantile(0.25)
            iqr = q3 - q1
            upper = q3 + (iqr * 1.5)
            lower = q1 - (iqr * 1.5)
            outliers = df[(df["popularity"] > upper) | (df["popularity"] < lower)]
            st.write(f"**Outliers count:** {len(outliers)}")
            st.dataframe(outliers)
            if st.checkbox("Show Code", key="q9_11"):
                st.code("""
q3 = df["popularity"].quantile(0.75)
q1 = df["popularity"].quantile(0.25)
iqr = q3 - q1
upper = q3 + (iqr * 1.5)
lower = q1 - (iqr * 1.5)
outliers = df[(df["popularity"] > upper) | (df["popularity"] < lower)]
                """)
        with st.expander("12. Crosstab: time_signature vs track_genre"):
            st.dataframe(pd.crosstab(df["time_signature"], df["track_genre"]))
            if st.checkbox("Show Code", key="q9_12"):
                st.code(""" 
pd.crosstab(df["time_signature"], df["track_genre"])
                """)
    elif data is not None and data.name != "spotify.csv":
        st.error("Please upload the correct file: spotify.csv")

elif Q == "Q10. Car Dataset Analysis":
    st.subheader("Q10. Car Dataset Analysis (car data.csv)")
    data = st.file_uploader("Upload 'car data.csv'", type=["csv"])
    if data is not None and "car" in data.name.lower():
        df = pd.read_csv(data)
        st.dataframe(df)

        with st.expander("1. Ritz cars with Kms_Driven > 30,000"):
            count = df[(df["Car_Name"] == "ritz") & (df["Kms_Driven"] > 30000)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_1"):
                st.code('df[(df["Car_Name"]=="ritz") & (df["Kms_Driven"]>30000)].shape[0]')

        with st.expander("2. Petrol cars of year 2017 with Selling_Price > 10 Lakhs"):
            count = df[(df["Fuel_Type"] == "Petrol") & (df["Year"] == 2017) & (df["Selling_Price"] > 10)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_2"):
                st.code('df[(df["Fuel_Type"]=="Petrol") & (df["Year"]==2017) & (df["Selling_Price"]>10)].shape[0]')

        with st.expander("3. Swift cars with Selling_Price < 4 Lakhs"):
            count = df[(df["Car_Name"] == "swift") & (df["Selling_Price"] < 4)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_3"):
                st.code('df[(df["Car_Name"]=="swift") & (df["Selling_Price"]<4)].shape[0]')

        with st.expander("4. Automatic Petrol cars of 2015 with Selling_Price > 10 Lakhs"):
            count = df[(df["Transmission"] == "Automatic") & (df["Fuel_Type"] == "Petrol") & (df["Year"] == 2015) & (df["Selling_Price"] > 10)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_4"):
                st.code("""
df[(df["Transmission"]=="Automatic") & (df["Fuel_Type"]=="Petrol") &
   (df["Year"]==2015) & (df["Selling_Price"]>10)].shape[0]
                """)

        with st.expander("5. Automatic vehicles with Selling_Price < 1 Lakh"):
            result = df[(df["Transmission"] == "Automatic") & (df["Selling_Price"] < 1)]
            st.dataframe(result)
            if st.checkbox("Show Code", key="q10_5"):
                st.code('df[(df["Transmission"]=="Automatic") & (df["Selling_Price"]<1)]')

        with st.expander("6. Petrol cars with Kms_Driven > 50,000 and Year 2010–2015"):
            count = df[(df["Fuel_Type"] == "Petrol") & (df["Kms_Driven"] > 50000) & (df["Year"] >= 2010) & (df["Year"] <= 2015)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_6"):
                st.code("""
df[(df["Fuel_Type"]=="Petrol") & (df["Kms_Driven"]>50000) &
   (df["Year"]>=2010) & (df["Year"]<=2015)].shape[0]
                """)

        with st.expander("7. Cars where Present_Price - Selling_Price > 15"):
            count = df[df["Present_Price"] - df["Selling_Price"] > 15].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_7"):
                st.code('df[df["Present_Price"] - df["Selling_Price"] > 15].shape[0]')

        with st.expander("8. Petrol cars with Kms_Driven < 5000 & Selling_Price < 0.5"):
            count = df[(df["Fuel_Type"] == "Petrol") & (df["Kms_Driven"] < 5000) & (df["Selling_Price"] < 0.5)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q10_8"):
                st.code("""
df[(df["Fuel_Type"]=="Petrol") & (df["Kms_Driven"]<5000) &
   (df["Selling_Price"]<0.5)].shape[0]
                """)
    elif data is not None and data.name != "car data.csv":
        st.error("Please upload 'car data.csv'")



elif Q == "Q11. data_result.csv Analysis":
    st.subheader("Q11. Student Result Analysis (data_result.csv)")
    data = st.file_uploader("Upload data_result.csv", type=["csv"])
    if data is not None and data.name == "data_result.csv":
        df = pd.read_csv(data)

        with st.expander("1 & 2. First few rows"):
            st.dataframe(df.head(4))
            if st.checkbox("Show Code", key="q11_1_2"):
                st.code("""
df.head(4)
                    """)

        with st.expander("3. Shape of dataset"):
            st.write(f"**Shape:** `{df.shape}`")
            if st.checkbox("Show Code", key="q11_3"):
                st.code("""
df.shape
                """)

        with st.expander("4. Last few rows"):
            st.dataframe(df.tail(4))
            if st.checkbox("Show Code", key="q11_4"):
                st.code("""
df.tail(4)
                """)

        with st.expander("5. Summary statistics (numerical)"):
            st.dataframe(df.describe())
            if st.checkbox("Show Code", key="q11_5"):
                st.code("""
df.describe()
                """)

        with st.expander("6. Summary statistics with custom percentiles (0.58 & 0.87)"):
            st.dataframe(df.describe(percentiles=[0.58, 0.87]))
            if st.checkbox("Show Code", key="q11_6"):
                st.code("""
df.describe(percentiles=[0.58, 0.87])
                """)

        with st.expander("7. Summary statistics (all column types)"):
            st.dataframe(df.describe(include="all"))
            if st.checkbox("Show Code", key="q11_7"):
                st.code("""
df.describe(include="all")
                """)

        with st.expander("8. Info of all columns"):
            buf = io.StringIO(); df.info(buf=buf); st.text(buf.getvalue())
            if st.checkbox("Show Code", key="q11_8"):
                st.code("""
df.info()
                """)

        with st.expander("9. Check for missing values"):
            st.dataframe(df.isnull().sum().rename("Missing Values"))
            if st.checkbox("Show Code", key="q11_9"):
                st.code("""
df.isnull().sum()
                """)

        with st.expander("10. Remove duplicates"):
            clean = df.drop_duplicates()
            st.write(f"**Rows before:** {len(df)} | **After:** {len(clean)}")
            st.dataframe(clean)
            if st.checkbox("Show Code", key="q11_10"):
                st.code("""
df.drop_duplicates()
                """)

        with st.expander("11. Female students with SPI > 7 in all semesters"):
            st.dataframe(df[(df["Gender"]=="Female") & (df["Sem1_SPI"]>7)& 
    (df["Sem2_SPI"]>7)& (df["Sem3_SPI"]>7)& 
    (df["Sem4_SPI"]>7)& (df["Sem5_SPI"]>7)])
            if st.checkbox("Show Code", key="q11_11"):
                st.code("""
df[(df["Gender"]=="Female") & (df["Sem1_SPI"]>7)& 
   (df["Sem2_SPI"]>7)& (df["Sem3_SPI"]>7)& 
   (df["Sem4_SPI"]>7)& (df["Sem5_SPI"]>7)]
                """)

        with st.expander("12. Students with SPI > 8 in all 5 semesters"):
            count = df[(df["Sem1_SPI"]>8)& (df["Sem2_SPI"]>8)& (df["Sem3_SPI"]>8)& 
    (df["Sem4_SPI"]>8)& (df["Sem5_SPI"]>8)].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q11_12"):
                st.code("""
df[(df["Sem1_SPI"]>8)& (df["Sem2_SPI"]>8)& (df["Sem3_SPI"]>8)& 
   (df["Sem4_SPI"]>8)& (df["Sem5_SPI"]>8)].shape[0]
                """)

        with st.expander("13. Outliers in Sem4 SPI (Boxplot)"):
            fig, ax = plt.subplots()
            sns.boxplot(df["Sem4_SPI"], ax=ax)
            ax.set_title("Sem4 SPI Boxplot")
            st.pyplot(fig)
            plt.close()
            
    elif data is not None and data.name != "data_result.csv":
        st.error("Please upload 'data_result.csv'")



elif Q == "Q12. Movies Analysis":
    st.subheader("Q12. Movies Dataset Analysis (movies.csv)")
    data = st.file_uploader("Upload movies.csv", type=["csv"])
    if data is not None and data.name == "movies.csv":
        df = pd.read_csv(data)
        buf = io.StringIO(); df.info(buf=buf)
        with st.expander("Dataset Info"):
            st.text(buf.getvalue())

        with st.expander("1. Movies released in 2019"):
            st.dataframe(df[df["year_of_release"] == 2019])
            if st.checkbox("Show Code", key="q12_1"):
                st.code('df[df["year_of_release"] == 2019]')

        with st.expander("2. Movies with IMDB Rating > 7"):
            count = df[df["imdb_rating"] > 7].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q12_2"):
                st.code('df[df["imdb_rating"] > 7].shape[0]')

        with st.expander("3. Movies with IMDB Votes > 20,000 (title & story)"):
            cols = [c for c in ["title_x", "story"] if c in df.columns]
            st.dataframe(df[df["imdb_votes"] > 20000][cols])
            if st.checkbox("Show Code", key="q12_3"):
                st.code('df[df["imdb_votes"] > 20000][["title_x", "story"]]')

        with st.expander("4. Movies released in 2018 — Title & Release Date"):
            cols = [c for c in ["original_title", "year_of_release"] if c in df.columns]
            st.dataframe(df[df["year_of_release"] == 2018][cols])
            if st.checkbox("Show Code", key="q12_4"):
                st.code('df[df["year_of_release"]==2018][["original_title","year_of_release"]]')

        with st.expander("5. Movie Title with Wikipedia Link"):
            cols = [c for c in ["original_title", "wiki_link"] if c in df.columns]
            st.dataframe(df[cols])
            if st.checkbox("Show Code", key="q12_5"):
                st.code('df[["original_title", "wiki_link"]]')
    elif data is not None and data.name != "movies.csv":
        st.error("Please upload 'movies.csv'")



elif Q == "Q13. IPL Advanced Analysis":
    st.subheader("Q13. IPL Advanced Analysis (ipl-matches.csv)")
    data = st.file_uploader("Upload ipl-matches.csv", type=["csv"])
    if data is not None and data.name == "ipl-matches.csv":
        df = pd.read_csv(data)
        buf = io.StringIO(); df.info(buf=buf)
        with st.expander("Dataset Info"):
            st.text(buf.getvalue())

        with st.expander("1. Matches won by Gujarat Titans in a Super Over"):
            count = df[(df["SuperOver"] == "Y") & (df["WinningTeam"] == "Gujarat Titans")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_1"):
                st.code('df[(df["SuperOver"]=="Y") & (df["WinningTeam"]=="Gujarat Titans")].shape[0]')

        with st.expander("2. Matches won by RCB vs KKR"):
            count = df[(df["WinningTeam"] == "Royal Challengers Bangalore") &
                       ((df["Team1"] == "Kolkata Knight Riders") | (df["Team2"] == "Kolkata Knight Riders"))].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_2"):
                st.code("""
df[(df["WinningTeam"]=="Royal Challengers Bangalore") &
   ((df["Team1"]=="Kolkata Knight Riders") |
    (df["Team2"]=="Kolkata Knight Riders"))].shape[0]
                """)

        with st.expander("3. Matches won by Toss Winner"):
            count = df[df["WinningTeam"] == df["TossWinner"]].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_3"):
                st.code('df[df["WinningTeam"] == df["TossWinner"]].shape[0]')

        with st.expander("4. D/L method matches won by Wickets"):
            count = df[(df["method"] == "D/L") & (df["WonBy"] == "Wickets")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_4"):
                st.code('df[(df["method"]=="D/L") & (df["WonBy"]=="Wickets")].shape[0]')

        with st.expander("5. Rajasthan Royals won Toss AND won the Match"):
            count = df[(df["WinningTeam"] == "Rajasthan Royals") & (df["TossWinner"] == "Rajasthan Royals")].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_5"):
                st.code("""
df[(df["WinningTeam"]=="Rajasthan Royals") &
   (df["TossWinner"]=="Rajasthan Royals")].shape[0]
                """)

        with st.expander("6. V Kohli as Player of Match vs CSK"):
            count = df[(df["Player_of_Match"] == "V Kohli") &
                       ((df["Team1"] == "Chennai Super Kings") | (df["Team2"] == "Chennai Super Kings"))].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q13_6"):
                st.code("""
df[(df["Player_of_Match"]=="V Kohli") &
   ((df["Team1"]=="Chennai Super Kings") |
    (df["Team2"]=="Chennai Super Kings"))].shape[0]
                """)

        with st.expander("7. Toss Winner in Final played at Dubai"):
            result = df[(df["MatchNumber"] == "Final") & (df["City"] == "Dubai")]["TossWinner"]
            st.dataframe(result.reset_index(drop=True))
            if st.checkbox("Show Code", key="q13_7"):
                st.code('df[(df["MatchNumber"]=="Final") & (df["City"]=="Dubai")]["TossWinner"]')

        with st.expander("8. Finals where KKR won Toss and chose to Field"):
            result = df[(df["MatchNumber"] == "Final") & (df["TossWinner"] == "Kolkata Knight Riders") & (df["TossDecision"] == "field")]
            st.dataframe(result)
            if st.checkbox("Show Code", key="q13_8"):
                st.code("""
df[(df["MatchNumber"]=="Final") &
   (df["TossWinner"]=="Kolkata Knight Riders") &
   (df["TossDecision"]=="field")]
                """)
    elif data is not None and data.name != "ipl-matches.csv":
        st.error("Please upload the correct file: ipl-matches.csv")



elif Q == "Q14. Sort Employees":
    st.subheader("Q14. Sort employees by Dept (Ascending) and Salary (Descending), then sort index Descending")

    data = {
        "EmpID":  [101, 102, 103, 104, 105],
        "Dept":   ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [60000, 45000, 80000, 75000, 50000],
        "Age":    [25, 32, 29, 41, 28]
    }
    df = pd.DataFrame(data)
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    df_sorted = df.sort_values(by=["Dept", "Salary"], ascending=[True, False])
    df_sorted = df_sorted.sort_index(ascending=False)
    st.write("**After sorting :**")
    st.dataframe(df_sorted)

    if st.checkbox("Show Code", key="q14"):
        st.code("""
df.sort_values(by=["Dept","Salary"], ascending=[True, False], inplace=True)
df.sort_index(ascending=False)
        """)



elif Q == "Q15. Apply & Grade Column":
    st.subheader("Q15. Create Average column and Grade column using apply()")

    df = pd.DataFrame({
        "Student": ["A", "B", "C", "D"],
        "Math":    [70, 45, 90, 60],
        "Science": [75, 40, 85, 55]
    })
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    df["Average"] = df[["Math", "Science"]].mean(axis=1)
    df["Grade"] = np.where(df["Average"] >= 80, "Distinction",
                  np.where(df["Average"] >= 60, "First", "Second"))

    st.write("**After adding Average and Grade columns:**")
    st.dataframe(df)

    if st.checkbox("Show Code", key="q15"):
        st.code("""
df["Average"] = df[["Math","Science"]].mean(axis=1)
df["Grade"] = np.where(df["Average"]>=80, "Distinction",
              np.where(df["Average"]>=60, "First", "Second"))
        """)



elif Q == "Q16. Replace Absent with 0":
    st.subheader("Q16. Replace 'Absent' with 0, convert to int, show mean and students above 50")

    df = pd.DataFrame({"Marks": ["50", "60", "Absent", "70", "Absent"]})
    st.write("**Original DataFrame:**")
    st.dataframe(df)

    df.replace("Absent", "0", inplace=True)
    df["Marks"] = pd.to_numeric(df["Marks"])

    st.write("**After replacement and conversion:**")
    st.dataframe(df)

    mean_val = df["Marks"].mean()
    above_50 = (df["Marks"] > 50).sum()

    st.metric("Mean Marks", f"{mean_val:.1f}")
    st.metric("Students scoring above 50", int(above_50))

    if st.checkbox("Show Code", key="q16"):
        st.code("""
df.replace("Absent", "0", inplace=True)
df["Marks"] = pd.to_numeric(df["Marks"])
df["Marks"].mean()
(df["Marks"] > 50).sum()
        """)



elif Q == "Q17. Concatenate & Outer Join":
    st.subheader("Q17. Outer merge two DataFrames, count missing values, sort by ID")

    df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["A", "B", "C"]})
    df2 = pd.DataFrame({"ID": [2, 3, 4], "Marks": [80, 90, 70]})

    col1, col2 = st.columns(2)
    with col1:
        st.write("**DataFrame 1:**"); st.dataframe(df1)
    with col2:
        st.write("**DataFrame 2:**"); st.dataframe(df2)

    merged = pd.merge(df1, df2, how="outer", on="ID")
    missing = merged.isnull().sum().sum()
    merged = merged.sort_values(by="ID")

    st.write(f"**Total missing values after merge:** `{missing}`")
    st.write("**Merged & Sorted DataFrame:**")
    st.dataframe(merged)

    if st.checkbox("Show Code", key="q17"):
        st.code("""
merged = pd.merge(df1, df2, how='outer', on='ID')
missing = merged.isnull().sum().sum()
merged = merged.sort_values(by='ID')
        """)



elif Q == "Q18. Outer Merge with Indicator":
    st.subheader("Q18. Outer merge with indicator=True — count both/left_only/right_only")

    students = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["A", "B", "C", "D"]})
    marks    = pd.DataFrame({"ID": [2, 3, 5], "Score": [85, 90, 75]})

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Students:**"); st.dataframe(students)
    with col2:
        st.write("**Marks:**"); st.dataframe(marks)

    merged = pd.merge(students, marks, how="outer", indicator=True)
    st.write("**Merged DataFrame with `_merge` indicator:**")
    st.dataframe(merged)

    both       = merged[merged["_merge"] == "both"].shape[0]
    left_only  = merged[merged["_merge"] == "left_only"].shape[0]
    right_only = merged[merged["_merge"] == "right_only"].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("In Both", both)
    col2.metric("Only in Students", left_only)
    col3.metric("Only in Marks", right_only)

    if st.checkbox("Show Code", key="q18"):
        st.code("""
merged = pd.merge(students, marks, how='outer', indicator=True)
merged[merged["_merge"]=="both"].shape[0]
merged[merged["_merge"]=="left_only"].shape[0]
merged[merged["_merge"]=="right_only"].shape[0]
        """)



elif Q == "Q19. GroupBy Dept - Mean/Median/Max":
    st.subheader("Q19. Group by Dept and calculate Mean, Median, Max salary")

    df = pd.DataFrame({
        "Dept":   ["IT", "IT", "HR", "HR", "Finance", "Finance"],
        "Salary": [50000, 70000, 40000, 60000, 80000, 75000]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    result = df.groupby("Dept")["Salary"].agg(["mean", "median", "max"])
    st.write("**GroupBy Result:**"); st.dataframe(result)

    if st.checkbox("Show Code", key="q19"):
        st.code('df.groupby("Dept")["Salary"].agg(["mean", "median", "max"])')



elif Q == "Q20. Range per Team using GroupBy":
    st.subheader("Q20. Calculate Range (max − min) per Team using groupby + apply")

    df = pd.DataFrame({
        "Team": ["A", "A", "A", "B", "B"],
        "Runs": [50, 70, 80, 40, 60]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    result = df.groupby("Team")["Runs"].apply(lambda x: x.max() - x.min())
    result = result.rename("Range (max-min)").reset_index()
    st.write("**Range per Team:**"); st.dataframe(result)

    if st.checkbox("Show Code", key="q20"):
        st.code('df.groupby("Team")["Runs"].apply(lambda x: x.max() - x.min())')

elif Q == "Q21. Detect & Remove Outliers (IQR)":
    st.subheader("Q21. Detect outliers using IQR method, remove them, print cleaned dataset")

    df = pd.DataFrame({"Salary": [20000, 22000, 21000, 25000, 24000, 300000]})
    st.write("**Original DataFrame:**"); st.dataframe(df)

    fig, ax = plt.subplots()
    sns.boxplot(df["Salary"], ax=ax)
    ax.set_title("Salary Boxplot (with outlier)")
    st.pyplot(fig); plt.close()

    q3 = df["Salary"].quantile(0.75)
    q1 = df["Salary"].quantile(0.25)
    iqr = q3 - q1
    upper = q3 + (iqr * 1.5)
    lower = q1 - (iqr * 1.5)
    clean = df[(df["Salary"] < upper) & (df["Salary"] > lower)]

    st.write(f"**IQR:** {iqr} | **Lower bound:** {lower:.0f} | **Upper bound:** {upper:.0f}")
    st.write("**Cleaned DataFrame (outliers removed):**"); st.dataframe(clean)

    if st.checkbox("Show Code", key="q21"):
        st.code("""
q3 = df["Salary"].quantile(0.75)
q1 = df["Salary"].quantile(0.25)
iqr = q3 - q1
upper = q3 + (iqr * 1.5)
lower = q1 - (iqr * 1.5)
clean = df[(df["Salary"] < upper) & (df["Salary"] > lower)]
        """)



elif Q == "Q22. Unique Cities & Random Employee per Dept":
    st.subheader("Q22. Unique cities per Dept and one random employee per Dept")

    df = pd.DataFrame({
        "Dept":     ["IT", "IT", "HR", "HR", "Finance", "Finance"],
        "Employee": ["A", "B", "C", "D", "E", "F"],
        "City":     ["X", "X", "Y", "Z", "X", "Y"]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    unique_cities = df.groupby("Dept")["City"].nunique().reset_index()
    unique_cities.columns = ["Dept", "Unique Cities"]
    st.write("**Unique cities per Dept:**"); st.dataframe(unique_cities)

    random_emp = df.groupby("Dept").sample(1).reset_index(drop=True)
    st.write("**One random employee per Dept:**"); st.dataframe(random_emp)

    if st.checkbox("Show Code", key="q22"):
        st.code("""
df.groupby("Dept")["City"].nunique()
df.groupby("Dept").sample(1)
        """)



elif Q == "Q23. TotalAmount Column & Sort":
    st.subheader("Q23. Create TotalAmount = Price × Quantity, sort descending")

    df = pd.DataFrame({
        "Product":  ["P1", "P2", "P3", "P4", "P5"],
        "Price":    [100, 200, 150, 300, 250],
        "Quantity": [5, 2, 4, 1, 3]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    df["TotalAmount"] = df["Price"] * df["Quantity"]
    result = df.sort_values(by="TotalAmount", ascending=False)
    st.write("**With TotalAmount column, sorted descending:**"); st.dataframe(result)

    if st.checkbox("Show Code", key="q23"):
        st.code("""
df["TotalAmount"] = df["Price"] * df["Quantity"]
df.sort_values(by="TotalAmount", ascending=False)
        """)



elif Q == "Q24. GroupBy Dept - Total & Avg Salary":
    st.subheader("Q24. GroupBy Dept — Total & Average Salary, filter avg > 50,000")

    df = pd.DataFrame({
        "Employee": ["A", "B", "C", "D", "E"],
        "Dept":     ["IT", "HR", "IT", "Finance", "HR"],
        "Salary":   [50000, 40000, 70000, 80000, 45000]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    st.write("**Employee count per Dept:**")
    st.dataframe(df.groupby("Dept")["Employee"].count().reset_index())

    agg = df.groupby("Dept")["Salary"].agg(["sum", "mean"]).rename(columns={"sum": "Total Salary", "mean": "Avg Salary"})
    st.write("**Total & Average Salary per Dept:**"); st.dataframe(agg)

    filtered = agg[agg["Avg Salary"] > 50000]
    st.write("**Depts where Avg Salary > 50,000:**"); st.dataframe(filtered)

    if st.checkbox("Show Code", key="q24"):
        st.code("""
df.groupby("Dept")["Employee"].count()
agg = df.groupby("Dept")["Salary"].agg(["sum", "mean"])
agg[agg["mean"] > 50000]
        """)



elif Q == "Q25. Employees per Dept & Max Experience":
    st.subheader("Q25. Employee count per Dept (size) and most experienced per Dept")

    df = pd.DataFrame({
        "Dept":       ["IT", "IT", "HR", "HR", "Finance", "Finance"],
        "Employee":   ["A", "B", "C", "D", "E", "F"],
        "Experience": [2, 5, 3, 7, 4, 6]
    })
    st.write("**Original DataFrame:**"); st.dataframe(df)

    size_result = df.groupby("Dept").size().reset_index(name="Employee Count")
    st.write("**Employees per Dept:**"); st.dataframe(size_result)

    max_exp = df.groupby("Dept")[["Employee", "Experience"]].max().reset_index()
    st.write("**Most experienced employee per Dept:**"); st.dataframe(max_exp)

    if st.checkbox("Show Code", key="q25"):
        st.code("""
df.groupby("Dept").size()
df.groupby("Dept")[["Employee","Experience"]].max()
        """)



elif Q == "Q26. House Data Analysis (kc_house_data.csv)":
    st.subheader("Q26. King County House Sales Analysis (kc_house_data.csv)")
    data = st.file_uploader("Upload kc_house_data.csv", type=["csv"])
    if data is not None and "house" in data.name.lower():
        df = pd.read_csv(data)

        with st.expander("1. Load dataset & show first 5 rows"):
            st.dataframe(df.head(5))

        with st.expander("2. Drop 'id' and 'Unnamed: 0' columns"):
            cols_to_drop = [c for c in ["id", "Unnamed: 0"] if c in df.columns]
            df.drop(cols_to_drop, axis=1, inplace=True)
            st.write(f"Dropped: {cols_to_drop}")
            st.dataframe(df.head())

        with st.expander("3. Check null values"):
            st.dataframe(df.isnull().sum().rename("Missing"))

        with st.expander("4. Fill missing values with column mean"):
            for col in ["bedrooms", "bathrooms"]:
                if col in df.columns:
                    df[col] = df[col].fillna(df[col].mean())
            st.write("**Null values after filling:**")
            st.dataframe(df.isnull().sum().rename("Missing"))

        with st.expander("5. Correlation table"):
            st.dataframe(df.corr(numeric_only=True))

        if st.checkbox("Show Code", key="q26"):
            st.code("""
df.head(5)
df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)
df.isnull().sum()
df["bedrooms"].fillna(df["bedrooms"].mean(), inplace=True)
df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)
df.corr(numeric_only=True)
            """)
    elif data is not None and data.name != "kc_house_data.csv":
        st.error("Please upload 'kc_house_data.csv'")



elif Q == "Q27. Supermarket Sales Analysis":
    st.subheader("Q27. Supermarket Sales Analysis (supermarket_sales.csv)")
    data = st.file_uploader("Upload supermarket_sales.csv", type=["csv"])
    if data is not None and "supermarket" in data.name.lower():
        df = pd.read_csv(data)

        with st.expander("1. Load dataset & first 8 rows"):
            st.dataframe(df.head(8))

        with st.expander("2. Check & fill missing values with column mean"):
            st.write("**Missing values before:**")
            st.dataframe(df.isnull().sum().rename("Missing"))
            for col in df.select_dtypes(include="number").columns:
                df[col] = df[col].fillna(df[col].mean())
            st.write("**Missing values after filling:**")
            st.dataframe(df.isnull().sum().rename("Missing"))

        with st.expander("3. Orders with Quantity < 3 AND (Rating > 8.5 OR Total > 600)"):
            count = df[(df["Quantity"] < 3) & ((df["Rating"] > 8.5) | (df["Total"] > 600))].shape[0]
            st.metric("Count", count)
            if st.checkbox("Show Code", key="q27_3"):
                st.code('df[(df["Quantity"]<3) & ((df["Rating"]>8.5) | (df["Total"]>600))].shape[0]')

        with st.expander("4. Sum of Total spending by Customer Type"):
            if "Customer type" in df.columns and "Total" in df.columns:
                result = df.groupby("Customer type")["Total"].sum().reset_index()
                st.dataframe(result)
                if st.checkbox("Show Code", key="q27_4"):
                    st.code('df.groupby("Customer type")["Total"].sum()')

        if st.checkbox("Show All Code", key="q27_all"):
            st.code("""
df.head(8)
df.isnull().sum()
df["Quantity"].fillna(df["Quantity"].mean(), inplace=True)
df["Rating"].fillna(df["Rating"].mean(), inplace=True)
df[(df["Quantity"]<3) & ((df["Rating"]>8.5) | (df["Total"]>600))].shape[0]
df.groupby("Customer type")["Total"].sum()
            """)
    elif data is not None and data.name != "supermarket_sales.csv":
        st.error("Please upload 'supermarket_sales.csv'")


st.markdown("""
<hr style="margin-top:50px;">
<div style="text-align:center; padding:10px;">
<a href="https://github.com/Pareshprajapati-777" target="_blank">
    <img src="https://github.com/Pareshprajapati-777.png"
         width="90"
         style="border-radius:50%; border:2px solid #555; margin-bottom:10px;">
</a>
<p style="font-size:18px; margin:0;"><b>Paresh Prajapati</b></p>
<p style="color:gray; margin:5px 0;">AI • ML • Data Science</p>
<p style="font-size:14px; color:#808080;">© 2026 Pandas Questions Solver</p>
</div>
""", unsafe_allow_html=True)
