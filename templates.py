from config import *


def format_content_with_lists(content_text):
    """
    Convert text with bullet points to proper HTML list structure.
    Handles both bullet points (•) and numbered lists.
    """
    if not content_text:
        return ""

    lines = content_text.split('\n')
    html_parts = []
    in_list = False
    list_items = []

    for line in lines:
        line = line.strip()
        if not line:
            if in_list and list_items:
                html_parts.append(
                    '<ul class="content-list compact-list">\n' +
                    '\n'.join(f'<li>{item}</li>' for item in list_items) +
                    '\n</ul>'
                )
                list_items = []
                in_list = False
            continue

        if (
            line.startswith('•')
            or line.startswith('*')
            or line.startswith('-')
            or (line[0].isdigit() and '.' in line[:3])
        ):
            in_list = True
            if line[0].isdigit():
                list_items.append(line[line.find('.') + 1:].strip())
            else:
                list_items.append(line[1:].strip())
        else:
            if in_list and list_items:
                html_parts.append(
                    '<ul class="content-list compact-list">\n' +
                    '\n'.join(f'<li>{item}</li>' for item in list_items) +
                    '\n</ul>'
                )
                list_items = []
                in_list = False
            html_parts.append(f'<p>{line}</p>')

    if in_list and list_items:
        html_parts.append(
            '<ul class="content-list compact-list">\n' +
            '\n'.join(f'<li>{item}</li>' for item in list_items) +
            '\n</ul>'
        )

    return '\n'.join(html_parts)


def get_base_html(content, title, current_page, hero_image):
    """Base HTML template with navigation and styling"""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Community Leader Biography</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

<style>
/* =========================
   ENHANCED LIGHT MODE WITH STRONGER CONTRAST
   ========================= 
   This design features:
   - Stronger shadows with layered depth (multiple shadow layers)
   - Thicker borders on all interactive elements (3-4px)
   - Subtle background shading on content areas
   - Enhanced hover effects with dramatic shadow increases
   - Inset shadows for inner glow effects
   - Dark mode remains unchanged
   ========================= */
/* =========================
   LIGHT MODE – REFINED
   ========================= */
