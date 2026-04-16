from jinja2 import Template


def generate_resume(
    name,
    phone,
    email,
    education,
    leetcode=None,
    linkedin=None,
    github=None,
    portfolio=None,
    summary=None,
    experience=None,
    projects=None,
    certifications=None,
    achievements=None,
    output_file="resume.html"
):
    # Merge all arguments into a single dictionary for the template
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "education": education,
        "leetcode": leetcode,
        "linkedin": linkedin,
        "github": github,
        "portfolio": portfolio,
        "summary": summary,
        "experience": experience,
        "projects": projects,
        "certifications": certifications,
        "achievements": achievements,
    }

    template_str = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{{ name }}</title>
<style>
body {
  font-family: Arial;
  margin: 40px;
  color: #222;
  line-height: 1.5;
}
h1 {
  margin-bottom: 5px;
  text-align: center;
  font-weight: bold;
  font-size: 20px;
}
h2 {
  border-bottom: 2px solid #000;
  margin-top: 25px;
  font-size: 18px;
}
.header {
  text-align: center;
  margin-bottom: 15px;
}
.header .name {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 5px;
}
.header .contact {
  font-size: 14px;
  font-weight: normal;
  margin-bottom: 10px;
}
.header .contact a {
  color: #000;
  text-decoration: none;
}
.header .contact span {
  margin: 0 5px;
}
.header hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 10px 0;
  width: 100%;
}
.description {
  text-align: left;
  font-size: 14px;
  margin: 15px auto;
  line-height: 1.6;
  max-width: 800px;
  background-color: #f9f9f9;
}
.item { margin-bottom: 12px; }
.title { font-weight: bold; }
.sub { font-size: 13px; color: #555; }
ul { margin: 5px 0 0 18px; }
li { margin-bottom: 4px; }
a { color: #000; text-decoration: none; }
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="name">{{ name }}</div>
  <div class="contact">
    {% if email %}
    <span>{{ email }}</span> |
    {% endif %}
    {% if phone %}
    <span>{{ phone }}</span> |
    {% endif %}
    {% if linkedin %} <a href="{{ linkedin }}">LinkedIn</a> |{% endif %}
    {% if github %} <a href="{{ github }}">GitHub</a> |{% endif %}
    {% if leetcode %} <a href="{{ leetcode }}">LeetCode</a> {% endif %}
    {% if portfolio %} <a href="|{{ portfolio }}">Portfolio</a>{% endif %}
  </div>
  <hr>
</div>

<!-- DESCRIPTION -->
{% if summary %}
<div class="description">
  {{ summary }}
  {% if portfolio %}
  <p><strong>Portfolio:</strong> <a href="{{ portfolio }}">{{ portfolio }}</a></p>
  {% endif %}
</div>
{% endif %}

<!-- EDUCATION -->
{% if education %}
<h2>Education</h2>
{% for edu in education %}
<div class="item">
  <div class="title">{{ edu['institute'] }} — {{ edu['city'] }}</div>
  <div class="sub">
    {{ edu['degree'] }} | {{ edu['score'] }} ({{ edu['duration'] }})
  </div>
</div>
{% endfor %}
{% endif %}

<!-- EXPERIENCE -->
{% if experience %}
<h2>Professional Experience</h2>
{% for exp in experience %}
<div class="item">
  <div class="title">{{ exp['role'] }} | {{ exp['company'] }}</div>
  <div class="sub">{{ exp['duration'] }} — {{ exp['location'] }}</div>
  <ul>
    {% for p in exp['points'] %}
    <li>{{ p }}</li>
    {% endfor %}
  </ul>
</div>
{% endfor %}
{% endif %}

<!-- PROJECTS -->
{% if projects %}
<h2>Projects</h2>
{% for proj in projects %}
<div class="item">
  <div class="title">
    {{ proj['name'] }}
    {% if proj['link'] %} | <a href="{{ proj['link'] }}">Link</a>{% endif %}
  </div>
  <ul>
    {% for p in proj['points'] %}
    <li>{{ p }}</li>
    {% endfor %}
  </ul>
</div>
{% endfor %}
{% endif %}

<!-- CERTIFICATIONS -->
{% if certifications %}
<h2>Certifications</h2>
<ul>
{% for cert in certifications %}
<li>{{ cert }}</li>
{% endfor %}
</ul>
{% endif %}

<!-- ACHIEVEMENTS -->
{% if achievements %}
<h2>Awards & Achievements</h2>
<ul>
{% for a in achievements %}
<li>{{ a }}</li>
{% endfor %}
</ul>
{% endif %}

</body>
</html>"""

    template = Template(template_str)
    html = template.render(**data)  # Unpack the merged data dictionary

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    return output_file

if __name__=="__main__":
    name = "Vishwajeet Patil"
    phone = "+91 8088115807"
    email = "vishwajeetrajpatil2002@gmail.com"
    linkedin = "https://www.linkedin.com/in/vishwajeet-r-patil/"
    github = "https://github.com/vishwapatill"
    leetcode = "https://leetcode.com/vishwapatill"
    education = [
        {
            "institute": "PES University",
            "city": "Bengaluru",
            "degree": "B.Tech Computer Science",
            "score": "8.31 CGPA",
            "duration": "2021 – 2025"
        },
        {
            "institute": "CB Gurukul PU College",
            "city": "Bhalki",
            "degree": "PCMB",
            "score": "90.5%",
            "duration": "2019 – 2021"
        }
    ]
    portfolio = "https://vishwajeetpatill.netlify.app/"
    summary = """
    I'm a Software developer with a strong foundation in Database design, Data science and Machine Learning,
    eager to apply my technical skills to innovative projects. My passion lies in building software solutions
    with real-world impact. Skilled in deploying applications by integrating AI/ML models with modern web
    technologies to solve complex and real-world challenges.
    """
    experience = [
        {
            "role": "Analyst",
            "company": "Deloitte USI",
            "duration": "Jul 2025 – Present",
            "location": "Bangalore",
            "points": [
                "Working as Data Conversion Analyst",
                "Handling enterprise data workflows"
            ]
        },
        {
            "role": "Data Science Engineer",
            "company": "Evam Labs",
            "duration": "Jan 2025 – Jun 2025",
            "location": "India",
            "points": [
                "Reduced third-party costs by 75%",
                "Cut compute usage by 50–70%",
                "Built AI systems (CNNs, embeddings, agents)"
            ]
        }
    ]
    projects = [
        {
            "name": "Food Pairing Recommendation",
            "link": "https://github.com/vishwapatill/FOOD-PAIRING-RECOMMENDATION-SYSTEM-USING-GRAPHS",
            "points": [
                "Graph-based ingredient modeling",
                "Metapath2vec embeddings",
                "Trained on 6000 recipes"
            ]
        },
        {
            "name": "Outfit Compatibility Model",
            "link": "https://github.com/vishwapatill/WARDROBE-WIZARD",
            "points": [
                "Used ResNet-50 + YOLOv8",
                "Triplet loss embedding model",
                "Improved compatibility prediction"
            ]
        },
        {
            "name": "House Rental App (Nimma Manne)",
            "link": "https://nimmamane.in/",
            "points": [
                "Full-stack React + PostgreSQL app",
                "Implemented RLS security",
                "Built production-ready system"
            ]
        }
    ]
    certifications = [
        "Web Developer Bootcamp — Udemy",
        "Machine Intelligence — PES University",
        "AWS Databases Certification"
    ]
    achievements = [
        "District Level Volleyball Player (2018, 2019)"
    ]

    # Generate HTML
    html_file = generate_resume(
        name=name,
        phone=phone,
        email=email,
        education=education,
        leetcode=leetcode,
        linkedin=linkedin,
        github=github,
        summary=summary,
        experience=experience,
        projects=projects,
        certifications=certifications,
        achievements=achievements
    )
    