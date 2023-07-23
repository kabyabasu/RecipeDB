from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Sample DataFrame, replace this with your actual DataFrame

data = pd.read_json("/home/kabya/utsav_data/recipedb.ndjson", lines=True, chunksize=1000)

for i in data:
    df = i
    break
    

def wrap_with_expand_button(text, cell_id):
    return f'<div id="{cell_id}">{text}</div><span class="expand-button" onclick="toggleExpand(\'{cell_id}\')">Expand</span>'



@app.route('/')
def display_dataframe():
    # Generate unique IDs for each cell in the DataFrame
    df_with_ids = df.applymap(lambda x: wrap_with_expand_button(x, f'cell-{id(x)}'))
    return render_template('index.html', table=df_with_ids.to_html(classes='table table-striped', escape=False))




if __name__ == '__main__':
    app.run(debug=True)

