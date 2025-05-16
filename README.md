# Excel Assistant - Smart Excel Analyzer with Chatbot

**Excel Assistant** is an interactive Streamlit web app that helps you upload Excel and other data files, clean and analyze the data, generate pivot tables, visualize insights with charts, and chat with your data using an AI-powered chatbot.

---

## Features

* Upload Excel (`.xlsx`, `.xls`), CSV, TXT, JSON, XML files
* Clean data: drop missing rows, fill missing values, remove duplicates, clean column names
* Generate pivot tables with custom row/column/value selections and aggregation functions
* Visualize pivot tables as bar charts
* Ask questions about your dataset via AI-powered chatbot (using OpenRouter Llama 3.3 8B Instruct model)
* User-friendly interface with step-by-step data exploration

---

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/excel-assistant.git
   cd excel-assistant
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenRouter API key:

   Create a `.streamlit/secrets.toml` file with the following content:

   ```toml
   OPENROUTER_API_KEY = "your_openrouter_api_key_here"
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Upload your Excel or data file, clean and analyze the data, generate pivot tables, visualize charts, and chat with the AI to get insights.

---

## Folder Structure

```
.
├── app.py               # Main Streamlit app
├── chatbot.py           # Chatbot UI and OpenRouter API integration
├── data_cleaning.py     # Data cleaning functions
├── pivot_generator.py   # Pivot table generation
├── graph_visualizer.py  # Plotting and visualization
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Requests
* OpenRouter API (Llama 3.3 8B Instruct model)

---

## Troubleshooting

* **401 Unauthorized Error:** Make sure your OpenRouter API key is valid and correctly added in `.streamlit/secrets.toml`.
* **Unsupported File Type:** Only Excel, CSV, TXT, JSON, XML files are supported.
* For other issues, please raise an issue on GitHub.

---

## License

This project is licensed under the MIT License.

---

**Enjoy your smart data analysis with Excel Assistant! 🚀**