:root {{
    /* Light Capri Blue Color Scheme */
    --primary-color: #00bfff;        /* capri blue */
    --secondary-color: #1e90ff;      /* dodger blue */
    --accent-color: #00d4ff;         /* light capri blue */
    --accent-secondary: #ef4444;     /* red accent */
    --accent-tertiary: #6366f1;      /* indigo accent */
    --accent-quaternary: #4f46e5;    /* indigo accent */
    --success-color: #10b981;        /* pleasant green for success states */
    
    /* Text colors - modern charcoal tones for readability */
    --text-dark: #0b1320;
    --text-medium: #24303b;
    --text-light: #475569;
    
    /* Backgrounds - soft layered gradients for depth */
    --background: linear-gradient(180deg, #e0f7ff 0%, #d0f0ff 100%);
    --background-alt: linear-gradient(135deg, #f0faff 0%, #e0f5ff 100%);
    --background-gradient: linear-gradient(135deg, #00bfff 0%, #1e90ff 100%);
    
    /* Shadows - ENHANCED for much stronger light mode contrast */
    --shadow-sm: 0 8px 24px rgba(0, 0, 0, 0.12), 0 3px 8px rgba(0, 191, 255, 0.2);
    --shadow-md: 0 16px 40px rgba(0, 0, 0, 0.15), 0 6px 16px rgba(0, 191, 255, 0.25);
    --shadow-lg: 0 24px 60px rgba(0, 0, 0, 0.2), 0 12px 28px rgba(0, 191, 255, 0.3);
    --shadow-colored: 0 16px 48px rgba(0, 0, 0, 0.2), 0 8px 24px rgba(0, 212, 255, 0.4);
    --shadow-secondary: 0 16px 48px rgba(0, 0, 0, 0.18), 0 8px 24px rgba(30, 144, 255, 0.35);

    --border-radius: 14px;
    --transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}}

/* =========================
   DARK MODE – UNCHANGED
   ========================= */
[data-theme="dark"] {{
    --primary-color: #6D9AFF;
    --secondary-color: #B794F4;
    --accent-color: #FFB74D;
    --accent-secondary: #FF6B9D;
    --accent-tertiary: #4EF0DA;
    --accent-quaternary: #FF8EFF;
    --success-color: #00FFCC;
    --text-dark: #F8FAFC;
    --text-medium: #E2E8F0;
    --text-light: #CBD5E0;
    --background: #0F172A;
    --background-alt: linear-gradient(135deg, #1E293B 0%, #334155 50%, #475569 100%);
    --background-gradient: linear-gradient(135deg, #6D9AFF 0%, #B794F4 100%);
    --shadow-sm: 0 4px 12px rgba(0,0,0,0.5);
    --shadow-md: 0 8px 24px rgba(0,0,0,0.6);
    --shadow-lg: 0 16px 48px rgba(0,0,0,0.8);
    --shadow-colored: 0 12px 40px rgba(109,154,255,0.4);
    --shadow-secondary: 0 12px 40px rgba(183,148,244,0.4);
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.8;
    color: var(--text-dark);
    background: var(--background);
    transition: background 0.4s ease, color 0.4s ease;
    font-size: 1.15rem;
    font-weight: 400;
    overflow-x: hidden;
}}

        /* Background floating gradient circles */
        .floating-circle {{
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            z-index: -1;
            filter: blur(40px);
            opacity: 0.15;
            animation: floatAround 20s ease-in-out infinite;
        }}

        .circle-1 {{
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, var(--primary-color) 0%, transparent 70%);
            top: 10%;
            left: 5%;
            animation-delay: 0s;
        }}

        .circle-2 {{
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, var(--secondary-color) 0%, transparent 70%);
            bottom: 15%;
            right: 8%;
            animation-delay: -5s;
        }}

        .circle-3 {{
            width: 350px;
            height: 350px;
            background: radial-gradient(circle, var(--accent-color) 0%, transparent 70%);
            top: 50%;
            left: 70%;
            animation-delay: -10s;
        }}

        .circle-4 {{
            width: 250px;
            height: 250px;
            background: radial-gradient(circle, var(--accent-tertiary) 0%, transparent 70%);
            bottom: 5%;
            left: 20%;
            animation-delay: -15s;
        }}

        @keyframes floatAround {{
            0%, 100% {{
                transform: translate(0, 0) rotate(0deg);
            }}
            25% {{
                transform: translate(30px, -30px) rotate(90deg);
            }}
            50% {{
                transform: translate(-20px, 20px) rotate(180deg);
            }}
            75% {{
                transform: translate(-30px, -20px) rotate(270deg);
            }}
        }}

        /* MAIN CONTENT TEXT - SIGNIFICANTLY LARGER */
        .section-text p,
        .intro-section p,
        .impact-cta p,
        .hero-subtitle,
        .footer-section p,
        .footer-links a,
        .content-list li,
        .section-text ul li,
        .section-text ol li,
        .section-text p {{
            font-size: 1.4rem !important;
            line-height: 1.9 !important;
            font-weight: 400 !important;
        }}

        /* REGULAR Bullet point and list styling */
        .section-text ul,
        .section-text ol,
        .content-list {{
            margin: 1.5rem 0 !important;
            padding-left: 2.5rem !important;
        }}

        .section-text ul,
        .content-list {{
            list-style-type: disc !important;
        }}

        .section-text ol {{
            list-style-type: decimal !important;
        }}

        /* COMPACT LISTS - For Early Life and other dense content */
        .compact-list {{
            margin: 1rem 0 !important;
            padding-left: 2rem !important;
        }}

        .compact-list li {{
            margin-bottom: 0.3rem !important;
            padding-left: 0.5rem !important;
            font-size: 1.35rem !important;
            line-height: 1.6 !important;
            transition: all 0.2s ease;
        }}

        /* Light mode list items - subtle background on hover */
        :root .compact-list li,
        :root .regular-list li,
        :root .content-list li {{
            padding: 0.3rem 0.5rem;
            border-radius: 6px;
        }}

        :root .compact-list li:hover,
        :root .regular-list li:hover,
        :root .content-list li:hover {{
            background: rgba(0, 191, 255, 0.08);
            padding-left: 0.8rem !important;
        }}

        .compact-list li:last-child {{
            margin-bottom: 0 !important;
        }}

        .regular-list li {{
            margin-bottom: 0.8rem !important;
            padding-left: 0.8rem !important;
            font-size: 1.4rem !important;
            line-height: 1.9 !important;
        }}

        .regular-list li:last-child {{
            margin-bottom: 0 !important;
        }}

        /* Special styling for bullet points */
        .section-text ul li::marker,
        .content-list li::marker {{
            color: var(--primary-color) !important;
            font-size: 1.6rem !important;
        }}

        .compact-list li::marker {{
            font-size: 1.4rem !important;
        }}

        /* Hero quote - even larger */
        .hero-quote {{
            font-size: 1.7rem !important;
            font-style: italic;
            padding: 2.5rem 3rem;
            background: rgba(255,255,255,0.25);
            border-radius: var(--border-radius);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255,255,255,0.4);
            box-shadow: 
                0 12px 40px rgba(0, 0, 0, 0.35),
                0 6px 18px rgba(0, 0, 0, 0.25),
                inset 0 2px 8px rgba(255, 255, 255, 0.3);
            max-width: 800px;
            margin: 0 auto 2rem;
            font-weight: 500;
            line-height: 1.8 !important;
            white-space: nowrap;
            animation: fadeInUp 1s ease-out 0.4s backwards;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        }}

        /* Footer contact info */
        .footer-section p i {{
            font-size: 1.4rem !important;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.3px;
        }}

        /* Stats Grid Styles */
        .stats-grid {{
            display: flex;
            flex-wrap: nowrap;
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            justify-content: center;
            overflow-x: auto;
            padding: 20px 10px;
            scrollbar-width: thin;
            scrollbar-color: var(--primary-color) transparent;
        }}

        .stats-grid::-webkit-scrollbar {{
            height: 8px;
        }}

        .stats-grid::-webkit-scrollbar-track {{
            background: transparent;
            border-radius: 4px;
        }}

        .stats-grid::-webkit-scrollbar-thumb {{
            background: var(--primary-color);
            border-radius: 4px;
        }}

        .stat-card {{
            background: var(--background-alt);
            padding: 40px 30px;
            border-radius: var(--border-radius);
            text-align: center;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            border: 3px solid var(--primary-color);
            backdrop-filter: blur(10px);
            flex-shrink: 0;
            width: 250px;
            position: relative;
            overflow: hidden;
        }}

        /* Light mode only - add extra depth */
        :root .stat-card {{
            box-shadow: 
                0 16px 40px rgba(0, 0, 0, 0.15),
                0 6px 16px rgba(0, 191, 255, 0.25),
                inset 0 2px 10px rgba(255, 255, 255, 0.5);
        }}

        .stat-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg,
                transparent 30%,
                rgba(30, 58, 138, 0.3) 50%,
                transparent 70%);
            transform: rotate(0deg);
            animation: shimmer 3s infinite;
        }}

        @keyframes shimmer {{
            0% {{
                transform: rotate(0deg) translateX(-100%);
            }}
            100% {{
                transform: rotate(0deg) translateX(100%);
            }}
        }}

        .stat-card:hover {{
            transform: translateY(-12px) scale(1.04);
            box-shadow: var(--shadow-colored);
            border-color: var(--accent-color);
        }}

        /* Light mode hover - even stronger shadow */
        :root .stat-card:hover {{
            box-shadow: 
                0 24px 60px rgba(0, 0, 0, 0.22),
                0 12px 28px rgba(0, 212, 255, 0.4),
                inset 0 2px 12px rgba(255, 255, 255, 0.6);
        }}

        .stat-card i {{
            font-size: 2.8rem;
            color: var(--primary-color);
            margin-bottom: 20px;
            animation: iconFloat 3s ease-in-out infinite;
            position: relative;
            z-index: 1;
        }}

        @keyframes iconFloat {{
            0%, 100% {{
                transform: translateY(0px);
            }}
            50% {{
                transform: translateY(-10px);
            }}
        }}

        .stat-number {{
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #6366f1 0%, #3b82f6 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
            text-shadow: 0 2px 8px rgba(0,0,0,0.2);
            position: relative;
            z-index: 1;
        }}

        /* Dark mode stat numbers - keep original gradient */
        [data-theme="dark"] .stat-number {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .stat-label {{
            font-size: 1.3rem;
            color: var(--text-dark);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            z-index: 1;
        }}

        /* Impact at a Glance heading - Light Mode */
        .impact-heading {{
            text-align: center;
            font-size: 2.8rem;
            background: linear-gradient(135deg, #6366f1 0%, #3b82f6 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 3rem;
            font-weight: 800;
        }}

        /* Impact at a Glance heading - Dark Mode */
        [data-theme="dark"] .impact-heading {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .impact-cta {{
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 40px;
            background: var(--background-alt);
            border-radius: var(--border-radius);
            /* stronger border in light mode */
            border: 4px solid var(--primary-color);
            box-shadow: var(--shadow-lg);
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
            transition: border-color 0.28s ease, box-shadow 0.28s ease, transform 0.28s ease;
        }}

        /* Light mode only - add even stronger shadow */
        :root .impact-cta {{
            box-shadow: 
                0 24px 60px rgba(0, 0, 0, 0.2),
                0 12px 28px rgba(0, 191, 255, 0.3),
                inset 0 2px 10px rgba(255, 255, 255, 0.5);
        }}

        .impact-cta::before {{
            /* animated gradient background layer — visible always */
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: var(--border-radius);
            z-index: 0;
            background: linear-gradient(135deg,
                rgba(255,255,255,0.06) 0%,
                rgba(255,255,255,0.03) 30%,
                rgba(255,255,255,0.00) 100%);
            background-size: 300% 300%;
            opacity: 1;
            pointer-events: none;
            transition: opacity 0.35s ease;
        }}

        /* content inside should sit above the gradient */
        .impact-cta > * {{
            position: relative;
            z-index: 1;
        }}

        /* reveal the visible border on hover while keeping the gradient visible */
        .impact-cta:hover {{
            border-color: var(--accent-color);
            box-shadow: var(--shadow-colored);
            transform: translateY(-8px);
        }}

        /* Light mode hover - stronger effect */
        :root .impact-cta:hover {{
            box-shadow: 
                0 32px 80px rgba(0, 0, 0, 0.25),
                0 16px 36px rgba(0, 212, 255, 0.45),
                inset 0 2px 12px rgba(255, 255, 255, 0.6);
        }}

        /* Dark mode moving gradient for the background layer (still visible always) */
        [data-theme="dark"] .impact-cta::before {{
            background: linear-gradient(45deg,
                var(--primary-color),
                var(--accent-color),
                var(--accent-secondary),
                var(--accent-tertiary));
            animation: darkGradientMove 6s linear infinite;
            background-size: 300% 300%;
        }}

        @keyframes darkGradientMove {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .impact-cta h2 {{
            font-size: 2.8rem;
            color: var(--primary-color);
            margin-bottom: 1.5rem;
            font-weight: 800;
            line-height: 1.2;
            animation: textPulse 2s ease-in-out infinite;
            position: relative;
            z-index: 1;
        }}

        /* Dark mode impact-cta h2 */
        [data-theme="dark"] .impact-cta h2 {{
            color: var(--primary-color);
        }}

        @keyframes textPulse {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.85;
            }}
        }}

        .impact-cta p {{
            position: relative;
            z-index: 1;
        }}

        .impact-cta .cta-button {{
            position: relative;
            z-index: 1;
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
            width: 60px;
            height: 60px;
            border: 4px solid var(--primary-color);
            border-top-color: var(--accent-color);
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
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px) saturate(180%);
            box-shadow: var(--shadow-md);
            z-index: 1000;
            transition: var(--transition);
            padding: 1rem 0;
            border-bottom: 3px solid var(--primary-color);
        }}

        /* Light mode navbar - extra shadow depth */
        :root .navbar {{
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.12),
                0 4px 12px rgba(0, 191, 255, 0.2);
        }}

        [data-theme="dark"] .navbar {{
            background: rgba(15, 23, 42, 0.98);
            border-bottom: 2px solid var(--secondary-color);
        }}

        .navbar.scrolled {{
            padding: 0.8rem 0;
            box-shadow: var(--shadow-lg);
        }}

        /* Light mode scrolled navbar - extra depth */
        :root .navbar.scrolled {{
            box-shadow: 
                0 12px 40px rgba(0, 0, 0, 0.15),
                0 6px 18px rgba(0, 191, 255, 0.25);
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
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--primary-color);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }}

        .nav-logo i {{
            animation: starPulse 3s ease-in-out infinite;
        }}

        @keyframes starPulse {{
            0%, 100% {{
                transform: scale(1) rotate(0deg);
                color: #6366f1;
                filter: drop-shadow(0 0 5px rgba(99, 102, 241, 0.5));
            }}
            25% {{
                transform: scale(1.2) rotate(72deg);
                color: #3b82f6;
                filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.8));
            }}
            50% {{
                transform: scale(1) rotate(144deg);
                color: #06b6d4;
                filter: drop-shadow(0 0 10px rgba(6, 182, 212, 0.7));
            }}
            75% {{
                transform: scale(1.2) rotate(216deg);
                color: #a855f7;
                filter: drop-shadow(0 0 15px rgba(168, 85, 247, 0.8));
            }}
        }}

        /* Dark mode star pulse - keep original */
        [data-theme="dark"] .nav-logo i {{
            animation: starPulseDark 3s ease-in-out infinite;
        }}

        @keyframes starPulseDark {{
            0%, 100% {{
                transform: scale(1) rotate(0deg);
                color: var(--primary-color);
                filter: drop-shadow(0 0 5px rgba(109, 154, 255, 0.5));
            }}
            25% {{
                transform: scale(1.2) rotate(72deg);
                color: var(--accent-color);
                filter: drop-shadow(0 0 15px rgba(255, 183, 77, 0.8));
            }}
            50% {{
                transform: scale(1) rotate(144deg);
                color: var(--secondary-color);
                filter: drop-shadow(0 0 10px rgba(183, 148, 244, 0.7));
            }}
            75% {{
                transform: scale(1.2) rotate(216deg);
                color: var(--accent-tertiary);
                filter: drop-shadow(0 0 15px rgba(78, 240, 218, 0.8));
            }}
        }}

        .nav-menu {{
            display: flex;
            list-style: none;
            gap: 0.5rem;
            align-items: center;
            min-width: 550px;
            position: relative;
        }}

        .nav-link {{
            color: var(--text-dark);
            text-decoration: none;
            font-weight: 600;
            padding: 0.8rem 1.2rem;
            border-radius: 10px;
            transition: var(--transition);
            position: relative;
            font-size: 1.05rem;
        }}

        .nav-link:hover {{
            color: white;
            background: var(--primary-color);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25), 0 3px 10px rgba(0, 191, 255, 0.4);
        }}

        .nav-link.active {{
            color: white;
            font-weight: 700;
            background: var(--primary-color);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25), 0 3px 10px rgba(0, 191, 255, 0.4);
        }}

        /* Close Menu Button (Mobile Only) */
        .close-menu {{
            display: none;
            padding: 1rem 2rem;
        }}
        @media (max-width: 968px) {{
            .close-menu {{
                display: block;
            }}
        }}

        /* Dark Mode Toggle */
        .theme-toggle {{
            background: var(--primary-color);
            border: 3px solid var(--accent-color);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
            font-size: 1.2rem;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }}

        /* Light mode theme toggle - extra shadow */
        :root .theme-toggle {{
            box-shadow: 
                0 8px 24px rgba(0, 0, 0, 0.15),
                0 4px 12px rgba(0, 191, 255, 0.3);
        }}

        .theme-toggle::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }}

        .theme-toggle:hover::before {{
            width: 100px;
            height: 100px;
        }}

        .theme-toggle:hover {{
            transform: scale(1.1) rotate(180deg);
            box-shadow: var(--shadow-colored);
        }}

        /* Light mode theme toggle hover */
        :root .theme-toggle:hover {{
            box-shadow: 
                0 12px 32px rgba(0, 0, 0, 0.2),
                0 6px 16px rgba(0, 212, 255, 0.45);
        }}

        .theme-toggle i {{
            position: relative;
            z-index: 1;
        }}

        /* Mobile Menu Toggle */
        .menu-toggle {{
            display: none;
            flex-direction: column;
            gap: 5px;
            background: none;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
        }}

        .menu-toggle span {{
            display: block;
            width: 30px;
            height: 3px;
            background: var(--text-dark);
            transition: var(--transition);
            border-radius: 2px;
        }}

        .menu-toggle.active span:nth-child(1) {{
            transform: rotate(45deg) translate(8px, 8px);
        }}

        .menu-toggle.active span:nth-child(2) {{
            opacity: 0;
            transform: translateX(-15px);
        }}

        .menu-toggle.active span:nth-child(3) {{
            transform: rotate(-45deg) translate(6px, -6px);
        }}

        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 9rem 2rem 6rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            margin-top: 0;
        }}

        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('{hero_image}') center 20%/cover;
            opacity: 0.15;
            z-index: 0;
            animation: heroZoom 20s ease-in-out infinite alternate;
        }}

        @keyframes heroZoom {{
            0% {{
                transform: scale(1);
            }}
            100% {{
                transform: scale(1.1);
            }}
        }}

        .hero::after {{
            content: '';
            position: absolute;
            top: -30%;
            right: -10%;
            width: 700px;
            height: 700px;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
            border-radius: 50%;
            z-index: 0;
            animation: float 6s ease-in-out infinite;
        }}

        @keyframes float {{
            0%, 100% {{
                transform: translate(0, 0);
            }}
            50% {{
                transform: translate(-30px, 30px);
            }}
        }}

        .hero-content {{
            position: relative;
            z-index: 1;
            max-width: 900px;
            margin: 0 auto;
        }}

        .hero h1 {{
            font-size: 3.8rem;
            margin-bottom: 1rem;
            text-shadow: 2px 4px 12px rgba(0,0,0,0.3);
            font-weight: 800;
            letter-spacing: -1px;
            line-height: 1.1;
            animation: fadeInDown 1s ease-out;
        }}

        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .hero h2 {{
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            font-weight: 600;
            opacity: 0.95;
            letter-spacing: 0.3px;
            animation: fadeInDown 1s ease-out 0.2s backwards;
        }}

        .hero-quote {{
            font-size: 1.7rem !important;
            font-style: italic;
            padding: 2.5rem 3rem;
            background: rgba(255,255,255,0.25);
            border-radius: var(--border-radius);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            max-width: 800px;
            margin: 0 auto 2rem;
            font-weight: 500;
            line-height: 1.8 !important;
            white-space: nowrap;
            animation: fadeInUp 1s ease-out 0.4s backwards;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        }}

        .cta-button {{
            display: inline-block;
            background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
            color: white;
            padding: 1.1rem 3.2rem;
            border-radius: var(--border-radius);
            text-decoration: none;
            font-weight: 700;
            font-size: 1.25rem;
            transition: var(--transition);
            box-shadow: var(--shadow-md);
            margin-top: 1rem;
            border: 3px solid rgba(255, 255, 255, 0.3);
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }}

        /* Light mode CTA - extra depth */
        :root .cta-button {{
            box-shadow: 
                0 12px 32px rgba(0, 0, 0, 0.2),
                0 6px 16px rgba(59, 130, 246, 0.35);
        }}

        /* Dark mode CTA button - keep original */
        [data-theme="dark"] .cta-button {{
            background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-secondary) 100%);
        }}

        .cta-button::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }}

        .cta-button:hover::before {{
            left: 100%;
        }}

        .cta-button:hover {{
            transform: translateY(-5px) scale(1.03);
            box-shadow: var(--shadow-lg);
            background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        }}

        /* Light mode CTA hover - even stronger */
        :root .cta-button:hover {{
            box-shadow: 
                0 20px 48px rgba(0, 0, 0, 0.25),
                0 10px 24px rgba(99, 102, 241, 0.45);
        }}

        /* Dark mode CTA button hover - keep original */
        [data-theme="dark"] .cta-button:hover {{
            background: linear-gradient(135deg, var(--accent-secondary) 0%, var(--primary-color) 100%);
        }}

        /* Content Sections */
        .content-section {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 100px 2rem 40px;
            min-height: calc(100vh - 100px);
            display: flex;
            align-items: center;
            position: relative;
            z-index: 1;
        }}

        /* Enhanced decorative background elements for content sections */
        .content-section::before,
        .content-section::after {{
            content: '';
            position: absolute;
            border-radius: 50%;
            z-index: -1;
            pointer-events: none;
            filter: blur(30px);
            opacity: 0.1;
        }}

        .content-section::before {{
            top: 10%;
            right: -5%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, var(--primary-color) 0%, transparent 70%);
            animation: float 8s ease-in-out infinite;
        }}

        .content-section::after {{
            bottom: 15%;
            left: -5%;
            width: 350px;
            height: 350px;
            background: radial-gradient(circle, var(--secondary-color) 0%, transparent 70%);
            animation: float 10s ease-in-out infinite reverse;
        }}

        .section-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
            width: 100%;
        }}

        .section-content.reverse {{
            direction: rtl;
        }}

        .section-content.reverse > * {{
            direction: ltr;
        }}

        .section-text {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 100%;
            position: relative;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.4);
            border-radius: var(--border-radius);
            backdrop-filter: blur(8px);
        }}

        /* Light mode section text - subtle card effect */
        :root .section-text {{
            background: rgba(255, 255, 255, 0.6);
            box-shadow: 
                0 4px 16px rgba(0, 0, 0, 0.06),
                inset 0 1px 4px rgba(255, 255, 255, 0.8);
        }}

        /* Dark mode - remove the light background */
        [data-theme="dark"] .section-text {{
            background: transparent;
            box-shadow: none;
        }}

        /* Decorative accent line beside section text */
        .section-text::before {{
            content: '';
            position: absolute;
            left: -30px;
            top: 0;
            bottom: 0;
            width: 6px;
            background: linear-gradient(180deg, 
                #6366f1 0%, 
                #3b82f6 33%, 
                #06b6d4 66%,
                #a855f7 100%);
            border-radius: 3px;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
            animation: glowPulse 3s ease-in-out infinite;
        }}

        /* Dark mode section text line - keep original */
        [data-theme="dark"] .section-text::before {{
            background: linear-gradient(180deg, 
                var(--primary-color) 0%, 
                var(--accent-color) 50%, 
                var(--secondary-color) 100%);
            box-shadow: 0 0 20px rgba(109, 154, 255, 0.5);
        }}

        @keyframes glowPulse {{
            0%, 100% {{
                box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
            }}
            50% {{
                box-shadow: 0 0 30px rgba(99, 102, 241, 0.8);
            }}
        }}

        /* Dark mode glow pulse - keep original */
        [data-theme="dark"] .section-text::before {{
            animation: glowPulseDark 3s ease-in-out infinite;
        }}

        @keyframes glowPulseDark {{
            0%, 100% {{
                box-shadow: 0 0 20px rgba(109, 154, 255, 0.5);
            }}
            50% {{
                box-shadow: 0 0 30px rgba(109, 154, 255, 0.8);
            }}
        }}

        .section-text h2 {{
            font-size: 3rem;
            background: linear-gradient(135deg, #6366f1 0%, #3b82f6 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2.5rem;
            font-weight: 800;
            letter-spacing: -1px;
            line-height: 1.2;
            position: relative;
            padding-bottom: 1rem;
        }}

        /* Dark mode section text h2 - keep original */
        [data-theme="dark"] .section-text h2 {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .section-text h2::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, #6366f1, #3b82f6, #06b6d4);
            border-radius: 2px;
            animation: expandWidth 2s ease-in-out infinite;
        }}

        /* Dark mode section text h2 underline - keep original */
        [data-theme="dark"] .section-text h2::after {{
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        }}

        @keyframes expandWidth {{
            0%, 100% {{
                width: 80px;
            }}
            50% {{
                width: 120px;
            }}
        }}

        /* ALL SECTION IMAGES - With shining effect */
        .section-image {{
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            transition: var(--transition);
            position: relative;
            border: 4px solid var(--primary-color);
        }}

        /* Light mode section images - extra depth */
        :root .section-image {{
            box-shadow: 
                0 20px 52px rgba(0, 0, 0, 0.18),
                0 10px 24px rgba(0, 191, 255, 0.3),
                inset 0 1px 4px rgba(255, 255, 255, 0.4);
        }}

        .section-image::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(30, 58, 138, 0.2) 0%, rgba(37, 99, 235, 0.2) 100%);
            opacity: 0;
            transition: opacity 0.6s ease;
            z-index: 1;
        }}

        /* Shining effect for ALL section images */
        .section-image::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(45deg,
                transparent 40%,
                rgba(255, 255, 255, 0.3) 50%,
                transparent 60%);
            background-size: 200% 200%;
            animation: awardShine 10s linear infinite;
            z-index: 2;
            pointer-events: none;
        }}

        @keyframes awardShine {{
            0% {{
                background-position: -200% 0;
            }}
            100% {{
                background-position: 200% 0;
            }}
        }}

        .section-image:hover::after {{
            animation: awardShine 10s linear infinite;
        }}

        .section-image:hover::before {{
            opacity: 1;
        }}

        .section-image:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: var(--shadow-colored);
            border-color: var(--accent-color);
        }}

        /* Light mode section image hover - even stronger */
        :root .section-image:hover {{
            box-shadow: 
                0 28px 68px rgba(0, 0, 0, 0.24),
                0 14px 32px rgba(0, 212, 255, 0.45),
                inset 0 1px 6px rgba(255, 255, 255, 0.5);
        }}

        .section-image img {{
            width: 100%;
            height: 450px;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.7s ease;
        }}

        /* Early Life Image - Taller */
        .early-life-image img {{
            height: 650px !important;
            object-position: center top;
        }}

        .section-image:hover img {{
            transform: scale(1.1);
        }}

        /* Awards Images - Special Styling for Multiple Images */
        .awards-images-wrapper {{
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        .awards-image-container {{
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            transition: var(--transition);
            position: relative;
            border: 4px solid var(--primary-color);
        }}

        /* Light mode awards images - extra depth */
        :root .awards-image-container {{
            box-shadow: 
                0 20px 52px rgba(0, 0, 0, 0.18),
                0 10px 24px rgba(0, 191, 255, 0.3),
                inset 0 1px 4px rgba(255, 255, 255, 0.4);
        }}

        .awards-image-container:nth-child(2) {{
            border: 4px solid var(--secondary-color);
        }}

        .awards-image-container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(30, 58, 138, 0.2) 0%, rgba(37, 99, 235, 0.2) 100%);
            opacity: 0;
            transition: opacity 0.6s ease;
            z-index: 1;
        }}

        .awards-image-container:nth-child(2)::before {{
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(79, 70, 229, 0.2) 100%);
        }}

        .awards-image-container::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(45deg,
                transparent 40%,
                rgba(255, 255, 255, 0.3) 50%,
                transparent 60%);
            background-size: 200% 200%;
            animation: awardShine 10s linear infinite;
            z-index: 2;
            pointer-events: none;
        }}

        .awards-image-container:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: var(--shadow-colored);
        }}

        /* Light mode awards hover - stronger */
        :root .awards-image-container:hover {{
            box-shadow: 
                0 28px 68px rgba(0, 0, 0, 0.24),
                0 14px 32px rgba(0, 212, 255, 0.45),
                inset 0 1px 6px rgba(255, 255, 255, 0.5);
        }}

        .awards-image-container:nth-child(2):hover {{
            box-shadow: var(--shadow-secondary);
            border-color: var(--accent-quaternary);
        }}

        /* Light mode second award hover */
        :root .awards-image-container:nth-child(2):hover {{
            box-shadow: 
                0 28px 68px rgba(0, 0, 0, 0.22),
                0 14px 32px rgba(30, 144, 255, 0.4),
                inset 0 1px 6px rgba(255, 255, 255, 0.5);
        }}

        .awards-image-container:hover::before {{
            opacity: 1;
        }}

        .awards-image-container img {{
            width: 100%;
            height: 450px;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.7s ease;
        }}

        .awards-image-container:hover img {{
            transform: scale(1.1) rotate(1deg);
        }}

        /* Intro Section (Home Page) */
        .intro-section {{
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
            padding: 60px 40px;
            background: var(--background-alt);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-lg);
            border: 4px solid var(--primary-color);
            position: relative;
            overflow: hidden;
        }}

        /* Light mode intro section - extra depth */
        :root .intro-section {{
            box-shadow: 
                0 24px 60px rgba(0, 0, 0, 0.2),
                0 12px 28px rgba(0, 191, 255, 0.3),
                inset 0 2px 10px rgba(255, 255, 255, 0.5);
        }}

        .intro-section::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 20px,
                rgba(30, 58, 138, 0.05) 20px,
                rgba(30, 58, 138, 0.05) 40px
            );
            animation: diagonalMove 20s linear infinite;
            z-index: 0;
        }}

        @keyframes diagonalMove {{
            0% {{
                transform: translate(0, 0);
            }}
            100% {{
                transform: translate(50px, 50px);
            }}
        }}

        .intro-section h2 {{
            font-size: 2.8rem;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2rem;
            font-weight: 800;
            position: relative;
            z-index: 1;
        }}

        .intro-section p {{
            position: relative;
            z-index: 1;
        }}

        /* Footer */
        .footer {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 4rem 2rem 2rem;
            margin-top: 6rem;
            position: relative;
            overflow: hidden;
        }}

        .footer::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: repeating-linear-gradient(
                -45deg,
                transparent,
                transparent 40px,
                rgba(255, 255, 255, 0.05) 40px,
                rgba(255, 255, 255, 0.05) 80px
            );
            pointer-events: none;
        }}

        .footer-container {{
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
            position: relative;
            z-index: 1;
        }}

        .footer-section h3 {{
            margin-bottom: 1.5rem;
            font-size: 1.6rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }}

        .footer-section h3 i {{
            font-size: 1.8rem;
            animation: iconBounce 2s ease-in-out infinite;
        }}

        @keyframes iconBounce {{
            0%, 100% {{
                transform: translateY(0);
            }}
            50% {{
                transform: translateY(-5px);
            }}
        }}

        .footer-section p {{
            margin-bottom: 0.8rem;
            opacity: 0.95;
            line-height: 1.8;
        }}

        .footer-links {{
            list-style: none;
        }}

        .footer-links li {{
            margin-bottom: 0.8rem;
        }}

        .footer-links a {{
            color: white;
            text-decoration: none;
            transition: var(--transition);
            display: inline-block;
            opacity: 0.9;
        }}

        .footer-links a:hover {{
            opacity: 1;
            transform: translateX(8px);
            color: var(--accent-color);
        }}

        /* Social Media Links */
        .social-links {{
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }}

        .social-links a {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            text-decoration: none;
            transition: var(--transition);
            font-size: 1.2rem;
        }}

        .social-links a:hover {{
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }}

        .footer-bottom {{
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.2);
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }}

        /* Responsive Design */
        @media (max-width: 1200px) {{
            .hero h1 {{ font-size: 3.2rem; }}
            .section-text h2 {{ font-size: 2.5rem; }}
        }}

        @media (max-width: 968px) {{
            .menu-toggle {{
                display: flex;
            }}

            .nav-menu {{
                position: fixed;
                top: 0;
                right: -100%;
                width: 70%;
                max-width: 400px;
                height: 100vh;
                background: var(--background);
                flex-direction: column;
                padding: 6rem 2rem 2rem;
                box-shadow: var(--shadow-lg);
                transition: right 0.4s ease;
                align-items: stretch;
                gap: 0;
                min-width: auto;
            }}

            .nav-menu.active {{
                right: 0;
            }}

            .nav-link {{
                padding: 1.2rem;
                border-radius: 8px;
                margin-bottom: 0.5rem;
            }}

            .section-content {{
                grid-template-columns: 1fr;
                gap: 40px;
            }}

            .section-content.reverse {{
                direction: ltr;
            }}

            .hero h1 {{ font-size: 2.5rem; }}
            .hero h2 {{ font-size: 1.8rem; }}
            .hero-quote {{ font-size: 1.3rem !important; white-space: normal; }}
            
            .section-text::before {{
                display: none;
            }}

            /* Hide some floating circles on mobile */
            .floating-circle {{
                display: none;
            }}
        }}

        @media (max-width: 640px) {{
            .hero {{ padding: 7rem 1.5rem 4rem; }}
            .hero h1 {{ font-size: 2rem; }}
            .hero h2 {{ font-size: 1.5rem; }}
            .section-text h2 {{ font-size: 2rem; }}
            .content-section {{ padding: 80px 1.5rem 40px; }}

            .stats-grid {{
                flex-direction: column;
                align-items: center;
            }}

            .stat-card {{
                width: 100%;
                max-width: 300px;
            }}
        }}

        /* Smooth Scrolling */
        html {{
            scroll-behavior: smooth;
        }}

        /* Selection Styling */
        ::selection {{
            background: var(--primary-color);
            color: white;
        }}
    </style>
