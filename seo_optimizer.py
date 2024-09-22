def add_seo_metadata(title, description, keywords):
    return f"""
    <meta name="description" content="{description}">
    <meta name="keywords" content="{', '.join(keywords)}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    """
