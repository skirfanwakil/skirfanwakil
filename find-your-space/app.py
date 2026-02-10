from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# The Google Sheet URL converted to an export link for CSV
SHEET_ID = "1xXJznjhzh0P2Q1CLieVPDBEW3z1Az0Xbmlr5HknBqis"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        # Get data from the form
        try:
            min_budget = float(request.form.get('min_budget', 0))
            max_budget = float(request.form.get('max_budget', 0))
            hangout_type = request.form.get('hangout_type')

            # Read the Google Sheet directly into Pandas
            df = pd.read_csv(SHEET_URL)

            # Filtering Logic:
            # 1. Matches the Type
            # 2. Max Price in sheet is >= student's Min Budget
            # 3. Min Price in sheet is <= student's Max Budget
            filtered_df = df[
                (df['Type'] == hangout_type) & 
                (df['Max Price'] >= min_budget) & 
                (df['Min Price'] <= max_budget)
            ]
            
            # Convert results to a list of dictionaries for the template
            results = filtered_df.to_dict(orient='records')
        except Exception as e:
            print(f"Error: {e}")
            results = []

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
