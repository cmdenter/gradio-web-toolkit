import xml.etree.ElementTree as ET
from datetime import datetime

def generate_sitemap(base_url, pages):
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for page in pages:
        url = ET.SubElement(root, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = f"{base_url}/{page}"
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = datetime.now().strftime("%Y-%m-%d")
    
    return ET.tostring(root, encoding="unicode")