</head>
<body>
    <!-- Floating Background Gradient Circles -->
    <div class="floating-circle circle-1"></div>
    <div class="floating-circle circle-2"></div>
    <div class="floating-circle circle-3"></div>
    <div class="floating-circle circle-4"></div>

    <!-- Page Loader -->
    <div class="page-loader">
        <div class="loader"></div>
    </div>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="/" class="nav-logo">
                <i class="fas fa-star"></i>
                <span>Meyer</span>
            </a>
            <ul class="nav-menu">
                <li class="close-menu">
                    <button class="menu-toggle active" onclick="toggleMenu()">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </li>
                <li><a href="/" class="nav-link {'active' if current_page == 'home' else ''}">Home</a></li>
                <li><a href="/early-life" class="nav-link {'active' if current_page == 'early-life' else ''}">Early Life</a></li>
                <li><a href="/education" class="nav-link {'active' if current_page == 'education' else ''}">Education</a></li>
                <li><a href="/family" class="nav-link {'active' if current_page == 'family' else ''}">Family</a></li>
                <li><a href="/career" class="nav-link {'active' if current_page == 'career' else ''}">Career</a></li>
                <li><a href="/awards" class="nav-link {'active' if current_page == 'awards' else ''}">Awards</a></li>
                <li><a href="/contributions" class="nav-link {'active' if current_page == 'contributions' else ''}">Contributions</a></li>
                <li><a href="/philanthropy" class="nav-link {'active' if current_page == 'philanthropy' else ''}">Philanthropy</a></li>
            </ul>
            <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode">
                <i class="fas fa-moon"></i>
            </button>
            <button class="menu-toggle" onclick="toggleMenu()">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        {content}
    </main>

        <!-- Footer -->
    <footer class="footer">
      <div class="footer-container">

        <div class="footer-section">
          <h3><i class="fas fa-info-circle"></i> About</h3>
          <p>
            This website celebrates the life and achievements of a remarkable
            community leader who has made lasting impacts through dedication,
            passion, and service.
          </p>
        </div>

        <div class="footer-section">
          <h3><i class="fas fa-link"></i> Quick Links</h3>
          <ul class="footer-links">
            <li><a href="/">Home</a></li>
            <li><a href="/early-life">Early Life</a></li>
            <li><a href="/career">Career</a></li>
            <li><a href="/contributions">Contributions</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h3><i class="fas fa-envelope"></i> Contact</h3>
          <p><i class="fas fa-envelope"></i> Email: {CONTACT_EMAIL}</p>
          <p><i class="fas fa-phone"></i> Phone: {CONTACT_PHONE}</p>
          <p>
            <i class="fas fa-map-marker-alt"></i>
            Location: 1235 Cedar Lane Rd, Middletown, DE 19709
          </p>

          <div class="social-links">
            <a href="https://facebook.com" target="_blank" rel="noopener" aria-label="Facebook">
              <i class="fab fa-facebook-f"></i>
            </a>

            <a href="https://x.com" target="_blank" rel="noopener" aria-label="X">
              <i class="fab fa-x-twitter"></i>
            </a>

            <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="LinkedIn">
              <i class="fab fa-linkedin-in"></i>
            </a>

            <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="Instagram">
              <i class="fab fa-instagram"></i>
            </a>
          </div>
        </div>

      </div>

      <div class="footer-bottom">
        <p>&copy; 2025 BPA Web-Design Team. All rights reserved.</p>
      </div>
    </footer>

    <!-- AOS Animation Script -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

    <script>
        // Initialize AOS
        AOS.init({{
            duration: 1000,
            once: true,
            offset: 100,
            easing: 'ease-out-cubic'
        }});

        // Page Loader
        window.addEventListener('load', () => {{
            setTimeout(() => {{
                document.querySelector('.page-loader').classList.add('hidden');
            }}, 500);
        }});

        // Navbar scroll effect
        window.addEventListener('scroll', () => {{
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {{
                navbar.classList.add('scrolled');
            }} else {{
                navbar.classList.remove('scrolled');
            }}
        }});

        // Dark mode toggle
        function toggleTheme() {{
            const html = document.documentElement;
            const themeIcon = document.querySelector('.theme-toggle i');

            if (html.getAttribute('data-theme') === 'dark') {{
                html.removeAttribute('data-theme');
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
                localStorage.setItem('theme', 'light');
            }} else {{
                html.setAttribute('data-theme', 'dark');
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
                localStorage.setItem('theme', 'dark');
            }}
        }}

        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        // Default to dark mode if no preference stored; honor explicit 'light' choice
        const themeIcon = document.querySelector('.theme-toggle i');
        if (savedTheme === 'light') {{
            document.documentElement.removeAttribute('data-theme');
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
        }} else {{
            // If savedTheme === 'dark' OR no saved preference, enable dark mode by default
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
            localStorage.setItem('theme', 'dark');
        }}

        // Mobile menu toggle
        function toggleMenu() {{
            const navMenu = document.querySelector('.nav-menu');
            const menuToggle = document.querySelectorAll('.menu-toggle');

            navMenu.classList.toggle('active');
            menuToggle.forEach(toggle => toggle.classList.toggle('active'));
        }}

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {{
            const navMenu = document.querySelector('.nav-menu');
            const menuToggle = document.querySelector('.menu-toggle');

            if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {{
                navMenu.classList.remove('active');
                document.querySelectorAll('.menu-toggle').forEach(toggle => {{
                    toggle.classList.remove('active');
                }});
            }}
        }});

        // Animated counter for stats
        const animateCounter = (element, target) => {{
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {{
                current += increment;
                if (current >= target) {{
                    element.textContent = target.toLocaleString();
                    clearInterval(timer);
                }} else {{
                    element.textContent = Math.floor(current).toLocaleString();
                }}
            }}, 30);
        }};

        // Observer for stats animation
        const statsObserver = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    const target = parseInt(entry.target.getAttribute('data-target'));
                    animateCounter(entry.target, target);
                    statsObserver.unobserve(entry.target);
                }}
            }});
        }}, {{ threshold: 0.5 }});

        document.querySelectorAll('.stat-number').forEach(stat => {{
            statsObserver.observe(stat);
        }});
    </script>
