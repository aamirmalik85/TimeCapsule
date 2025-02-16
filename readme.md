#**Time Capsule Generator**
###🏆
# Time Capsule Generator

## Overview

The **Time Capsule Generator** is a web application built using **Streamlit** and powered by **OpenAI's GPT-3.5/4** model. It allows users to create personalized time capsules by reflecting on their current life, goals, and thoughts. The application generates a unique time capsule containing a reflective summary, future predictions, and a heartfelt letter from the user's past self to their future self. Users can also share their time capsules on social media or download them as JSON files.

## Features

- **Create Time Capsule**: Users can input their name, email, and reflections on their current life, goals, and thoughts. The AI generates a time capsule with a reflective summary, future predictions, and a letter from their past self.
- **My Capsules**: Users can view all the time capsules they have created, organized by name and delivery date.
- **Unbox Capsule**: Users can unbox their time capsules and generate new reflections comparing their past and present selves.
- **Share**: Users can share their time capsules on social media platforms like Facebook, WhatsApp, Instagram, and LinkedIn.
- **Email Notifications**: Users receive an email with a preview of their time capsule when it is created.
- **Download as JSON**: Users can download their time capsules as JSON files for future reference.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **OpenAI GPT-3.5/4**: For generating the content of the time capsules.
- **Gmail API**: For sending email notifications to users.
- **OAuth 2.0**: For authenticating with Gmail's API.
- **Python**: The core programming language used for the backend logic.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   git clone https://github.com/your-username/time-capsule-generator.git
   cd time-capsule-generator
   
2. **Set Up Environment Variables**:
Create a .env file in the root directory and add the following variables:
OPENAI_API_KEY=your_openai_api_key
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
GMAIL_REFRESH_TOKEN=your_gmail_refresh_token

3. **Install Dependencies**:
pip install -r requirements.txt

4. **Run the Application**:
streamlit run app.py
Access the Application:

Open your browser and navigate to http://localhost:8501.

5. *Usage*
i. **Create a Time Capsule**:
  Navigate to the "Create Capsule" tab.
  Fill in your name, email, and reflections on your current life, goals, and thoughts.
  Choose a theme and set a delivery date.
  Click "Create Time Capsule" to generate your capsule.

ii. **View Your Capsules****:
Go to the "My Capsules" tab to view all the time capsules you have created.

iii. **Unbox a Capsule**:
In the "Unbox Capsule" tab, select a capsule to unbox and generate new reflections.

iv. **Share Your Capsule**:
Use the "Share" tab to share your time capsule on social media platforms.

6. *License*
This project is licensed under the MIT License. See the LICENSE file for details.

7. *Acknowledgments*
OpenAI for providing the GPT-3.5/4 API.
Streamlit for the easy-to-use web framework.
Google for the Gmail API and OAuth 2.0 integration.


##**Contact**
For any questions or feedback, please reach out to [Aamir Malik] at [anm782@gmail.com].

Built with ❤️ using DeepSeek / OpenAI and Streamlit.
