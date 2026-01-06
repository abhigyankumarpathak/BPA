from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# EDIT YOUR CONTENT HERE - REPLACE ALL PLACEHOLDER TEXT
# ==========================================

# Landing Page Content
HERO_NAME = "[Leader's Full Name]"
HERO_TITLE = "[Their Role/Title in Community]"
HERO_QUOTE = "[Inspiring quote about their mission or values]"
HERO_SUBTITLE = "Empowering Communities Through Leadership and Service"
HERO_IMAGE = "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=800"

# Contact Information (for footer)
CONTACT_EMAIL = "contact@example.com"
CONTACT_PHONE = "(555) 123-4567"
SOCIAL_LINKS = {
    "linkedin": "#",
    "twitter": "#",
    "facebook": "#"
}

# Early Life Content
EARLY_LIFE = {
    "title": "Early Life",
    "content": """
    [Write about where they were born and grew up]
    [Describe their childhood environment and family background]
    [Mention early experiences that shaped their character]
    [Include any challenges they faced growing up]
    [Explain what inspired them from a young age]
    """,
    "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=800&q=80"
}

# Education Content
EDUCATION = {
    "title": "Education",
    "content": """
    [List their educational background chronologically]
    • [High School Name and Year]
    • [College/University - Degree - Year]
    • [Graduate School - Degree - Year]
    • [Any certifications or special training]
    
    [Describe their academic journey and achievements]
    [Mention any scholarships, honors, or obstacles overcome]
    [Explain how their education prepared them for their work]
    """,
    "image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&q=80"
}

# Family Content
FAMILY = {
    "title": "Family",
    "content": """
    [Describe their family structure]
    [Mention spouse/partner if applicable]
    [Talk about children if they have any]
    [Explain how family influences their work]
    [Describe family involvement in community service]
    [Share how they balance family and community leadership]
    """,
    "image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=800&q=80"
}

# Career Content
CAREER = {
    "title": "Career",
    "content": """
    [List their career progression chronologically]
    • [First Job/Position - Years]
    • [Second Position - Years]
    • [Current Position - Years]
    
    [Describe their professional journey]
    [Explain key responsibilities in each role]
    [Highlight major projects or initiatives they led]
    [Discuss their leadership style and approach]
    [Mention organizations they've worked with]
    """,
    "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80"
}

# Contributions Content
CONTRIBUTIONS = {
    "title": "Significant Contributions",
    "content": """
    [List their major contributions to the community]
    • [First major contribution - impact/numbers]
    • [Second major contribution - impact/numbers]
    • [Third major contribution - impact/numbers]
    • [Fourth major contribution - impact/numbers]
    • [Fifth major contribution - impact/numbers]
    
    [Describe the lasting impact of their work]
    [Explain how they've changed the community for the better]
    """,
    "image": "https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?w=800&q=80"
}

# Awards Content
AWARDS = {
    "title": "Awards, Honors & Achievements",
    "content": """
    [List all awards and honors received]
    • [Award Name - Organization - Year]
    • [Award Name - Organization - Year]
    • [Award Name - Organization - Year]
    • [Honor/Recognition - Organization - Year]
    • [Achievement - Description - Year]
    
    [Describe what these recognitions mean]
    [Explain the significance of major awards]
    """,
    "image": "https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?w=800&q=80"
}

# Community Connections Content
COMMUNITY = {
    "title": "Community Connections",
    "content": """
    [Describe their involvement in community organizations]
    
    Board memberships and leadership roles:
    • [Organization Name - Role]
    • [Organization Name - Role]
    • [Organization Name - Role]
    
    [Explain how they connect with community members]
    [Describe their accessibility and engagement style]
    [Mention regular community events they attend or host]
    """,
    "image": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800&q=80"
}

# Philanthropy Content
PHILANTHROPY = {
    "title": "Philanthropy",
    "content": """
    [Describe their charitable work and donations]
    [Mention organizations or causes they support financially]
    [Explain programs or funds they've established]
    [Describe volunteer work they regularly do]
    [Share their philosophy on giving back]
    [Include quotes about why philanthropy matters to them]
    
    [Add specific examples of philanthropic impact with numbers if possible]
    """,
    "image": "https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?w=800&q=80"
}

# ==========================================
# HTML TEMPLATE WITH MODERN DESIGN
# ==========================================