</body>
</html>
    """


def get_home_content():
    # Get intro content - check if it exists, otherwise use default
    try:
        intro_title = HOME_INTRO.get('title', f'Celebrating {HERO_NAME}')
        intro_content = HOME_INTRO.get(
            'content', f'{HERO_NAME} has dedicated his life to serving the community and making a positive impact.')
    except NameError:
        # HOME_INTRO doesn't exist in config, use defaults
        intro_title = f'Celebrating {HERO_NAME}'
        intro_content = f'{HERO_NAME} has dedicated his life to serving the community and making a positive impact.'
    formatted_intro = format_content_with_lists(intro_content)

    return f"""
   <section class="hero">
       <div class="hero-content" data-aos="fade-up">
           <h1>{HERO_NAME}</h1>
           <h2>{HERO_TITLE}</h2>
           <p class="hero-quote">{HERO_QUOTE}</p>
           <a href="#intro-section" class="cta-button">Explore his Impact</a>
       </div>
   </section>

   <div id="intro-section" class="content-section">
       <div class="intro-section" data-aos="zoom-in">
           <h2>{intro_title}</h2>
           <div class="intro-content">
           {formatted_intro}
           </div>
       </div>
   </div>

   <div class="content-section" style="display: block;">
       <h2 class="impact-heading" data-aos="fade-up">Impact at a Glance</h2>
       <div class="stats-grid">
           <div class="stat-card" data-aos="fade-up" data-aos-delay="0">
               <i class="fas fa-users"></i>
               <div class="stat-number" data-target="1500">0</div>
               <div class="stat-label">Lives Impacted</div>
           </div>
           <div class="stat-card" data-aos="fade-up" data-aos-delay="100">
               <i class="fas fa-award"></i>
               <div class="stat-number" data-target="25">0</div>
               <div class="stat-label">Awards Received</div>
           </div>
           <div class="stat-card" data-aos="fade-up" data-aos-delay="200">
               <i class="fas fa-calendar"></i>
               <div class="stat-number" data-target="15">0</div>
               <div class="stat-label">Years of Service</div>
           </div>
           <div class="stat-card" data-aos="fade-up" data-aos-delay="300">
               <i class="fas fa-heart"></i>
               <div class="stat-number" data-target="50">0</div>
               <div class="stat-label">Community Programs</div>
           </div>
       </div>
   </div>

   <div class="content-section" style="display: block; text-align: center;">
       <div class="impact-cta" data-aos="fade-up">
           <h2>How Can You Amplify Your Impact?</h2>
           <p>Inspired by the remarkable journey of {HERO_NAME}? Learn how you can make a meaningful difference in your community. Whether through volunteering, mentoring, or advocating for change, discover the steps to amplify your impact like a true community leader.</p>
           <a href="/contributions" class="cta-button">Explore his Path</a>
       </div>
   </div>
   """


def get_early_life_content():
    content_text = EARLY_LIFE.get(
        'content', 'Content about early life experiences and background.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content">
           <div class="section-text" data-aos="fade-right">
               <h2>{EARLY_LIFE.get('title', 'Early Life')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image early-life-image" data-aos="fade-left">
               <img src="{EARLY_LIFE.get('image', '/static/images/early-life.jpg')}"
                    alt="{EARLY_LIFE.get('title', 'Early Life')}">
           </div>
       </div>
   </div>
   """


