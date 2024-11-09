def check_compatibility(product_profile, customer_profile):
    # Compatibility checks
    compatibility_results = {
        "Country Match": customer_profile["Location"] in product_profile["focusCountries"],
        "Company Type Match": any(
            uc["category"] == customer_profile["CompanyType"] and uc["available"] 
            for uc in product_profile["userCategory"]
        ),
        "Language Match": any(
            lang in product_profile["languages"] 
            for lang in customer_profile["PrimaryLanguage"]
        ),
        "Industry Match": any(
            ind["industry"] in customer_profile["Industry"] and ind["available"] 
            for ind in product_profile["industry"]
        ),
        "Team Size Match": any(
            ts["size"] == customer_profile["TeamSize"] and ts["available"] 
            for ts in product_profile["teamSize"]
        ),
        "Goal Match": "Cost efficiency" in customer_profile["Goals"]
    }
    return compatibility_results

# Example profiles
# {
#     "focusCountries": ["India", "Philippines", "Indonesia", "Saudi Arabia", "Singapore"],
#     "languages": ["English"],
#     "userCategory": [
#         {"category": "Enterprises", "percentage": 100, "available": true},
#         {"category": "Startups", "percentage": 0, "available": false}
#     ],
#     "industry": [
#         {"industry": "Construction and Engineering", "percentage": 0, "available": true},
#         {"industry": "Energy and Utilities", "percentage": 0, "available": true}, 
#         {"industry": "Manufacturing", "percentage": 0, "available": true},
#         {"industry": "Media and Entertainment", "percentage": 0, "available": true},
#         {"industry": "Real Estate", "percentage": 0, "available": true},
#         {"industry": "Technology and Software", "percentage": 0, "available": true},
#         {"industry": "Defence", "percentage": 50, "available": true},
#         {"industry": "Retail and Consumer Goods", "percentage": 50, "available": true}
#     ],
#     "teamSize": [
#         {"size": "2-20", "percentage": 50, "available": true},
#         {"size": "21-50", "percentage": 50, "available": true}
#     ]
# }

# customer_profile = {
#     "Location": "India",
#     "CompanyType": "Startups",
#     "PrimaryLanguage": ["Spanish"],
#     "Industry": ["Banking and Finance"],
#     "TeamSize": "2-20",
#     "Goals": ["Cost efficiency"]
# }

# Run compatibility test
# compatibility_results = check_compatibility(product_profile, customer_profile)
# print(compatibility_results)