def get_base_html(content, title, current_page, hero_image):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Community Leader Biography</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- AOS Animation Library -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <style>
        :root {{
            --primary-color: #1A73E8;
            --secondary-color: #0F4C81;
            --accent-color: #F4B400;
            --text-dark: #1a202c;
            --text-medium: #4a5568;
            --text-light: #718096;
            --background: #ffffff;
            --background-alt: #f7fafc;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.1);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
            --border-radius: 12px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        [data-theme="dark"] {{
            --primary-color: #4A9EFF;
            --secondary-color: #2D5F8D;
            --accent-color: #FFD166;
            --text-dark: #e2e8f0;
            --text-medium: #cbd5e0;
            --text-light: #a0aec0;
            --background: #1a202c;
            --background-alt: #2d3748;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.5);
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html {{
            scroll-behavior: smooth;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background: var(--background);
            transition: background 0.3s ease, color 0.3s ease;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            line-height: 1.2;
        }}
        
        /* Loading Animation */
        .page-loader {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--background);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            transition: opacity 0.5s, visibility 0.5s;
        }}
        
        .page-loader.hidden {{
            opacity: 0;
            visibility: hidden;
        }}
        
        .loader {{
            width: 50px;
            height: 50px;
            border: 4px solid var(--primary-color);
            border-top-color: transparent;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}
        
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
        
        /* Fixed Navigation Bar */
        .navbar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px) saturate(180%);
            box-shadow: var(--shadow-sm);
            z-index: 1000;
            transition: var(--transition);
            padding: 1rem 0;
        }}
        
        [data-theme="dark"] .navbar {{
            background: rgba(26, 32, 44, 0.95);
        }}
        
        .navbar.scrolled {{
            padding: 0.5rem 0;
            box-shadow: var(--shadow-md);
        }}
        
        .nav-container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .nav-logo {{
            font-family: 'Montserrat', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--primary-color);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .nav-menu {{
            display: flex;
            list-style: none;
            gap: 0.5rem;
            align-items: center;
        }}
        
        .nav-link {{
            color: var(--text-medium);
            text-decoration: none;
            font-weight: 500;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            transition: var(--transition);
            position: relative;
        }}
        
        .nav-link:hover {{
            color: var(--primary-color);
            background: rgba(26, 115, 232, 0.08);
        }}
        
        .nav-link.active {{
            color: var(--primary-color);
            font-weight: 600;
            background: rgba(26, 115, 232, 0.12);
        }}
        
        .nav-link.active::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 1.25rem;
            right: 1.25rem;
            height: 2px;
            background: var(--primary-color);
            border-radius: 2px 2px 0 0;
        }}
        
        /* Dark Mode Toggle */
        .theme-toggle {{
            background: none;
            border: 2px solid var(--text-light);
            color: var(--text-medium);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
            font-size: 1.2rem;
        }}
        
        .theme-toggle:hover {{
            border-color: var(--primary-color);
            color: var(--primary-color);
            transform: rotate(20deg);
        }}
        
        /* Mobile Menu Toggle */
        .menu-toggle {{
            display: none;
            background: none;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
            z-index: 1001;
        }}
        
        .menu-toggle span {{
            display: block;
            width: 28px;
            height: 3px;
            background: var(--text-dark);
            margin: 5px 0;
            transition: var(--transition);
            border-radius: 3px;
        }}
        
        .menu-toggle.active span:nth-child(1) {{
            transform: rotate(45deg) translate(7px, 7px);
        }}
        
        .menu-toggle.active span:nth-child(2) {{
            opacity: 0;
            transform: translateX(-20px);
        }}
        
        .menu-toggle.active span:nth-child(3) {{
            transform: rotate(-45deg) translate(7px, -7px);
        }}
        
        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 10rem 2rem 6rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            margin-top: 70px;
        }}
        
        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('{hero_image}') center/cover;
            opacity: 0.12;
            z-index: 0;
        }}
        
        .hero::after {{
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            border-radius: 50%;
            z-index: 0;
        }}
        
        .hero-content {{
            position: relative;
            z-index: 1;
            max-width: 900px;
            margin: 0 auto;
        }}
        
        .hero h1 {{
            font-size: 4rem;
            margin-bottom: 1rem;
            text-shadow: 2px 4px 12px rgba(0,0,0,0.2);
            font-weight: 800;
            letter-spacing: -1px;
        }}
        
        .hero h2 {{
            font-size: 1.8rem;
            margin-bottom: 2rem;
            font-weight: 400;
            opacity: 0.95;
            letter-spacing: 0.5px;
        }}
        
        .hero-subtitle {{
            font-size: 1.3rem;
            margin-bottom: 2.5rem;
            opacity: 0.9;
        }}
        
        .hero-quote {{
            font-size: 1.4rem;
            font-style: italic;
            padding: 2.5rem 3rem;
            background: rgba(255,255,255,0.15);
            border-radius: var(--border-radius);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: var(--shadow-lg);
            max-width: 700px;
            margin: 0 auto 2rem;
        }}
        
        .cta-button {{
            display: inline-block;
            background: white;
            color: var(--primary-color);
            padding: 1rem 2.5rem;
            border-radius: var(--border-radius);
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            box-shadow: var(--shadow-md);
            margin-top: 1rem;
        }}
        
        .cta-button:hover {{
            transform: translateY(-3px);
            box-shadow: var(--shadow-lg);
            background: var(--accent-color);
        }}
        
        /* Content Sections */
        .content-section {{
            max-width: 1300px;
            margin: 0 auto;
            padding: 80px 2rem;
        }}
        
        .section-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }}
        
        .section-content.reverse {{
            direction: rtl;
        }}
        
        .section-content.reverse > * {{
            direction: ltr;
        }}
        
        .section-text h2 {{
            font-size: 3rem;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2rem;
            font-weight: 800;
            letter-spacing: -1px;
            line-height: 1.2;
        }}
        
        .section-text p {{
            font-size: 1.15rem;
            margin-bottom: 1.5rem;
            white-space: pre-line;
            color: var(--text-medium);
            line-height: 1.7;
        }}
        
        .section-image {{
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            position: relative;
        }}
        
        .section-image::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(26, 115, 232, 0.1) 0%, rgba(15, 76, 129, 0.1) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 1;
        }}
        
        .section-image:hover {{
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
        }}
        
        .section-image:hover::before {{
            opacity: 1;
        }}
        
        .section-image img {{
            width: 100%;
            height: 450px;
            object-fit: cover;
            display: block;
            transition: transform 0.5s ease;
        }}
        
        .section-image:hover img {{
            transform: scale(1.05);
        }}
        
        /* Intro Section (Home Page) */
        .intro-section {{
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 30px;
            background: var(--background-alt);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
        }}
        
        .intro-section h2 {{
            font-size: 2.8rem;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2rem;
            font-weight: 800;
        }}
        
        .intro-section p {{
            font-size: 1.25rem;
            line-height: 1.8;
            color: var(--text-medium);
        }}
        
        /* Footer */
        footer {{
            background: linear-gradient(135deg, var(--text-dark) 0%, #2d3748 100%);
            color: white;
            padding: 60px 2rem 30px;
            margin-top: 80px;
        }}
        
        .footer-content {{
            max-width: 1300px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 50px;
            margin-bottom: 40px;
        }}
        
        .footer-section h3 {{
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            color: var(--accent-color);
        }}
        
        .footer-section p {{
            line-height: 1.8;
            opacity: 0.9;
            margin-bottom: 1rem;
        }}
        
        .footer-links {{
            list-style: none;
        }}
        
        .footer-links li {{
            margin-bottom: 0.75rem;
        }}
        
        .footer-links a {{
            color: white;
            text-decoration: none;
            opacity: 0.85;
            transition: var(--transition);
            display: inline-block;
        }}
        
        .footer-links a:hover {{
            opacity: 1;
            color: var(--accent-color);
            transform: translateX(5px);
        }}
        
        .social-icons {{
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }}
        
        .social-icons a {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
            color: white;
            text-decoration: none;
            transition: var(--transition);
            font-size: 1.2rem;
        }}
        
        .social-icons a:hover {{
            background: var(--accent-color);
            color: var(--text-dark);
            transform: translateY(-3px);
        }}
        
        .footer-bottom {{
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255,255,255,0.1);
            opacity: 0.8;
        }}
        
        /* Scroll to Top Button */
        .scroll-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-md);
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
            z-index: 999;
        }}
        
        .scroll-top.visible {{
            opacity: 1;
            visibility: visible;
        }}
        
        .scroll-top:hover {{
            background: var(--secondary-color);
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
        }}
        
        /* Responsive Design */
        @media (max-width: 968px) {{
            .nav-menu {{
                position: fixed;
                top: 0;
                right: -100%;
                width: 300px;
                height: 100vh;
                background: var(--background);
                flex-direction: column;
                padding: 100px 0 30px;
                box-shadow: -5px 0 25px rgba(0,0,0,0.1);
                transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                overflow-y: auto;
                gap: 0;
            }}
            
            .nav-menu.active {{
                right: 0;
            }}
            
            .nav-menu li {{
                width: 100%;
            }}
            
            .nav-link {{
                display: block;
                padding: 1.2rem 2rem;
                border-radius: 0;
            }}
            
            .nav-link.active::after {{
                left: 0;
                right: auto;
                width: 4px;
                height: 100%;
                top: 0;
                bottom: 0;
                border-radius: 0 4px 4px 0;
            }}
            
            .menu-toggle {{
                display: block;
            }}
            
            .hero {{
                padding: 8rem 1.5rem 4rem;
            }}
            
            .hero h1 {{
                font-size: 2.5rem;
            }}
            
            .hero h2 {{
                font-size: 1.3rem;
            }}
            
            .hero-subtitle {{
                font-size: 1.1rem;
            }}
            
            .hero-quote {{
                font-size: 1.1rem;
                padding: 1.5rem 2rem;
            }}
            
            .content-section {{
                padding: 50px 1.5rem;
            }}
            
            .section-content {{
                grid-template-columns: 1fr;
                gap: 30px;
            }}
            
            .section-content.reverse {{
                direction: ltr;
            }}
            
            .section-text h2 {{
                font-size: 2.2rem;
            }}
            
            .section-image img {{
                height: 300px;
            }}
            
            .footer-content {{
                grid-template-columns: 1fr;
                gap: 30px;
            }}
            
            .intro-section h2 {{
                font-size: 2rem;
            }}
            
            .intro-section p {{
                font-size: 1.1rem;
            }}
        }}
        
        @media (max-width: 480px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .nav-logo {{
                font-size: 1.2rem;
            }}
            
            .cta-button {{
                padding: 0.875rem 2rem;
                font-size: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <!-- Page Loader -->
    <div class="page-loader">
        <div class="loader"></div>
    </div>
    
    <!-- Fixed Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="/" class="nav-logo">
                <i class="fas fa-star"></i>
                {HERO_NAME.split()[0] if HERO_NAME and HERO_NAME != "[Leader's Full Name]" else "Leader"}
            </a>
            
            <button class="menu-toggle" id="menuToggle" onclick="toggleMenu()" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <ul class="nav-menu" id="navMenu">
                <li><a href="/" class="nav-link {'active' if current_page == 'home' else ''}" onclick="closeMenu()">Home</a></li>
                <li><a href="/early-life" class="nav-link {'active' if current_page == 'early-life' else ''}" onclick="closeMenu()">Early Life</a></li>
                <li><a href="/education" class="nav-link {'active' if current_page == 'education' else ''}" onclick="closeMenu()">Education</a></li>
                <li><a href="/family" class="nav-link {'active' if current_page == 'family' else ''}" onclick="closeMenu()">Family</a></li>
                <li><a href="/career" class="nav-link {'active' if current_page == 'career' else ''}" onclick="closeMenu()">Career</a></li>
                <li><a href="/contributions" class="nav-link {'active' if current_page == 'contributions' else ''}" onclick="closeMenu()">Contributions</a></li>
                <li><a href="/awards" class="nav-link {'active' if current_page == 'awards' else ''}" onclick="closeMenu()">Awards</a></li>
                <li><a href="/community" class="nav-link {'active' if current_page == 'community' else ''}" onclick="closeMenu()">Community</a></li>
                <li><a href="/philanthropy" class="nav-link {'active' if current_page == 'philanthropy' else ''}" onclick="closeMenu()">Philanthropy</a></li>
                <li>
                    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode">
                        <i class="fas fa-moon" id="themeIcon"></i>
                    </button>
                </li>
            </ul>
        </div>
    </nav>
    
    {content}
    
    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>About This Project</h3>
                <p>This biography celebrates the remarkable contributions of {HERO_NAME if HERO_NAME != "[Leader's Full Name]" else "a community leader"} and their lasting impact on our community.</p>
                <div class="social-icons">
                    <a href="{SOCIAL_LINKS['linkedin']}" aria-label="LinkedIn" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    <a href="{SOCIAL_LINKS['twitter']}" aria-label="Twitter" title="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="{SOCIAL_LINKS['facebook']}" aria-label="Facebook" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
            
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul class="footer-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/early-life">Early Life</a></li>
                    <li><a href="/education">Education</a></li>
                    <li><a href="/career">Career</a></li>
                    <li><a href="/contributions">Contributions</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h3>Contact</h3>
                <p><i class="fas fa-envelope"></i> {CONTACT_EMAIL}</p>
                <p><i class="fas fa-phone"></i> {CONTACT_PHONE}</p>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>&copy; 2024 Community Leader Biography Project | BPA Website Design Team</p>
            <p>Created with dedication to celebrate local leadership</p>
        </div>
    </footer>
    
    <!-- Scroll to Top Button -->
    <button class="scroll-top" id="scrollTop" onclick="scrollToTop()" aria-label="Scroll to top">
        <i class="fas fa-arrow-up"></i>
    </button>
    
    <!-- AOS Animation Library -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    
    <script>
        // Initialize AOS animations
        AOS.init({{
            duration: 800,
            once: true,
            offset: 100
        }});
        
        // Page Loader
        window.addEventListener('load', function() {{
            setTimeout(function() {{
                document.querySelector('.page-loader').classList.add('hidden');
            }}, 500);
        }});
        
        // Mobile Menu Toggle
        function toggleMenu() {{
            const navMenu = document.getElementById('navMenu');
            const menuToggle = document.getElementById('menuToggle');
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        }}
        
        function closeMenu() {{
            const navMenu = document.getElementById('navMenu');
            const menuToggle = document.getElementById('menuToggle');
            navMenu.classList.remove('active');
            menuToggle.classList.remove('active');
        }}
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {{
            const navMenu = document.getElementById('navMenu');
            const menuToggle = document.getElementById('menuToggle');
            const navbar = document.getElementById('navbar');
            
            if (!navbar.contains(event.target) && navMenu.classList.contains('active')) {{
                closeMenu();
            }}
        }});
        
        // Navbar scroll effect
        let lastScroll = 0;
        window.addEventListener('scroll', function() {{
            const navbar = document.getElementById('navbar');
            const scrollTop = document.getElementById('scrollTop');
            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 100) {{
                navbar.classList.add('scrolled');
            }} else {{
                navbar.classList.remove('scrolled');
            }}
            
            // Show/hide scroll to top button
            if (currentScroll > 300) {{
                scrollTop.classList.add('visible');
            }} else {{
                scrollTop.classList.remove('visible');
            }}
            
            lastScroll = currentScroll;
        }});
        
        // Scroll to top function
        function scrollToTop() {{
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }}
        
        // Dark mode toggle
        function toggleTheme() {{
            const html = document.documentElement;
            const themeIcon = document.getElementById('themeIcon');
            const currentTheme = html.getAttribute('data-theme');
            
            if (currentTheme === 'dark') {{
                html.removeAttribute('data-theme');
                themeIcon.className = 'fas fa-moon';
                localStorage.setItem('theme', 'light');
            }} else {{
                html.setAttribute('data-theme', 'dark');
                themeIcon.className = 'fas fa-sun';
                localStorage.setItem('theme', 'dark');
            }}
        }}
        
        // Load saved theme
        window.addEventListener('DOMContentLoaded', function() {{
            const savedTheme = localStorage.getItem('theme');
            const themeIcon = document.getElementById('themeIcon');
            
            if (savedTheme === 'dark') {{
                document.documentElement.setAttribute('data-theme', 'dark');
                themeIcon.className = 'fas fa-sun';
            }}
        }});
    </script>
</body>
</html>
"""
    return get_base_html(content, title, current_page, hero_image)

# ==========================================
# FLASK ROUTES
# ==========================================


@app.route('/')
def home():
    content = """
    <div class="hero">
        <div class="hero-content" data-aos="fade-up">
            <h1>""" + HERO_NAME + """</h1>
            <h2>""" + HERO_TITLE + """</h2>
            <p class="hero-subtitle">""" + HERO_SUBTITLE + """</p>
            <div class="hero-quote">
                \"""" + HERO_QUOTE + """\"
            </div>
            <a href="#intro" class="cta-button">Learn More</a>
        </div>
    </div>
    
    <div class="content-section" id="intro">
        <div class="intro-section" data-aos="fade-up">
            <h2>A Legacy of Service</h2>
            <p>
                [Write a compelling introduction about this community leader. 
                Describe their overall impact, what makes them special, and why 
                their story matters. This should capture the reader's attention 
                and inspire them to learn more about this remarkable individual's journey.]
            </p>
        </div>
    </div>
    
    <!-- Impact Statistics -->
    <div class="content-section">
        <div class="stats-grid" data-aos="fade-up">
            <div class="stat-card">
                <i class="fas fa-users"></i>
                <div class="stat-number" data-target="1500">0</div>
                <div class="stat-label">Lives Impacted</div>
            </div>
            <div class="stat-card">
                <i class="fas fa-award"></i>
                <div class="stat-number" data-target="25">0</div>
                <div class="stat-label">Awards Received</div>
            </div>
            <div class="stat-card">
                <i class="fas fa-calendar"></i>
                <div class="stat-number" data-target="15">0</div>
                <div class="stat-label">Years of Service</div>
            </div>
            <div class="stat-card">
                <i class="fas fa-heart"></i>
                <div class="stat-number" data-target="50">0</div>
                <div class="stat-label">Community Programs</div>
            </div>
        </div>
    </div>
    
    <style>
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .stat-card {
            background: var(--background-alt);
            padding: 40px 30px;
            border-radius: var(--border-radius);
            text-align: center;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            border: 2px solid transparent;
        }
        
        .stat-card:hover {
            transform: translateY(-10px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-color);
        }
        
        .stat-card i {
            font-size: 3rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }
        
        .stat-number {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }
        
        .stat-label {
            font-size: 1.1rem;
            color: var(--text-medium);
            font-weight: 600;
        }
    </style>
    
    <script>
        // Animated counter for statistics
        function animateCounter(element) {
            const target = parseInt(element.getAttribute('data-target'));
            const duration = 2000;
            const increment = target / (duration / 16);
            let current = 0;
            
            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    element.textContent = Math.floor(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    element.textContent = target;
                }
            };
            
            updateCounter();
        }
        
        // Trigger counters when stats section is in view
        const observerOptions = {
            threshold: 0.5
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counters = entry.target.querySelectorAll('.stat-number');
                    counters.forEach(counter => {
                        if (counter.textContent === '0') {
                            animateCounter(counter);
                        }
                    });
                }
            });
        }, observerOptions);
        
        document.addEventListener('DOMContentLoaded', () => {
            const statsGrid = document.querySelector('.stats-grid');
            if (statsGrid) {
                observer.observe(statsGrid);
            }
        });
    </script>
    """
    return get_base_html(content, "Home", "home", HERO_IMAGE)


@app.route('/early-life')
def early_life():
    content = f"""
    <div class="content-section">
        <div class="section-content">
            <div class="section-text" data-aos="fade-right">
                <h2>{EARLY_LIFE['title']}</h2>
                <p>{EARLY_LIFE['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-left">
                <img src="{EARLY_LIFE['image']}" alt="{EARLY_LIFE['title']} - Childhood and formative years">
            </div>
        </div>
    </div>
    
    <!-- Interactive Timeline -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Key Milestones</h2>
        <div class="timeline" data-aos="fade-up">
            <div class="timeline-item" data-aos="fade-right" data-aos-delay="100">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <div class="timeline-year">19XX</div>
                    <h3>Born in [City, State]</h3>
                    <p>[Add brief description of birthplace and early environment]</p>
                </div>
            </div>
            <div class="timeline-item" data-aos="fade-right" data-aos-delay="200">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <div class="timeline-year">19XX</div>
                    <h3>First Community Involvement</h3>
                    <p>[Describe their first experience with community service]</p>
                </div>
            </div>
            <div class="timeline-item" data-aos="fade-right" data-aos-delay="300">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <div class="timeline-year">19XX</div>
                    <h3>Formative Experience</h3>
                    <p>[Describe a key moment that shaped their future path]</p>
                </div>
            </div>
        </div>
    </div>
    
    <style>
        .section-title {{
            font-size: 2.8rem;
            text-align: center;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 3rem;
            font-weight: 800;
        }}
        
        .timeline {{
            position: relative;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px 0;
        }}
        
        .timeline::before {{
            content: '';
            position: absolute;
            left: 30px;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(180deg, var(--primary-color), var(--accent-color));
            border-radius: 2px;
        }}
        
        .timeline-item {{
            position: relative;
            margin-bottom: 50px;
            padding-left: 80px;
        }}
        
        .timeline-dot {{
            position: absolute;
            left: 18px;
            top: 0;
            width: 28px;
            height: 28px;
            background: var(--primary-color);
            border: 4px solid var(--background);
            border-radius: 50%;
            box-shadow: 0 0 0 4px var(--primary-color);
            transition: var(--transition);
            cursor: pointer;
        }}
        
        .timeline-item:hover .timeline-dot {{
            transform: scale(1.3);
            box-shadow: 0 0 0 8px rgba(26, 115, 232, 0.3);
        }}
        
        .timeline-content {{
            background: var(--background-alt);
            padding: 25px 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            cursor: pointer;
        }}
        
        .timeline-content:hover {{
            transform: translateX(10px);
            box-shadow: var(--shadow-md);
        }}
        
        .timeline-year {{
            display: inline-block;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }}
        
        .timeline-content h3 {{
            font-size: 1.5rem;
            color: var(--text-dark);
            margin-bottom: 10px;
        }}
        
        .timeline-content p {{
            color: var(--text-medium);
            line-height: 1.6;
        }}
        
        @media (max-width: 768px) {{
            .timeline::before {{
                left: 20px;
            }}
            
            .timeline-dot {{
                left: 8px;
            }}
            
            .timeline-item {{
                padding-left: 60px;
            }}
        }}
    </style>
    """
    return get_base_html(content, "Early Life", "early-life", HERO_IMAGE)


@app.route('/education')
def education():
    content = f"""
    <div class="content-section">
        <div class="section-content reverse">
            <div class="section-text" data-aos="fade-left">
                <h2>{EDUCATION['title']}</h2>
                <p>{EDUCATION['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-right">
                <img src="{EDUCATION['image']}" alt="{EDUCATION['title']} - Academic achievements and learning journey">
            </div>
        </div>
    </div>
    
    <!-- Interactive Education Cards -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Academic Journey</h2>
        <div class="education-grid">
            <div class="education-card" data-aos="flip-left" data-aos-delay="100">
                <div class="education-icon">
                    <i class="fas fa-school"></i>
                </div>
                <h3>High School</h3>
                <div class="education-school">[School Name]</div>
                <div class="education-year">19XX - 19XX</div>
                <p>[Notable achievements, activities, or honors]</p>
                <div class="education-badge">Graduated</div>
            </div>
            
            <div class="education-card" data-aos="flip-left" data-aos-delay="200">
                <div class="education-icon">
                    <i class="fas fa-graduation-cap"></i>
                </div>
                <h3>Bachelor's Degree</h3>
                <div class="education-school">[University Name]</div>
                <div class="education-year">19XX - 19XX</div>
                <p>[Major/Minor, GPA, honors, activities]</p>
                <div class="education-badge">B.A./B.S.</div>
            </div>
            
            <div class="education-card" data-aos="flip-left" data-aos-delay="300">
                <div class="education-icon">
                    <i class="fas fa-user-graduate"></i>
                </div>
                <h3>Graduate School</h3>
                <div class="education-school">[University Name]</div>
                <div class="education-year">19XX - 19XX</div>
                <p>[Advanced degree, research, specialization]</p>
                <div class="education-badge">M.A./Ph.D.</div>
            </div>
        </div>
    </div>
    
    <style>
        .education-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .education-card {{
            background: var(--background-alt);
            padding: 35px 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }}
        
        .education-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }}
        
        .education-card:hover {{
            transform: translateY(-10px);
            box-shadow: var(--shadow-lg);
        }}
        
        .education-card:hover::before {{
            transform: scaleX(1);
        }}
        
        .education-icon {{
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            transition: var(--transition);
        }}
        
        .education-card:hover .education-icon {{
            transform: rotateY(360deg);
        }}
        
        .education-icon i {{
            font-size: 2.5rem;
            color: white;
        }}
        
        .education-card h3 {{
            font-size: 1.5rem;
            color: var(--text-dark);
            margin-bottom: 10px;
            text-align: center;
        }}
        
        .education-school {{
            font-weight: 600;
            color: var(--primary-color);
            text-align: center;
            margin-bottom: 5px;
        }}
        
        .education-year {{
            text-align: center;
            color: var(--text-light);
            font-size: 0.95rem;
            margin-bottom: 15px;
        }}
        
        .education-card p {{
            color: var(--text-medium);
            line-height: 1.6;
            text-align: center;
            margin-bottom: 20px;
        }}
        
        .education-badge {{
            display: inline-block;
            background: var(--accent-color);
            color: var(--text-dark);
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
        }}
    </style>
    """
    return get_base_html(content, "Education", "education", HERO_IMAGE)


@app.route('/family')
def family():
    content = f"""
    <div class="content-section">
        <div class="section-content">
            <div class="section-text" data-aos="fade-right">
                <h2>{FAMILY['title']}</h2>
                <p>{FAMILY['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-left">
                <img src="{FAMILY['image']}" alt="{FAMILY['title']} - Family life and relationships">
            </div>
        </div>
    </div>
    
    <!-- Interactive Family Values -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Family Values</h2>
        <div class="values-container">
            <div class="value-card" data-aos="zoom-in" data-aos-delay="100">
                <div class="value-icon">
                    <i class="fas fa-hands-helping"></i>
                </div>
                <h3>Service</h3>
                <p>Commitment to helping others and making a difference in the community</p>
            </div>
            
            <div class="value-card" data-aos="zoom-in" data-aos-delay="200">
                <div class="value-icon">
                    <i class="fas fa-heart"></i>
                </div>
                <h3>Compassion</h3>
                <p>Deep empathy and care for those in need throughout the community</p>
            </div>
            
            <div class="value-card" data-aos="zoom-in" data-aos-delay="300">
                <div class="value-icon">
                    <i class="fas fa-book"></i>
                </div>
                <h3>Education</h3>
                <p>Belief in lifelong learning and empowering others through knowledge</p>
            </div>
            
            <div class="value-card" data-aos="zoom-in" data-aos-delay="400">
                <div class="value-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3>Unity</h3>
                <p>Bringing people together and fostering strong community connections</p>
            </div>
        </div>
    </div>
    
    <style>
        .values-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .value-card {{
            background: var(--background);
            padding: 40px 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            text-align: center;
            transition: var(--transition);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }}
        
        .value-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(26, 115, 232, 0.1), transparent);
            transition: left 0.6s ease;
        }}
        
        .value-card:hover {{
            transform: translateY(-10px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-color);
        }}
        
        .value-card:hover::before {{
            left: 100%;
        }}
        
        .value-icon {{
            width: 90px;
            height: 90px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            transition: var(--transition);
            position: relative;
            z-index: 1;
        }}
        
        .value-card:hover .value-icon {{
            transform: scale(1.1) rotate(10deg);
        }}
        
        .value-icon i {{
            font-size: 2.5rem;
            color: white;
        }}
        
        .value-card h3 {{
            font-size: 1.6rem;
            color: var(--text-dark);
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
        }}
        
        .value-card p {{
            color: var(--text-medium);
            line-height: 1.6;
            position: relative;
            z-index: 1;
        }}
    </style>
    """
    return get_base_html(content, "Family", "family", HERO_IMAGE)


@app.route('/career')
def career():
    content = f"""
    <div class="content-section">
        <div class="section-content reverse">
            <div class="section-text" data-aos="fade-left">
                <h2>{CAREER['title']}</h2>
                <p>{CAREER['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-right">
                <img src="{CAREER['image']}" alt="{CAREER['title']} - Professional journey and leadership roles">
            </div>
        </div>
    </div>
    
    <!-- Interactive Career Path -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Career Progression</h2>
        <div class="career-path">
            <div class="career-step" data-aos="fade-up" data-aos-delay="100">
                <div class="career-number">1</div>
                <div class="career-info">
                    <h3>[First Position Title]</h3>
                    <div class="career-company">[Company/Organization]</div>
                    <div class="career-years">20XX - 20XX</div>
                    <p>[Brief description of role and key achievements]</p>
                    <div class="career-skills">
                        <span class="skill-tag">Leadership</span>
                        <span class="skill-tag">Management</span>
                        <span class="skill-tag">Strategy</span>
                    </div>
                </div>
            </div>
            
            <div class="career-step" data-aos="fade-up" data-aos-delay="200">
                <div class="career-number">2</div>
                <div class="career-info">
                    <h3>[Second Position Title]</h3>
                    <div class="career-company">[Company/Organization]</div>
                    <div class="career-years">20XX - 20XX</div>
                    <p>[Brief description of role and key achievements]</p>
                    <div class="career-skills">
                        <span class="skill-tag">Innovation</span>
                        <span class="skill-tag">Team Building</span>
                        <span class="skill-tag">Growth</span>
                    </div>
                </div>
            </div>
            
            <div class="career-step" data-aos="fade-up" data-aos-delay="300">
                <div class="career-number">3</div>
                <div class="career-info">
                    <h3>[Current Position Title]</h3>
                    <div class="career-company">[Company/Organization]</div>
                    <div class="career-years">20XX - Present</div>
                    <p>[Brief description of current role and ongoing impact]</p>
                    <div class="career-skills">
                        <span class="skill-tag">Vision</span>
                        <span class="skill-tag">Transformation</span>
                        <span class="skill-tag">Excellence</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <style>
        .career-path {{
            max-width: 900px;
            margin: 0 auto;
        }}
        
        .career-step {{
            display: flex;
            gap: 30px;
            margin-bottom: 50px;
            position: relative;
        }}
        
        .career-step:not(:last-child)::after {{
            content: '';
            position: absolute;
            left: 35px;
            top: 80px;
            bottom: -50px;
            width: 3px;
            background: linear-gradient(180deg, var(--primary-color), var(--accent-color));
            opacity: 0.3;
        }}
        
        .career-number {{
            min-width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: 800;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            flex-shrink: 0;
        }}
        
        .career-step:hover .career-number {{
            transform: scale(1.15) rotate(10deg);
            box-shadow: var(--shadow-lg);
        }}
        
        .career-info {{
            flex: 1;
            background: var(--background-alt);
            padding: 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            cursor: pointer;
        }}
        
        .career-info:hover {{
            transform: translateX(10px);
            box-shadow: var(--shadow-md);
        }}
        
        .career-info h3 {{
            font-size: 1.6rem;
            color: var(--text-dark);
            margin-bottom: 10px;
        }}
        
        .career-company {{
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: 5px;
        }}
        
        .career-years {{
            color: var(--text-light);
            font-size: 0.95rem;
            margin-bottom: 15px;
        }}
        
        .career-info p {{
            color: var(--text-medium);
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        
        .career-skills {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .skill-tag {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            transition: var(--transition);
        }}
        
        .skill-tag:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(26, 115, 232, 0.4);
        }}
        
        @media (max-width: 768px) {{
            .career-step {{
                flex-direction: column;
                gap: 20px;
            }}
            
            .career-step:not(:last-child)::after {{
                left: 35px;
                top: 90px;
            }}
        }}
    </style>
    """
    return get_base_html(content, "Career", "career", HERO_IMAGE)


@app.route('/contributions')
def contributions():
    content = f"""
    <div class="content-section">
        <div class="section-content">
            <div class="section-text" data-aos="fade-right">
                <h2>{CONTRIBUTIONS['title']}</h2>
                <p>{CONTRIBUTIONS['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-left">
                <img src="{CONTRIBUTIONS['image']}" alt="{CONTRIBUTIONS['title']} - Community impact and achievements">
            </div>
        </div>
    </div>
    
    <!-- Interactive Contributions Grid -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Major Contributions</h2>
        <div class="contributions-grid">
            <div class="contribution-card" data-aos="fade-up" data-aos-delay="100">
                <div class="contribution-header">
                    <div class="contribution-icon">
                        <i class="fas fa-building"></i>
                    </div>
                    <span class="contribution-badge">2020</span>
                </div>
                <h3>[Project/Initiative Name]</h3>
                <p>[Description of the contribution and its impact on the community]</p>
                <div class="impact-metrics">
                    <div class="metric">
                        <strong>500+</strong>
                        <span>People Helped</span>
                    </div>
                    <div class="metric">
                        <strong>$50K</strong>
                        <span>Raised</span>
                    </div>
                </div>
            </div>
            
            <div class="contribution-card" data-aos="fade-up" data-aos-delay="200">
                <div class="contribution-header">
                    <div class="contribution-icon">
                        <i class="fas fa-hand-holding-heart"></i>
                    </div>
                    <span class="contribution-badge">2019</span>
                </div>
                <h3>[Program Name]</h3>
                <p>[Description of the program and its lasting community benefits]</p>
                <div class="impact-metrics">
                    <div class="metric">
                        <strong>1000+</strong>
                        <span>Beneficiaries</span>
                    </div>
                    <div class="metric">
                        <strong>3</strong>
                        <span>Locations</span>
                    </div>
                </div>
            </div>
            
            <div class="contribution-card" data-aos="fade-up" data-aos-delay="300">
                <div class="contribution-header">
                    <div class="contribution-icon">
                        <i class="fas fa-lightbulb"></i>
                    </div>
                    <span class="contribution-badge">2018</span>
                </div>
                <h3>[Initiative Name]</h3>
                <p>[Description of innovation or change brought to the community]</p>
                <div class="impact-metrics">
                    <div class="metric">
                        <strong>200+</strong>
                        <span>Participants</span>
                    </div>
                    <div class="metric">
                        <strong>100%</strong>
                        <span>Success Rate</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <style>
        .contributions-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .contribution-card {{
            background: var(--background);
            padding: 35px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }}
        
        .contribution-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(26, 115, 232, 0.05), rgba(244, 180, 0, 0.05));
            opacity: 0;
            transition: opacity 0.4s ease;
        }}
        
        .contribution-card:hover {{
            transform: translateY(-10px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-color);
        }}
        
        .contribution-card:hover::before {{
            opacity: 1;
        }}
        
        .contribution-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            position: relative;
            z-index: 1;
        }}
        
        .contribution-icon {{
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
        }}
        
        .contribution-card:hover .contribution-icon {{
            transform: rotate(-10deg) scale(1.1);
        }}
        
        .contribution-icon i {{
            font-size: 1.8rem;
            color: white;
        }}
        
        .contribution-badge {{
            background: var(--accent-color);
            color: var(--text-dark);
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
        }}
        
        .contribution-card h3 {{
            font-size: 1.5rem;
            color: var(--text-dark);
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
        }}
        
        .contribution-card p {{
            color: var(--text-medium);
            line-height: 1.7;
            margin-bottom: 25px;
            position: relative;
            z-index: 1;
        }}
        
        .impact-metrics {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            padding-top: 20px;
            border-top: 2px solid rgba(26, 115, 232, 0.1);
            position: relative;
            z-index: 1;
        }}
        
        .metric {{
            text-align: center;
        }}
        
        .metric strong {{
            display: block;
            font-size: 1.8rem;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            margin-bottom: 5px;
        }}
        
        .metric span {{
            color: var(--text-light);
            font-size: 0.9rem;
        }}
    </style>
    """
    return get_base_html(content, "Contributions", "contributions", HERO_IMAGE)


@app.route('/awards')
def awards():
    content = f"""
    <div class="content-section">
        <div class="section-content reverse">
            <div class="section-text" data-aos="fade-left">
                <h2>{AWARDS['title']}</h2>
                <p>{AWARDS['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-right">
                <img src="{AWARDS['image']}" alt="{AWARDS['title']} - Recognition and honors received">
            </div>
        </div>
    </div>
    
    <!-- Interactive Awards Gallery -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Recognition & Honors</h2>
        <div class="awards-gallery">
            <div class="award-item" data-aos="zoom-in" data-aos-delay="100">
                <div class="award-medal">
                    <i class="fas fa-trophy"></i>
                </div>
                <div class="award-content">
                    <h3>[Award Name]</h3>
                    <div class="award-org">[Organization Name]</div>
                    <div class="award-year">2023</div>
                    <p>[Brief description of why this award was received and its significance]</p>
                </div>
            </div>
            
            <div class="award-item" data-aos="zoom-in" data-aos-delay="200">
                <div class="award-medal">
                    <i class="fas fa-medal"></i>
                </div>
                <div class="award-content">
                    <h3>[Honor Name]</h3>
                    <div class="award-org">[Organization Name]</div>
                    <div class="award-year">2022</div>
                    <p>[Brief description of recognition and impact]</p>
                </div>
            </div>
            
            <div class="award-item" data-aos="zoom-in" data-aos-delay="300">
                <div class="award-medal">
                    <i class="fas fa-award"></i>
                </div>
                <div class="award-content">
                    <h3>[Achievement Name]</h3>
                    <div class="award-org">[Organization Name]</div>
                    <div class="award-year">2021</div>
                    <p>[Brief description of achievement and community recognition]</p>
                </div>
            </div>
            
            <div class="award-item" data-aos="zoom-in" data-aos-delay="400">
                <div class="award-medal">
                    <i class="fas fa-star"></i>
                </div>
                <div class="award-content">
                    <h3>[Recognition Name]</h3>
                    <div class="award-org">[Organization Name]</div>
                    <div class="award-year">2020</div>
                    <p>[Brief description of honor and its meaning]</p>
                </div>
            </div>
        </div>
    </div>
    
    <style>
        .awards-gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .award-item {{
            background: var(--background-alt);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            cursor: pointer;
            position: relative;
        }}
        
        .award-item::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, var(--accent-color), var(--primary-color), var(--secondary-color));
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.5s ease;
        }}
        
        .award-item:hover {{
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
        }}
        
        .award-item:hover::before {{
            transform: scaleX(1);
        }}
        
        .award-medal {{
            background: linear-gradient(135deg, var(--accent-color), #FFA500);
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }}
        
        .award-medal::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
            animation: shimmer 3s infinite;
        }}
        
        @keyframes shimmer {{
            0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
            100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
        }}
        
        .award-item:hover .award-medal {{
            animation: pulse 1s ease-in-out;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}
        
        .award-medal i {{
            font-size: 3.5rem;
            color: white;
            filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.2));
            position: relative;
            z-index: 1;
            transition: var(--transition);
        }}
        
        .award-item:hover .award-medal i {{
            transform: rotateY(360deg) scale(1.2);
        }}
        
        .award-content {{
            padding: 25px;
        }}
        
        .award-content h3 {{
            font-size: 1.3rem;
            color: var(--text-dark);
            margin-bottom: 10px;
        }}
        
        .award-org {{
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: 5px;
            font-size: 0.95rem;
        }}
        
        .award-year {{
            display: inline-block;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 15px;
        }}
        
        .award-content p {{
            color: var(--text-medium);
            line-height: 1.6;
            font-size: 0.95rem;
        }}
    </style>
    """
    return get_base_html(content, "Awards", "awards", HERO_IMAGE)


@app.route('/community')
def community():
    content = f"""
    <div class="content-section">
        <div class="section-content">
            <div class="section-text" data-aos="fade-right">
                <h2>{COMMUNITY['title']}</h2>
                <p>{COMMUNITY['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-left">
                <img src="{COMMUNITY['image']}" alt="{COMMUNITY['title']} - Community engagement and involvement">
            </div>
        </div>
    </div>
    
    <!-- Interactive Organization Cards -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Organizations & Affiliations</h2>
        <div class="organizations-grid">
            <div class="org-card" data-aos="flip-up" data-aos-delay="100">
                <div class="org-icon">
                    <i class="fas fa-briefcase"></i>
                </div>
                <h3>[Organization Name]</h3>
                <div class="org-role">Board Member</div>
                <div class="org-duration">2020 - Present</div>
                <p>[Brief description of involvement and contributions to the organization]</p>
                <a href="#" class="org-link">Learn More <i class="fas fa-arrow-right"></i></a>
            </div>
            
            <div class="org-card" data-aos="flip-up" data-aos-delay="200">
                <div class="org-icon">
                    <i class="fas fa-users-cog"></i>
                </div>
                <h3>[Committee Name]</h3>
                <div class="org-role">Chairperson</div>
                <div class="org-duration">2018 - Present</div>
                <p>[Brief description of leadership role and committee achievements]</p>
                <a href="#" class="org-link">Learn More <i class="fas fa-arrow-right"></i></a>
            </div>
            
            <div class="org-card" data-aos="flip-up" data-aos-delay="300">
                <div class="org-icon">
                    <i class="fas fa-handshake"></i>
                </div>
                <h3>[Foundation Name]</h3>
                <div class="org-role">Advisory Council</div>
                <div class="org-duration">2015 - Present</div>
                <p>[Brief description of advisory role and foundation support]</p>
                <a href="#" class="org-link">Learn More <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </div>
    
    <!-- Community Impact Map -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Community Reach</h2>
        <div class="impact-areas" data-aos="fade-up">
            <div class="impact-area">
                <div class="area-icon"><i class="fas fa-graduation-cap"></i></div>
                <h4>Education</h4>
                <p>Supporting schools and educational programs across the region</p>
            </div>
            <div class="impact-area">
                <div class="area-icon"><i class="fas fa-heartbeat"></i></div>
                <h4>Healthcare</h4>
                <p>Improving access to healthcare services for underserved communities</p>
            </div>
            <div class="impact-area">
                <div class="area-icon"><i class="fas fa-home"></i></div>
                <h4>Housing</h4>
                <p>Providing affordable housing solutions and support</p>
            </div>
            <div class="impact-area">
                <div class="area-icon"><i class="fas fa-leaf"></i></div>
                <h4>Environment</h4>
                <p>Leading sustainability and environmental protection initiatives</p>
            </div>
        </div>
    </div>
    
    <style>
        .organizations-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .org-card {{
            background: var(--background);
            padding: 35px 30px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            border: 2px solid transparent;
            text-align: center;
        }}
        
        .org-card:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-color);
        }}
        
        .org-icon {{
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            transition: var(--transition);
        }}
        
        .org-card:hover .org-icon {{
            transform: rotateY(180deg);
        }}
        
        .org-icon i {{
            font-size: 2.2rem;
            color: white;
        }}
        
        .org-card h3 {{
            font-size: 1.5rem;
            color: var(--text-dark);
            margin-bottom: 10px;
        }}
        
        .org-role {{
            color: var(--primary-color);
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }}
        
        .org-duration {{
            color: var(--text-light);
            font-size: 0.9rem;
            margin-bottom: 15px;
        }}
        
        .org-card p {{
            color: var(--text-medium);
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        
        .org-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }}
        
        .org-link:hover {{
            gap: 12px;
            color: var(--secondary-color);
        }}
        
        .impact-areas {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .impact-area {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            padding: 35px 25px;
            border-radius: var(--border-radius);
            text-align: center;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }}
        
        .impact-area::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
            transition: var(--transition);
        }}
        
        .impact-area:hover {{
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
        }}
        
        .impact-area:hover::before {{
            transform: rotate(45deg);
        }}
        
        .area-icon {{
            width: 70px;
            height: 70px;
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            transition: var(--transition);
            position: relative;
            z-index: 1;
        }}
        
        .impact-area:hover .area-icon {{
            transform: scale(1.15) rotate(-10deg);
        }}
        
        .area-icon i {{
            font-size: 2rem;
            color: white;
        }}
        
        .impact-area h4 {{
            color: white;
            font-size: 1.5rem;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }}
        
        .impact-area p {{
            color: rgba(255,255,255,0.9);
            line-height: 1.6;
            position: relative;
            z-index: 1;
        }}
    </style>
    """
    return get_base_html(content, "Community", "community", HERO_IMAGE)


@app.route('/philanthropy')
def philanthropy():
    content = f"""
    <div class="content-section">
        <div class="section-content reverse">
            <div class="section-text" data-aos="fade-left">
                <h2>{PHILANTHROPY['title']}</h2>
                <p>{PHILANTHROPY['content']}</p>
            </div>
            <div class="section-image" data-aos="fade-right">
                <img src="{PHILANTHROPY['image']}" alt="{PHILANTHROPY['title']} - Charitable work and giving back">
            </div>
        </div>
    </div>
    
    <!-- Interactive Giving Circles -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Philanthropic Focus Areas</h2>
        <div class="giving-circles">
            <div class="giving-circle large" data-aos="zoom-in" data-aos-delay="100">
                <div class="circle-content">
                    <i class="fas fa-child"></i>
                    <h3>Youth Development</h3>
                    <p>$500K+ invested</p>
                </div>
            </div>
            
            <div class="giving-circle medium" data-aos="zoom-in" data-aos-delay="200">
                <div class="circle-content">
                    <i class="fas fa-book-reader"></i>
                    <h3>Education</h3>
                    <p>$250K+ invested</p>
                </div>
            </div>
            
            <div class="giving-circle medium" data-aos="zoom-in" data-aos-delay="300">
                <div class="circle-content">
                    <i class="fas fa-utensils"></i>
                    <h3>Food Security</h3>
                    <p>$200K+ invested</p>
                </div>
            </div>
            
            <div class="giving-circle small" data-aos="zoom-in" data-aos-delay="400">
                <div class="circle-content">
                    <i class="fas fa-palette"></i>
                    <h3>Arts</h3>
                    <p>$100K+</p>
                </div>
            </div>
            
            <div class="giving-circle small" data-aos="zoom-in" data-aos-delay="500">
                <div class="circle-content">
                    <i class="fas fa-tree"></i>
                    <h3>Environment</h3>
                    <p>$100K+</p>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Volunteer Impact -->
    <div class="content-section">
        <h2 class="section-title" data-aos="fade-up">Personal Involvement</h2>
        <div class="volunteer-stats">
            <div class="volunteer-card" data-aos="fade-right" data-aos-delay="100">
                <div class="volunteer-visual">
                    <div class="progress-ring">
                        <svg width="140" height="140">
                            <circle cx="70" cy="70" r="60" fill="none" stroke="#e5e7eb" stroke-width="12"/>
                            <circle cx="70" cy="70" r="60" fill="none" stroke="url(#gradient1)" stroke-width="12" 
                                    stroke-dasharray="377" stroke-dashoffset="94" stroke-linecap="round"
                                    transform="rotate(-90 70 70)" class="progress-circle"/>
                            <defs>
                                <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:var(--primary-color);stop-opacity:1" />
                                    <stop offset="100%" style="stop-color:var(--accent-color);stop-opacity:1" />
                                </linearGradient>
                            </defs>
                        </svg>
                        <div class="ring-text">
                            <div class="ring-number">2000+</div>
                            <div class="ring-label">Hours</div>
                        </div>
                    </div>
                </div>
                <h3>Volunteer Hours</h3>
                <p>Personal time dedicated to community service and mentorship programs</p>
            </div>
            
            <div class="volunteer-card" data-aos="fade-up" data-aos-delay="200">
                <div class="volunteer-visual">
                    <div class="progress-ring">
                        <svg width="140" height="140">
                            <circle cx="70" cy="70" r="60" fill="none" stroke="#e5e7eb" stroke-width="12"/>
                            <circle cx="70" cy="70" r="60" fill="none" stroke="url(#gradient2)" stroke-width="12" 
                                    stroke-dasharray="377" stroke-dashoffset="151" stroke-linecap="round"
                                    transform="rotate(-90 70 70)" class="progress-circle"/>
                            <defs>
                                <linearGradient id="gradient2" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:var(--primary-color);stop-opacity:1" />
                                    <stop offset="100%" style="stop-color:var(--secondary-color);stop-opacity:1" />
                                </linearGradient>
                            </defs>
                        </svg>
                        <div class="ring-text">
                            <div class="ring-number">50+</div>
                            <div class="ring-label">Events</div>
                        </div>
                    </div>
                </div>
                <h3>Community Events</h3>
                <p>Organized and participated in charitable events and fundraisers</p>
            </div>
            
            <div class="volunteer-card" data-aos="fade-left" data-aos-delay="300">
                <div class="volunteer-visual">
                    <div class="progress-ring">
                        <svg width="140" height="140">
                            <circle cx="70" cy="70" r="60" fill="none" stroke="#e5e7eb" stroke-width="12"/>
                            <circle cx="70" cy="70" r="60" fill="none" stroke="url(#gradient3)" stroke-width="12" 
                                    stroke-dasharray="377" stroke-dashoffset="113" stroke-linecap="round"
                                    transform="rotate(-90 70 70)" class="progress-circle"/>
                            <defs>
                                <linearGradient id="gradient3" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:var(--accent-color);stop-opacity:1" />
                                    <stop offset="100%" style="stop-color:var(--primary-color);stop-opacity:1" />
                                </linearGradient>
                            </defs>
                        </svg>
                        <div class="ring-text">
                            <div class="ring-number">100+</div>
                            <div class="ring-label">Mentees</div>
                        </div>
                    </div>
                </div>
                <h3>Mentorship</h3>
                <p>Guided and supported individuals through career and personal development</p>
            </div>
        </div>
    </div>
    
    <style>
        .giving-circles {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        .giving-circle {{
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }}
        
        .giving-circle::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }}
        
        .giving-circle:hover {{
            transform: scale(1.1) rotate(5deg);
            box-shadow: var(--shadow-lg);
        }}
        
        .giving-circle:hover::before {{
            opacity: 1;
        }}
        
        .giving-circle.large {{
            width: 280px;
            height: 280px;
        }}
        
        .giving-circle.medium {{
            width: 220px;
            height: 220px;
        }}
        
        .giving-circle.small {{
            width: 180px;
            height: 180px;
        }}
        
        .circle-content {{
            text-align: center;
            color: white;
            padding: 20px;
            position: relative;
            z-index: 1;
        }}
        
        .circle-content i {{
            font-size: 3rem;
            margin-bottom: 15px;
            display: block;
            filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.2));
        }}
        
        .giving-circle.large .circle-content i {{
            font-size: 4rem;
        }}
        
        .giving-circle.small .circle-content i {{
            font-size: 2rem;
        }}
        
        .circle-content h3 {{
            font-size: 1.4rem;
            margin-bottom: 8px;
            font-weight: 700;
        }}
        
        .giving-circle.small .circle-content h3 {{
            font-size: 1.1rem;
        }}
        
        .circle-content p {{
            font-size: 0.95rem;
            opacity: 0.95;
            font-weight: 600;
        }}
        
        .volunteer-stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .volunteer-card {{
            background: var(--background-alt);
            padding: 40px 30px;
            border-radius: var(--border-radius);
            text-align: center;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
        }}
        
        .volunteer-card:hover {{
            transform: translateY(-10px);
            box-shadow: var(--shadow-lg);
        }}
        
        .volunteer-visual {{
            margin-bottom: 25px;
        }}
        
        .progress-ring {{
            position: relative;
            display: inline-block;
        }}
        
        .progress-circle {{
            transition: stroke-dashoffset 2s ease-out;
        }}
        
        .ring-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }}
        
        .ring-number {{
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .ring-label {{
            font-size: 0.9rem;
            color: var(--text-medium);
            font-weight: 600;
        }}
        
        .volunteer-card h3 {{
            font-size: 1.6rem;
            color: var(--text-dark);
            margin-bottom: 15px;
        }}
        
        .volunteer-card p {{
            color: var(--text-medium);
            line-height: 1.6;
        }}
        
        @media (max-width: 768px) {{
            .giving-circles {{
                flex-direction: column;
            }}
            
            .giving-circle.large,
            .giving-circle.medium {{
                width: 240px;
                height: 240px;
            }}
            
            .giving-circle.small {{
                width: 200px;
                height: 200px;
            }}
        }}
    </style>
    """
    return get_base_html(content, "Philanthropy", "philanthropy", HERO_IMAGE)


if __name__ == '__main__':
    # Auto-reload enabled: Any changes to this file will automatically restart the server
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=True)