def get_education_content():
    content_text = EDUCATION.get(
        'content', 'Content about educational background and achievements.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content reverse">
           <div class="section-text" data-aos="fade-left">
               <h2>{EDUCATION.get('title', 'Education')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-right">
               <img src="{EDUCATION.get('image', '/static/images/education.jpg')}" 
                    alt="{EDUCATION.get('title', 'Education')}">
           </div>
       </div>
   </div>
   """


def get_family_content():
    content_text = FAMILY.get(
        'content', 'Content about family life and relationships.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content">
           <div class="section-text" data-aos="fade-right">
               <h2>{FAMILY.get('title', 'Family')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-left">
               <img src="{FAMILY.get('image', '/static/images/family.jpg')}" 
                    alt="{FAMILY.get('title', 'Family')}">
           </div>
       </div>
   </div>
   """


def get_career_content():
    content_text = CAREER.get(
        'content', 'Content about professional career and achievements.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content reverse">
           <div class="section-text" data-aos="fade-left">
               <h2>{CAREER.get('title', 'Career')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-right">
               <img src="{CAREER.get('image', '/static/images/career.jpg')}" 
                    alt="{CAREER.get('title', 'Career')}">
           </div>
       </div>
   </div>
   """


def get_awards_content():
    content_text = AWARDS.get(
        'content', 'Content about awards and recognitions received.')
    formatted_content = format_content_with_lists(content_text)

    # Check if there's an additional image
    additional_image = AWARDS.get('additional_image', '')
    additional_image_html = ''
    if additional_image:
        additional_image_html = f'''
           <div class="awards-image-container" data-aos="fade-right" data-aos-delay="200">
               <img src="{additional_image}" 
                    alt="{AWARDS.get('title', 'Awards')} - Additional">
           </div>
        '''

    return f"""
   <div class="content-section">
       <div class="section-content reverse">
           <div class="section-text" data-aos="fade-left">
               <h2>{AWARDS.get('title', 'Awards')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="awards-images-wrapper">
               <div class="awards-image-container" data-aos="fade-right">
                   <img src="{AWARDS.get('image', '/static/images/awards.jpg')}" 
                        alt="{AWARDS.get('title', 'Awards')}">
               </div>
               {additional_image_html}
           </div>
       </div>
   </div>
   """


def get_contributions_content():
    content_text = CONTRIBUTIONS.get(
        'content', 'Content about community contributions and impact.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content">
           <div class="section-text" data-aos="fade-right">
               <h2>{CONTRIBUTIONS.get('title', 'Contributions')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-left">
               <img src="{CONTRIBUTIONS.get('image', '/static/images/contributions.jpg')}" 
                    alt="{CONTRIBUTIONS.get('title', 'Contributions')}">
           </div>
       </div>
   </div>
   """


def get_community_content():
    content_text = COMMUNITY.get(
        'content', 'Content about community involvement and initiatives.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content">
           <div class="section-text" data-aos="fade-right">
               <h2>{COMMUNITY.get('title', 'Community')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-left">
               <img src="{COMMUNITY.get('image', '/static/images/community.jpg')}" 
                    alt="{COMMUNITY.get('title', 'Community')}">
           </div>
       </div>
   </div>
   """


def get_philanthropy_content():
    content_text = PHILANTHROPY.get(
        'content', 'Content about philanthropic efforts and charitable work.')
    formatted_content = format_content_with_lists(content_text)

    return f"""
   <div class="content-section">
       <div class="section-content reverse">
           <div class="section-text" data-aos="fade-left">
               <h2>{PHILANTHROPY.get('title', 'Philanthropy')}</h2>
               <div class="content-text">
               {formatted_content}
               </div>
           </div>
           <div class="section-image" data-aos="fade-right">
               <img src="{PHILANTHROPY.get('image', '/static/images/philanthropy.jpg')}" 
                    alt="{PHILANTHROPY.get('title', 'Philanthropy')}">
           </div>
       </div>
   </div>
   """
