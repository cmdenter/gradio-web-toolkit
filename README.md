# Advanced Data Analysis Web Application

## Overview

This project is an advanced data analysis web application built with Gradio and enhanced with SEO optimization and accessibility features. It allows users to upload data, perform various analyses including linear regression and ANOVA, and visualize the results.

## Features

- Data upload via file or text input
- Data profiling and issue detection
- Linear regression analysis with visualizations
- ANOVA (Analysis of Variance)
- SEO optimization
- Accessibility enhancements
- Google Analytics and Google Ads integration
- Automatic sitemap generation

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/advanced-data-analysis-app.git
   cd advanced-data-analysis-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up environment variables (optional, but recommended for production):
   ```
   export GOOGLE_ANALYTICS_ID=your-analytics-id
   export GOOGLE_ADS_ID=your-ads-id
   export BASE_URL=https://your-app-url.com
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://localhost:7860` (or the URL provided in the console output).

4. Use the interface to upload your data and perform analyses.

## Deploying to Hugging Face Spaces

1. Create a new Space on Hugging Face and choose "Gradio" as the SDK.

2. Upload your `app.py`, `requirements.txt`, and any other necessary files to the Space.

3. In the Space settings, add the environment variables mentioned in the Usage section.

4. Your app should now be live and accessible via the Hugging Face Spaces URL!

## Customization

### SEO Optimization

To customize SEO keywords, modify the `app.optimize_seo()` call in `app.py`:

```python
app.optimize_seo(keywords=["your", "custom", "keywords"])
```

### Analytics

The app automatically includes Google Analytics and Google Ads scripts if the corresponding environment variables are set. No further action is needed.

### Accessibility

The app includes basic accessibility enhancements. To add more, you can modify the `enhance_accessibility()` method in the `gradio_web_toolkit` package.

## Troubleshooting

- If you encounter any "module not found" errors, ensure all dependencies are installed: `pip install -r requirements.txt`
- For issues with file uploads, check that you have write permissions in the app's directory.
- If analytics aren't working, verify that you've set the correct environment variables.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
