import streamlit as st
import datetime
import json
import requests
import os
from streamlit_option_menu import option_menu  # For better navigation

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set this in Hugging Face Secrets
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# Function to call OpenAI API
def generate_time_capsule_content(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",  # Use GPT-3.5 or GPT-4
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        st.error(f"🚨 Error calling OpenAI API: {response.status_code} - {response.text}")
        return None

# Initialize session state for capsules
if "capsules" not in st.session_state:
    st.session_state.capsules = []

# Navigation Menu
with st.sidebar:
    selected_tab = option_menu(
        menu_title="Main Menu",
        options=["Create Capsule", "My Capsules", "Unbox Capsule", "Share"],
        icons=["capsule", "archive", "gift", "share"],
        default_index=0,
    )

# Tab 1: Create Capsule
if selected_tab == "Create Capsule":
    st.header("📦 Create Your Time Capsule")
    st.write("Tell us about your life, dreams, and thoughts. The AI will create a unique time capsule for you.")

    # User Input Fields
    name = st.text_input("Your Name", placeholder="John Doe")
    email = st.text_input("Your Email (for future delivery)", placeholder="john.doe@example.com")
    capsule_date = st.date_input("When should we deliver your time capsule?", min_value=datetime.date.today())
    theme = st.selectbox("Choose a Theme", ["Nostalgic", "Futuristic", "Inspirational", "Adventurous"])
    current_life = st.text_area("What's happening in your life right now?", placeholder="I'm currently studying computer science and dreaming of starting my own startup...")
    goals = st.text_area("What are your goals and dreams?", placeholder="I want to build a successful AI startup and travel the world...")
    thoughts = st.text_area("What's on your mind?", placeholder="I feel a bit overwhelmed but excited about the future...")

    # Generate Time Capsule
    if st.button("Create Time Capsule"):
        if name and email and current_life and goals and thoughts:
            with st.spinner("🪄 Creating your time capsule..."):
                # Combine user input into a single prompt
                prompt = f"""
                Name: {name}
                Current Life: {current_life}
                Goals: {goals}
                Thoughts: {thoughts}
                Theme: {theme}

                Generate:
                1. A reflective summary of this person's current state.
                2. Fun predictions about their future.
                3. A heartfelt letter from their past self to their future self.
                """

                # Call OpenAI API to generate the time capsule content
                capsule_content = generate_time_capsule_content(prompt)
                if capsule_content:
                    # Save the time capsule to session state
                    capsule_data = {
                        "name": name,
                        "email": email,
                        "delivery_date": capsule_date.strftime("%Y-%m-%d"),
                        "theme": theme,
                        "content": capsule_content,
                        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    st.session_state.capsules.append(capsule_data)

                    # Display the time capsule content
                    st.success("🎉 Your time capsule is ready!")
                    st.subheader("✨ Reflective Summary")
                    st.write(capsule_content.split("1. ")[1].split("2. ")[0].strip())
                    st.subheader("🔮 Future Predictions")
                    st.write(capsule_content.split("2. ")[1].split("3. ")[0].strip())
                    st.subheader("💌 Letter from Your Past Self")
                    st.write(capsule_content.split("3. ")[1].strip())

                    # Option to download the time capsule
                    st.download_button(
                        label="Download Your Time Capsule",
                        data=json.dumps(capsule_data, indent=2),
                        file_name=f"time_capsule_{name.replace(' ', '_')}.json",
                        mime="application/json",
                    )
        else:
            st.warning("Please fill in all fields and click 'Create Time Capsule'.")

# Tab 2: My Capsules
elif selected_tab == "My Capsules":
    st.header("📚 My Time Capsules")
    if st.session_state.capsules:
        for i, capsule in enumerate(st.session_state.capsules):
            with st.expander(f"Capsule {i+1}: {capsule['name']} - {capsule['delivery_date']}", expanded=False):
                st.write(f"**Theme:** {capsule['theme']}")
                st.write(f"**Reflective Summary:** {capsule['content'].split('1. ')[1].split('2. ')[0].strip()}")
                st.write(f"**Future Predictions:** {capsule['content'].split('2. ')[1].split('3. ')[0].strip()}")
                st.write(f"**Letter from Your Past Self:** {capsule['content'].split('3. ')[1].strip()}")
    else:
        st.info("You haven't created any time capsules yet. Go to the 'Create Capsule' tab to get started!")

# Tab 3: Unbox Capsule
elif selected_tab == "Unbox Capsule":
    st.header("🎁 Unbox Your Time Capsule")
    if st.session_state.capsules:
        selected_capsule = st.selectbox("Select a Capsule to Unbox", [capsule["name"] for capsule in st.session_state.capsules])
        capsule_index = [capsule["name"] for capsule in st.session_state.capsules].index(selected_capsule)
        capsule = st.session_state.capsules[capsule_index]

        st.write(f"Unboxing Capsule: **{capsule['name']}**")
        st.write(f"**Theme:** {capsule['theme']}")
        st.write(f"**Reflective Summary:** {capsule['content'].split('1. ')[1].split('2. ')[0].strip()}")
        st.write(f"**Future Predictions:** {capsule['content'].split('2. ')[1].split('3. ')[0].strip()}")
        st.write(f"**Letter from Your Past Self:** {capsule['content'].split('3. ')[1].strip()}")

        # Interactive Unboxing: Generate a new reflection
        if st.button("Generate New Reflection"):
            with st.spinner("🪄 Generating a new reflection..."):
                prompt = f"""
                Past Reflection:
                {capsule['content'].split('1. ')[1].split('2. ')[0].strip()}

                Current Life:
                {st.session_state.get("current_life", "No current life details available.")}

                Generate:
                1. A comparison of the user's past and present.
                2. Insights on how the user has grown or changed.
                """
                new_reflection = generate_time_capsule_content(prompt)
                if new_reflection:
                    st.success("🎉 New reflection generated!")
                    st.subheader("✨ Past vs. Present Comparison")
                    st.write(new_reflection.split("1. ")[1].split("2. ")[0].strip())
                    st.subheader("🔮 Insights on Growth")
                    st.write(new_reflection.split("2. ")[1].strip())
    else:
        st.info("You haven't created any time capsules yet. Go to the 'Create Capsule' tab to get started!")

# Tab 4: Share
elif selected_tab == "Share":
    st.header("📤 Share Your Time Capsule")
    if st.session_state.capsules:
        selected_capsule = st.selectbox("Select a Capsule to Share", [capsule["name"] for capsule in st.session_state.capsules])
        capsule_index = [capsule["name"] for capsule in st.session_state.capsules].index(selected_capsule)
        capsule = st.session_state.capsules[capsule_index]

        st.write(f"Sharing Capsule: **{capsule['name']}**")
        st.write(f"**Theme:** {capsule['theme']}")
        st.write(f"**Reflective Summary:** {capsule['content'].split('1. ')[1].split('2. ')[0].strip()}")
        st.write(f"**Future Predictions:** {capsule['content'].split('2. ')[1].split('3. ')[0].strip()}")
        st.write(f"**Letter from Your Past Self:** {capsule['content'].split('3. ')[1].strip()}")

        # Social Media Sharing Options
        st.subheader("Share on Social Media")
        share_text = f"Check out my Time Capsule: {capsule['name']} - {capsule['content'].split('1. ')[1].split('2. ')[0].strip()}"
        share_url = "https://huggingface.co/spaces/AamirMalik/Time_Capsule"  # Replace with your app's URL

        # Facebook Button
        facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
        st.markdown(f"""
        <a href="{facebook_url}" target="_blank">
            <button style="
                width: 100%;
                margin: 10px 0;
                padding: 15px;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                background-color: #1877F2;
                color: white;
                cursor: pointer;
                transition: all 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" style="width: 20px; height: 20px; margin-right: 10px;">
                Share on Facebook
            </button>
        </a>
        """, unsafe_allow_html=True)

        # WhatsApp Button
        whatsapp_url = f"https://wa.me/?text={share_text} {share_url}"
        st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank">
            <button style="
                width: 100%;
                margin: 10px 0;
                padding: 15px;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                background-color: #25D366;
                color: white;
                cursor: pointer;
                transition: all 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" style="width: 20px; height: 20px; margin-right: 10px;">
                Share on WhatsApp
            </button>
        </a>
        """, unsafe_allow_html=True)

        # Instagram Button
        st.markdown(f"""
        <button style="
            width: 100%;
            margin: 10px 0;
            padding: 15px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D, #F56040, #F77737, #FCAF45, #FFDC80);
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
        " onclick="navigator.clipboard.writeText('{share_url}')">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" style="width: 20px; height: 20px; margin-right: 10px;">
            Copy Instagram Link
        </button>
        """, unsafe_allow_html=True)
        st.caption("Paste this link in your Instagram bio or story.")

        # LinkedIn Button
        linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={share_url}"
        st.markdown(f"""
        <a href="{linkedin_url}" target="_blank">
            <button style="
                width: 100%;
                margin: 10px 0;
                padding: 15px;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                background-color: #0A66C2;
                color: white;
                cursor: pointer;
                transition: all 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 10px;">
                Share on LinkedIn
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.info("You haven't created any time capsules yet. Go to the 'Create Capsule' tab to get started!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [DeepSeek](https://deepseek.com/.com) / [OpenAI](https://openai.com) and [Streamlit](https://streamlit.io).")