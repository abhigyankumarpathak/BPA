from flask import Flask, render_template_string, request, redirect, url_for
from config import *
from templates import (
    get_base_html, get_home_content, get_early_life_content,
    get_education_content, get_family_content, get_career_content,
    get_contributions_content, get_awards_content, get_community_content,
    get_philanthropy_content
)


def register_routes(app):
    """Register all Flask routes"""

    @app.route('/')
    def home():
        content = get_home_content()
        return render_template_string(get_base_html(content, "Home", "home", HERO_IMAGE))

    @app.route('/early-life')
    def early_life():
        content = get_early_life_content()
        return render_template_string(get_base_html(content, "Early Life", "early-life", HERO_IMAGE))

    @app.route('/education')
    def education():
        content = get_education_content()
        return render_template_string(get_base_html(content, "Education", "education", HERO_IMAGE))

    @app.route('/family')
    def family():
        content = get_family_content()
        return render_template_string(get_base_html(content, "Family", "family", HERO_IMAGE))

    @app.route('/career')
    def career():
        content = get_career_content()
        return render_template_string(get_base_html(content, "Career", "career", HERO_IMAGE))

    @app.route('/contributions')
    def contributions():
        content = get_contributions_content()
        return render_template_string(get_base_html(content, "Contributions", "contributions", HERO_IMAGE))

    @app.route('/awards')
    def awards():
        content = get_awards_content()
        return render_template_string(get_base_html(content, "Awards", "awards", HERO_IMAGE))

    @app.route('/community')
    def community():
        content = get_community_content()
        return render_template_string(get_base_html(content, "Community", "community", HERO_IMAGE))

    @app.route('/philanthropy')
    def philanthropy():
        content = get_philanthropy_content()
        return render_template_string(get_base_html(content, "Philanthropy", "philanthropy", HERO_IMAGE))

    @app.errorhandler(404)
    def page_not_found(e):
        content = """
        <div class="content-section" style="text-align: center; padding: 100px 20px;">
            <h1 style="font-size: 4rem; color: var(--primary-color); margin-bottom: 20px;">404</h1>
            <h2 style="font-size: 2rem; margin-bottom: 30px;">Page Not Found</h2>
            <p style="font-size: 1.2rem; margin-bottom: 40px;">The page you are looking for does not exist.</p>
            <a href="/" class="cta-button">Return Home</a>
        </div>
        """
        return render_template_string(get_base_html(content, "404 Error", "error", HERO_IMAGE)), 404
