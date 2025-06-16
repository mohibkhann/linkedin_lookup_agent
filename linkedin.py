import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        # Generate generic mock data
        data = {
            "profile_pic_url": "https://via.placeholder.com/150",
            "name": linkedin_profile_url.split("/in/")[-1].replace("-", " ").title(),
            "headline": "Professional | Industry Expert | Problem Solver",
            "summary": "Experienced professional with a track record of success in various industries. Passionate about continuous learning and making a positive impact.",
            "experiences": [
                {
                    "title": "Senior Professional",
                    "company": "Global Solutions Inc",
                    "date_range": "2020 - Present",
                    "description": "Leading key initiatives and driving organizational success"
                },
                {
                    "title": "Professional",
                    "company": "Enterprise Solutions",
                    "date_range": "2018 - 2020",
                    "description": "Contributed to various projects and team success"
                }
            ],
            "education": [
                {
                    "school": "University of Excellence",
                    "degree": "Bachelor's Degree",
                    "date_range": "2014 - 2018"
                }
            ],
            "skills": ["Leadership", "Project Management", "Communication", "Problem Solving", "Team Collaboration"],
            "groups": [
                {
                    "name": "Professional Network",
                    "url": "https://www.linkedin.com/groups/123456"
                },
                {
                    "name": "Industry Leaders",
                    "url": "https://www.linkedin.com/groups/789012"
                }
            ]
        }
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
        data = response.json()
        
        # Debug the raw response
        print("\nRaw Scrapin API Response:")
        print(f"Profile Picture URL: {data.get('profile_pic_url')}")
        
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }
        
        # Debug the processed data
        print("\nProcessed Data:")
        print(f"Profile Picture URL: {data.get('profile_pic_url')}")
        
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://my.linkedin.com/in/mohibalikhan/",
        )
    )
