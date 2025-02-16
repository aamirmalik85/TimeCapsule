Time Capsule Generator
Overview
The Time Capsule Generator is a web application built using Streamlit and powered by OpenAI's GPT-3.5/4 model. It allows users to create personalized time capsules by reflecting on their current life, goals, and thoughts. The application generates a unique time capsule containing a reflective summary, future predictions, and a heartfelt letter from the user's past self to their future self. Users can also share their time capsules on social media or download them as JSON files.

The application integrates with Gmail's API to send email notifications to users when their time capsule is created. It also provides an interactive experience where users can unbox their capsules and generate new reflections based on their past and present experiences.

Features
Create Time Capsule: Users can input their name, email, and reflections on their current life, goals, and thoughts. The AI generates a time capsule with a reflective summary, future predictions, and a letter from their past self.

My Capsules: Users can view all the time capsules they have created, organized by name and delivery date.

Unbox Capsule: Users can unbox their time capsules and generate new reflections comparing their past and present selves.

Share: Users can share their time capsules on social media platforms like Facebook, WhatsApp, Instagram, and LinkedIn.

Email Notifications: Users receive an email with a preview of their time capsule when it is created.

Download as JSON: Users can download their time capsules as JSON files for future reference.

Technologies Used
Streamlit: For building the web application interface.

OpenAI GPT-3.5/4: For generating the content of the time capsules.

Gmail API: For sending email notifications to users.

OAuth 2.0: For authenticating with Gmail's API.

Python: The core programming language used for the backend logic.

Installation
To run this project locally, follow these steps:

Clone the Repository:

bash
Copy
git clone https://github.com/your-username/time-capsule-generator.git
cd time-capsule-generator
Set Up Environment Variables:

Create a .env file in the root directory and add the following variables:

Copy
OPENAI_API_KEY=your_openai_api_key
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
GMAIL_REFRESH_TOKEN=your_gmail_refresh_token
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Run the Application:

bash
Copy
streamlit run app.py
Access the Application:

Open your browser and navigate to http://localhost:8501.

Usage
Create a Time Capsule:

Navigate to the "Create Capsule" tab.

Fill in your name, email, and reflections on your current life, goals, and thoughts.

Choose a theme and set a delivery date.

Click "Create Time Capsule" to generate your capsule.

View Your Capsules:

Go to the "My Capsules" tab to view all the time capsules you have created.

Unbox a Capsule:

In the "Unbox Capsule" tab, select a capsule to unbox and generate new reflections.

Share Your Capsule:

Use the "Share" tab to share your time capsule on social media platforms.

Configuration
OpenAI API Key: Obtain an API key from OpenAI.

Gmail API Credentials: Set up OAuth 2.0 credentials in the Google Cloud Console and obtain the client ID, client secret, and refresh token.

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenAI for providing the GPT-3.5/4 API.

Streamlit for the easy-to-use web framework.

Google for the Gmail API and OAuth 2.0 integration.

Contact
For any questions or feedback, please reach out to [Your Name] at [your.email@example.com].

Built with ❤️ using OpenAI and Streamlit.
