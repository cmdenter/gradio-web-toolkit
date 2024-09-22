from .interface_builder import create_interface
from .seo_optimizer import add_seo_metadata
from .accessibility_enhancer import enhance_accessibility

class GradioWebApp:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.interface = None
        self.seo_metadata = None
        self.accessibility_features = None

    def build_interface(self, fn, inputs, outputs):
        self.interface = create_interface(fn, inputs, outputs)

    def optimize_seo(self, keywords):
        self.seo_metadata = add_seo_metadata(self.title, self.description, keywords)

    def enhance_accessibility(self):
        self.accessibility_features = enhance_accessibility()

    def launch(self):
        if not self.interface:
            raise ValueError("Interface not built. Call build_interface first.")
        
        html = f"""
        <html>
            <head>
                {self.seo_metadata if self.seo_metadata else ''}
                <title>{self.title}</title>
            </head>
            <body>
                <h1>{self.title}</h1>
                <div id="gradio-app"></div>
                {self.accessibility_features if self.accessibility_features else ''}
            </body>
        </html>
        """
        
        self.interface.launch(inbrowser=True, html=html)
