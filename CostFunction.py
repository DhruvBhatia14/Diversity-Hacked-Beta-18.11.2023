from playwright.sync_api import sync_playwright


"""def get_calculated_tuition(province, school, area_of_study):
    with sync_playwright() as p:

        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

    
        page.goto('https://www.getsmarteraboutmoney.ca/calculators/education-cost-calculator/')
    
        print("Timing measured for:", school, b) 

        frame = page.wait_for_selector('iframe[title="tool-embed-frame"]')
        frame_context = frame.content_frame()

        page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("Province:").select_option(province)
        page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("School:").select_option(school)
        page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("Area of Study:").select_option(area_of_study)

        frame_context.click('text="Next"')
        page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_role("button", name="Next").click()
       
        tuition = page.frame_locator("iframe[title=\"tool-embed-frame\"]").locator("#total-school-costs").inner_text()

        context.close()
        browser.close()
        return tuition"""

transformed_dict = { 'University of Alberta': 'AB',
    'Alberta University of the Arts': 'AB',
    'Grant MacEwan University': 'AB',
    'University of Calgary': 'AB',
    'Mount Royal University': 'AB',
    'University of Lethbridge': 'AB',
    'Athabasca University': 'AB',
    'University of British Columbia': 'BC',
    'Simon Fraser University': 'BC',
    'University of Victoria': 'BC',
    'University of Northern British Columbia': 'BC',
    'Thompson Rivers University': 'BC',
    'Royal Roads University': 'BC',
    'Capilano University': 'BC',
    'Emily Carr University of Art and Design': 'BC',
    'Kwantlen Polytechnic University': 'BC',
    'Justice Institute of British Columbia': 'BC',
    'Vancouver Island University': 'BC',
    'University of the Fraser Valley': 'BC',
    'University of Manitoba': 'MB',
    'University of Winnipeg': 'MB',
    'Brandon University': 'MB',
    'Université de Saint-Boniface': 'MB',
    'University of New Brunswick': 'NB',
    'Mount Allison University': 'NB',
    'St. Thomas University': 'NB',
    'Université de Moncton': 'NB',
    'Memorial University of Newfoundland': 'NL',
    'Dalhousie University': 'NS',
    "Saint Mary's University": 'NS',
    'Acadia University': 'NS',
    "University of King's College": 'NS',
    'Cape Breton University': 'NS',
    'Mount St. Vincent University': 'NS',
    'St. Francis Xavier University': 'NS',
    'NSCAD University': 'NS',
    'University of Toronto': 'ON',
    "University of Ottawa-Université d'Ottawa": 'ON',
    'York University': 'ON',
    'McMaster University': 'ON',
    'University of Waterloo': 'ON',
    'Western University': 'ON',
    "Queen's University": 'ON',
    'Carleton University': 'ON',
    'Toronto Metropolitan University': 'ON',
    'University of Guelph': 'ON',
    'Brock University': 'ON',
    'Wilfrid Laurier University': 'ON',
    'Lakehead University': 'ON',
    'Trent University': 'ON',
    'Ontario Tech University': 'ON',
    'University of Windsor': 'ON',
    'Algoma University': 'ON',
    'Nipissing University': 'ON',
    'Laurentian University': 'ON',
    'University of Prince Edward Island': 'PEI',
    'McGill University': 'QC',
    'Université de Montréal': 'QC',
    'Université Laval': 'QC',
    'Concordia University': 'QC',
    "Bishop's University": 'QC',
    'University of Saskatchewan': 'SK',
    'University of Regina': 'SK',
    'Yukon College': 'YT'
    # Your transformed_dict data remains unchanged
}

Specific_general_conversion = {'Administration Studies': "Business, Mgt and Public Administration",
    'Art Studies': "Visual & performing Arts, and Comm. Technologies",
    'Aviation': "Physical and Life Sciences and Technologies",
    'Business Studies': "Business, Mgt and Public Administration",
    'Construction': "Architecture and Related Technologies",
    'Design Studies': "Visual & performing Arts, and Comm. Technologies",
    'Economic Studies': "Business, Mgt and Public Administration",
    'Education': 'Education',
    'Energy Studies': "Physical and Life Sciences and Technologies",
    'Engineering Studies': "Engineering",
    'Environmental Studies': "Agriculture, Natural Resources and Conservation",
    'Fashion': "Visual & performing Arts, and Comm. Technologies",
    'Food and Beverage Studies': "Physical and Life Sciences and Technologies",
    'General Studies': "Physical and Life Sciences and Technologies",
    'Health Care': "Nursing",
    'Humanities Studies': "Humanities",
    'Journalism and Mass Communication': "Visual & performing Arts, and Comm. Technologies",
    'Languages': "Visual & performing Arts, and Comm. Technologies",
    'Law Studies': "Law",
    'Life Sciences': "Physical and Life Sciences and Technologies",
    'Management Studies': "Business, Mgt and Public Administration",
    'Marketing Studies': "Business, Mgt and Public Administration",
    'Natural Sciences': "Physical and Life Sciences and Technologies",
    'Performing Arts': "Visual & performing Arts, and Comm. Technologies",
    'Social Sciences': "Humanities",
    'Sport': "Other Health, Parks, Recreation and Fitness",
    'Sustainability Studies': "Agriculture, Natural Resources and Conservation",
    'Technology Studies': "Math, Computer and Information Sciences",
    'Tourism and Hospitality': "Business, Mgt and Public Administration",
    'Transportation and Logistics': "Personal, Protective and Transportation services" 
}

def CostCalc(majors,universities):
    
    major = majors[0]
    scrape_major = Specific_general_conversion[major]
    major = scrape_major
    output = {}


    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        for uni in universities:
          
            page.goto('https://www.getsmarteraboutmoney.ca/calculators/education-cost-calculator/')
           
            frame = page.wait_for_selector('iframe[title="tool-embed-frame"]')
            frame_context = frame.content_frame()

            page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("Province:").select_option(transformed_dict.get(uni))
            page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("School:").select_option(uni)

            page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_label("Area of Study:").select_option(major)
            frame_context.click('text="Next"')
            page.frame_locator("iframe[title=\"tool-embed-frame\"]").get_by_role("button", name="Next").click()
            tuition = page.frame_locator("iframe[title=\"tool-embed-frame\"]").locator("#total-school-costs").inner_text()

            output[uni] = tuition

        context.close()
        browser.close()

    return(output)




