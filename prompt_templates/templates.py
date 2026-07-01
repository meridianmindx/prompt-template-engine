"""LLM Prompt Templates Library - curated collection for common use cases."""

TEMPLATES = {
    "cold_outreach": [
        {
            "name": "cold_email_template",
            "description": "Professional cold email template",
            "template": "Subject: {{subject_line}}\n\nHi {{name}},\n\nI noticed you are {{interest}} at {{company}}.\n\n{{personalized_message}}\n\nWould you be open to a quick 15-minute call this week?\n\nBest,\n{{sender_name}}"
        },
        {
            "name": "cold_email_template_v2",
            "description": "Cold email with value proposition",
            "template": "Hi {{name}},\n\nI saw your work on {{topic}} and loved {{specific_point}}.\n\nWe helped {{company}} achieve {{outcome}} in {{timeframe}}.\n\nWant me to send over a quick breakdown of how?\n\n{{signature}}"
        },
        {
            "name": "followup_template",
            "description": "Follow-up to cold email",
            "template": "Hi {{name}},\n\nJust following up on my last note. Did you get a chance to review?\n\nWould love to chat about {{topic}} when you have 10 mins.\n\n{{signature}}"
        },
        {
            "name": "warm_lead_followup",
            "description": "Follow-up for warm lead",
            "template": "Hi {{name}},\n\nHope you are doing well! I wanted to circle back about {{topic}}.\n\nLet me know if you would like to explore further.\n\n{{signature}}"
        },
        {
            "name": "linkedin_outreach",
            "description": "Cold LinkedIn message template",
            "template": "Hi {{name}},\n\nI've been following your posts about {{topic}} at {{company}}. \n\nI help companies like {{company}} solve {{pain_point}}. Would you be open to a brief chat about {{topic}}?\n\nBest,\n{{sender_name}}"
        }
    ],
    "content_generation": [
        {
            "name": "blog_post_template",
            "description": "Blog post template",
            "template": "Title: {{title}}\n\nIntro: {{intro}}\n\nBody: {{body}}\n\nConclusion: {{conclusion}}\n\nCTA: {{cta}}"
        },
        {
            "name": "social_media_post",
            "description": "Social media post template",
            "template": "{{headline}}\n\n{{body}}\n\n#{{hashtag1}} #{{hashtag2}}"
        },
        {
            "name": "newsletter_template",
            "description": "Newsletter/email template",
            "template": "Subject: {{subject_line}}\n\n{{headline}}\n\n{{content}}\n\nP.S. {{postscript}}\n\n{{signature}}"
        }
    ],
    "sales_copywriting": [
        {
            "name": "product_page_copy",
            "description": "Product landing page copy",
            "template": "# {{product_name}}\n\n{{headline}}\n\n**Key Benefits:**\n- {{benefit_1}}\n- {{benefit_2}}\n- {{benefit_3}}\n\n**CTA:** {{cta_text}}"
        },
        {
            "name": "email_sales_copy",
            "description": "Sales email template",
            "template": "Subject: {{subject_line}}\n\n{{opening}}\n\n**What You Will Get:**\n- {{offer_1}}\n- {{offer_2}}\n\n**Special Offer:** {{deal}}\n\n**Deadline:** {{deadline}}\n\n{{closing}}"
        },
        {
            "name": "sales_landing_page",
            "description": "Sales landing page copy",
            "template": "# {{product_name}}\n\nHeadline: {{headline}}\n\n**Benefits:**\n- {{benefit_1}}\n- {{benefit_2}}\n\n**Pricing:** {{price}}\n\n**CTA:** {{cta_text}}\n\n**Risk Reversal:** {{guarantee}}"
        }
    ],
    "technical_docs": [
        {
            "name": "api_documentation",
            "description": "API documentation template",
            "template": "# API Endpoint: {{endpoint_name}}\n\n## Description\n{{description}}\n\n## Request\n{{request_format}}\n\n## Response\n{{response_format}}\n\n## Examples\n{{examples}}"
        },
        {
            "name": "release_notes",
            "description": "Release notes template",
            "template": "# Release Notes - {{version}}\n\n## New Features\n- {{feature_1}}\n- {{feature_2}}\n\n## Bug Fixes\n- {{fix_1}}\n- {{fix_2}}\n\n## Known Issues\n- {{issue_1}}"
        },
        {
            "name": "changelog_template",
            "description": "Changelog template",
            "template": "# Changelog\n\n## [{{version}}] - {{date}}\n\n### Added\n- {{addition_1}}\n### Fixed\n- {{fix_1}}"
        }
    ],
    "social_media": [
        {
            "name": "twitter_thread",
            "description": "Twitter/X thread template",
            "template": "# Title: {{title}}\n\n1/ {{intro}}\n\n2/ {{point_1}}\n\n3/ {{point_2}}\n\n4/ {{point_3}}\n\n5/ {{conclusion}}\n\n#{{hashtag}}"
        },
        {
            "name": "linkedin_post",
            "description": "LinkedIn post template",
            "template": "{{headline}}\n\n{{body}}\n\n#{{hashtag1}} #{{hashtag2}}"
        },
        {
            "name": "reddit_post_template",
            "description": "Reddit post template",
            "template": "Title: {{title}}\n\n{{body}}\n\n---\n**TL;DR:** {{tl_dr}}\n\n**Links:** {{links}}"
        }
    ]
}


def get_templates(category=None):
    """Get templates, optionally filtered by category.
    
    Args:
        category: Optional category filter (e.g., 'cold_outreach', 'content_generation')
    
    Returns:
        List of template dictionaries or dict of templates by category
    """
    if category:
        return TEMPLATES.get(category, [])
    return TEMPLATES


def get_template(category, template_name):
    """Get a specific template by category and name.
    
    Args:
        category: The template category
        template_name: The specific template name
    
    Returns:
        Template dictionary or None
    """
    templates = TEMPLATES.get(category, [])
    for template in templates:
        if template["name"] == template_name:
            return template
    return None


def generate(template, **kwargs):
    """Generate output by replacing {{vars}} in template with values.
    
    Args:
        template: Template string with {{variable}} placeholders
        **kwargs: Values to replace in template
    
    Returns:
        Generated string with all replacements made
    """
    result = template
    for key, value in kwargs.items():
        result = result.replace("{{" + key + "}}", str(value))
    return result
