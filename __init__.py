import gradio as gr
from .seo import optimize_seo
from .accessibility import enhance_accessibility
from .sitemap import generate_sitemap

class GradioWebApp:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.interface = None
        self.base_url = None
        self.theme = gr.themes.Base()
        self.seo_metadata = None
        self.accessibility_features = None

    def set_interface(self, interface):
        self.interface = interface

    def set_base_url(self, base_url):
        self.base_url = base_url

    def set_theme(self, theme):
        self.theme = theme

    def get_theme(self):
        return self.theme

    def optimize_seo(self, keywords):
        self.seo_metadata = optimize_seo(self.title, self.description, keywords)
        return self.seo_metadata

    def enhance_accessibility(self):
        self.accessibility_features = enhance_accessibility()
        return self.accessibility_features

    def generate_sitemap(self, pages):
        if not self.base_url:
            raise ValueError("Base URL not set. Use set_base_url() first.")
        return generate_sitemap(self.base_url, pages)

    def get_custom_html(self, analytics_script="", ads_script=""):
        custom_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{self.title}</title>
            <meta name="description" content="{self.description}">
            {self.seo_metadata if self.seo_metadata else ''}
            {analytics_script}
            {ads_script}
        </head>
        <body>
            {self.accessibility_features if self.accessibility_features else ''}
            <gradio-app></gradio-app>
        </body>
        </html>
        """
        return custom_html

    def launch(self, *args, **kwargs):
        if self.interface is None:
            raise ValueError("Interface not set. Use set_interface() first.")
        
        custom_html = kwargs.pop('custom_html', None)
        if custom_html is None:
            custom_html = self.get_custom_html()
        
        return self.interface.launch(*args, custom_html=custom_html, **kwargs)

# Compatibility with older versions
def create_interface(*args, **kwargs):
    import warnings
    warnings.warn("create_interface is deprecated. Use GradioWebApp instead.", DeprecationWarning)
    return gr.Interface(*args, **kwargs)
