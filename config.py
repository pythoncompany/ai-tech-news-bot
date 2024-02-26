# Set your name
NAME = "Ida"

# Choose your OpenAI Model (Chat only) - GPT-3.5 Turbo is 13x cheaper than GPT-4
MODEL_NAME = "gpt-3.5-turbo-0125"

# Word count for keyword summaries (the longer the more detailed the summaries will be)
WORD_COUNT = '150'

# Define category limits for the trending keywords - it will grab by top count first (check safron.io to look over your options)
CATEGORY_LIMITS = {
    "Subjects": 4,
    "Tools & Services": 4,
    "Websites & Applications": 4,
    "Concepts & Methods": 4,
    "Platforms & Search Engines": 4,
    "Companies & Organizations": 4,
    "Hardware & Systems": 4,
    "Languages & Syntax": 4,
    "Frameworks & Libraries": 3,
    "People": 5,
    "AI Models & Assistants": 5
}

# Set your keywords of interest - should always be there regardless if they are trending yesterday or not
KEYWORDS_OF_INTEREST = ["AI", "Google", "AWS", "OpenAI", "Machine Learning", "LLMs", "Cloud", "Serverless", "Lowcode", "No Code", "Make"]

# Set a category as something that is always there - categories grabs the highest count rather than if trending
CATEGORIES_OF_INTEREST = [{"category": "AI Models & Assistants", "limit": 10}]

########## SES Email Configs - Make sure you change these ########

SOURCE_EMAIL = 'noreply@safron.io' 
TO_ADRESS = 'ilsilfverskiold@gmail.com'
AWS_REGION_NAME = 'eu-north-1'


