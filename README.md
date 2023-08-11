# Flask Facebook Login

Flask Facebook Login is a simple Flask web application that demonstrates how to integrate Facebook login into your Flask app. This project allows users to log in to your web application using their Facebook credentials and retrieves their name and user ID from Facebook's Graph API.

## Prerequisites

To run this project, you'll need the following:

- Python (3.6 or higher)
- Flask
- Facebook SDK (facebook-sdk)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/liad07/flask-facebook-login.git
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install flask facebook-sdk
   ```

3. Update the Facebook app credentials in `app.py`:

   ```python
   app_id = 'YOUR_APP_ID'
   app_secret = 'YOUR_APP_SECRET'
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://localhost:5000/`. Click on the "Login with Facebook" link to initiate the Facebook login flow.

## Usage

- When the user clicks the "Login with Facebook" link, they will be redirected to Facebook's authentication page to log in and grant permissions to your app.
- Upon successful login, the user will be redirected back to your app's `/callback` route, and their name will be displayed on the page.

## Contributing

We welcome contributions to improve Flask Facebook Login. If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request.



## Acknowledgments

- This project uses the [Flask](https://flask.palletsprojects.com/) web framework.
- Facebook authentication is implemented using the [facebook-sdk](https://github.com/mobolic/facebook-sdk) library.

```

Remember to replace `YOUR_APP_ID`, `YOUR_APP_SECRET`, and `YOUR_REDIRECT_URI` with your actual Facebook app credentials in the `app.py` file before sharing the project on GitHub. The README provides instructions for users to get started, explains the purpose of the project, and outlines how to contribute if others are interested in doing so.
