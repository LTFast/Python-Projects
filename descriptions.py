from bs4 import BeautifulSoup
import bs4
import requests
import csv
"""
Created 2/6/2020
This program scrapes the individual FindWell neighborhood description pages then
stores data in to a csv

Columns of the csv = ['neighborhood', 'description', 'history', 'vibe', 'activities_attractions']

Links have been obtained from a previous scrape 
of all links in the FindWell Homepage for Seattle
"""

# indexes 33-90 are the Needed Neighborhood Links
links = ['https://www.findwell.com/', '#', 'https://www.findwell.com/buy-home-with-findwell', 'https://www.findwell.com/buy-your-home-how-it-works', 'https://www.findwell.com/home-buying-guide', 'https://www.findwell.com/open-house-anytime', '#', 'https://www.findwell.com/sell-home-with-findwell', 'https://www.findwell.com/sell-your-home-how-it-works', 'https://www.findwell.com/home-selling-guide', 'https://www.findwell.com/what-is-my-home-worth', '#', 'https://seattle.findwell.com/seattle-neighborhoods/', 'https://seattle.findwell.com/greater-seattle/', '#', 'https://www.findwell.com/resources', 'https://www.findwell.com/home-buying-class', 'https://www.findwell.com/calculators', 'https://www.findwell.com/real-estate-dictionary', '#', 'https://www.findwell.com/real-estate-agents', 'https://www.findwell.com/about', 'https://www.findwell.com/findwell-advantage', 'https://www.findwell.com/real-estate-myth-busters', 'https://www.findwell.com/findwell-customer-reviews', 'https://www.findwell.com/careers', 'https://www.findwell.com/press', 'https://seattle.findwell.com/contact/', 'http://blog.findwell.com/', '#', 'https://seattle.findwell.com/contact/', None, 'https://seattle.findwell.com/seattle-neighborhoods/', 'https://seattle.findwell.com/seattle-neighborhoods/belltown/', 'https://seattle.findwell.com/seattle-neighborhoods/broadmoor/', 'https://seattle.findwell.com/seattle-neighborhoods/capitol-hill/', 'https://seattle.findwell.com/seattle-neighborhoods/central-district/', 'https://seattle.findwell.com/seattle-neighborhoods/denny-blaine/', 'https://seattle.findwell.com/seattle-neighborhoods/downtown/', 'https://seattle.findwell.com/seattle-neighborhoods/eastlake/', 'https://seattle.findwell.com/seattle-neighborhoods/first-hill/', 'https://seattle.findwell.com/seattle-neighborhoods/international-district/', 'https://seattle.findwell.com/seattle-neighborhoods/leschi/', 'https://seattle.findwell.com/seattle-neighborhoods/madison-park/', 'https://seattle.findwell.com/seattle-neighborhoods/madison-valley/', 'https://seattle.findwell.com/seattle-neighborhoods/madrona/', 'https://seattle.findwell.com/seattle-neighborhoods/montlake/', 'https://seattle.findwell.com/seattle-neighborhoods/pioneer-square/', 'https://seattle.findwell.com/seattle-neighborhoods/south-lake-union/', 'https://seattle.findwell.com/seattle-neighborhoods/bryant/', 'https://seattle.findwell.com/seattle-neighborhoods/hawthorne-hills/', 'https://seattle.findwell.com/seattle-neighborhoods/lake-city/', 'https://seattle.findwell.com/seattle-neighborhoods/laurelhurst/', 'https://seattle.findwell.com/seattle-neighborhoods/maple-leaf/', 'https://seattle.findwell.com/seattle-neighborhoods/matthews-beach/', 'https://seattle.findwell.com/seattle-neighborhoods/northgate/', 'https://seattle.findwell.com/seattle-neighborhoods/ravenna/', 'https://seattle.findwell.com/seattle-neighborhoods/roosevelt/', 'https://seattle.findwell.com/seattle-neighborhoods/university-district/', 'https://seattle.findwell.com/seattle-neighborhoods/view-ridge/', 'https://seattle.findwell.com/seattle-neighborhoods/wedgwood/', 'https://seattle.findwell.com/seattle-neighborhoods/windermere/', 'https://seattle.findwell.com/seattle-neighborhoods/ballard/', 'https://seattle.findwell.com/seattle-neighborhoods/blue-ridge-north-beach/', 'https://seattle.findwell.com/seattle-neighborhoods/broadview/', 'https://seattle.findwell.com/seattle-neighborhoods/crown-hill/', 'https://seattle.findwell.com/seattle-neighborhoods/fremont/', 'https://seattle.findwell.com/seattle-neighborhoods/green-lake/', 'https://seattle.findwell.com/seattle-neighborhoods/greenwood/', 'https://seattle.findwell.com/seattle-neighborhoods/haller-lake/', 'https://seattle.findwell.com/seattle-neighborhoods/loyal-heights/', 'https://seattle.findwell.com/seattle-neighborhoods/magnolia/', 'https://seattle.findwell.com/seattle-neighborhoods/blue-ridge-north-beach/', 'https://seattle.findwell.com/seattle-neighborhoods/phinney-ridge/', 'https://seattle.findwell.com/seattle-neighborhoods/queen-anne/', 'https://seattle.findwell.com/seattle-neighborhoods/wallingford/', 'https://seattle.findwell.com/seattle-neighborhoods/westlake/', 'https://seattle.findwell.com/seattle-neighborhoods/whittier-heights/', 'https://seattle.findwell.com/seattle-neighborhoods/beacon-hill/', 'https://seattle.findwell.com/seattle-neighborhoods/columbia-city/', 'https://seattle.findwell.com/seattle-neighborhoods/georgetown/', 'https://seattle.findwell.com/seattle-neighborhoods/mount-baker/', 'https://seattle.findwell.com/seattle-neighborhoods/rainier-beach/', 'https://seattle.findwell.com/seattle-neighborhoods/seward-park/', 'https://seattle.findwell.com/seattle-neighborhoods/south-park/', 'https://seattle.findwell.com/seattle-neighborhoods/west-seattle/', 'https://seattle.findwell.com/seattle-neighborhoods/admiral/', 'https://seattle.findwell.com/seattle-neighborhoods/alki/', 'https://seattle.findwell.com/seattle-neighborhoods/fauntleroy/', 'https://seattle.findwell.com/seattle-neighborhoods/alaska-junction/', 'https://seattle.findwell.com/neighborhood-blogs/', 'https://seattle.findwell.com/greater-seattle/', 'https://seattle.findwell.com/greater-seattle/bellevue/', 'https://seattle.findwell.com/greater-seattle/clyde-hill/', 'https://seattle.findwell.com/greater-seattle/issaquah/', 'https://seattle.findwell.com/greater-seattle/kirkland/', 'https://seattle.findwell.com/greater-seattle/kirkland/houghton/', 'https://seattle.findwell.com/greater-seattle/kirkland/market/', 'https://seattle.findwell.com/greater-seattle/medina/', 'https://seattle.findwell.com/greater-seattle/mercer-island/', 'https://seattle.findwell.com/greater-seattle/newcastle/', 'https://seattle.findwell.com/greater-seattle/redmond/', 'https://seattle.findwell.com/greater-seattle/sammamish/', 'https://seattle.findwell.com/greater-seattle/woodinville/', 'https://seattle.findwell.com/greater-seattle/bothell/', 'https://seattle.findwell.com/greater-seattle/edmonds/', 'https://seattle.findwell.com/greater-seattle/kenmore/', 'https://seattle.findwell.com/greater-seattle/lake-forest-park/', 'https://seattle.findwell.com/greater-seattle/shoreline/', 'https://seattle.findwell.com/greater-seattle/renton/', 'https://seattle.findwell.com/seattle-suburban-blogs/', '/greater-seattle/', 'https://www.zillow.com/howto/api/neighborhood-boundaries.htm', '/seattle-neighborhoods/belltown/', '/seattle-neighborhoods/broadmoor/', '/seattle-neighborhoods/capitol-hill/', '/seattle-neighborhoods/central-district/', '/seattle-neighborhoods/denny-blaine/', '/seattle-neighborhoods/downtown/', '/seattle-neighborhoods/eastlake/', '/seattle-neighborhoods/first-hill/', '/seattle-neighborhoods/international-district/', '/seattle-neighborhoods/leschi/', '/seattle-neighborhoods/madison-park/', '/seattle-neighborhoods/madison-valley/', '/seattle-neighborhoods/madrona/', '/seattle-neighborhoods/montlake/', '/seattle-neighborhoods/pioneer-square/', '/seattle-neighborhoods/south-lake-union/', '/seattle-neighborhoods/bryant/', '/seattle-neighborhoods/hawthorne-hills/', '/seattle-neighborhoods/lake-city/', '/seattle-neighborhoods/laurelhurst/', '/seattle-neighborhoods/maple-leaf/', '/seattle-neighborhoods/matthews-beach/', '/seattle-neighborhoods/northgate/', '/seattle-neighborhoods/ravenna/', '/seattle-neighborhoods/roosevelt/', '/seattle-neighborhoods/university-district/', '/seattle-neighborhoods/view-ridge/', '/seattle-neighborhoods/wedgwood/', '/seattle-neighborhoods/windermere/', '/seattle-neighborhoods/ballard/', '/seattle-neighborhoods/blue-ridge-north-beach/', '/seattle-neighborhoods/broadview/', '/seattle-neighborhoods/crown-hill/', '/seattle-neighborhoods/fremont/', '/seattle-neighborhoods/green-lake/', '/seattle-neighborhoods/greenwood/', '/seattle-neighborhoods/haller-lake/', '/seattle-neighborhoods/loyal-heights/', '/seattle-neighborhoods/magnolia/', '/seattle-neighborhoods/phinney-ridge/', '/seattle-neighborhoods/queen-anne/', '/seattle-neighborhoods/wallingford/', '/seattle-neighborhoods/westlake/', '/seattle-neighborhoods/whittier-heights/', '/seattle-neighborhoods/beacon-hill/', '/seattle-neighborhoods/columbia-city/', '/seattle-neighborhoods/georgetown/', '/seattle-neighborhoods/mount-baker/', '/seattle-neighborhoods/rainier-beach/', '/seattle-neighborhoods/seward-park/', '/seattle-neighborhoods/south-park/', '/seattle-neighborhoods/west-seattle/', '/seattle-neighborhoods/admiral/', '/seattle-neighborhoods/alki/', '/seattle-neighborhoods/fauntleroy/', '/seattle-neighborhoods/alaska-junction/', '/neighborhood-blogs/', 'https://www.findwell.com/real-estate-agents', 'httsp://www.findwell.com/findwell-customer-reviews', 'https://www.findwell.com/what-is-my-home-worth', '/seattle-neighborhoods/', '/cdn-cgi/l/email-protection#543d3a323b14323d3a30233138387a373b39', 'https://www.findwell.com/buy-home-with-findwell', 'https://www.findwell.com/home-buying-guide', 'https://www.findwell.com/sell-home-with-findwell', 'https://www.findwell.com/home-selling-guide', 'https://www.findwell.com/resources', 'https://www.findwell.com/home-buying-class', 'https://www.findwell.com/calculators', 'https://www.findwell.com/mortgage-rates', 'https://www.findwell.com/real-estate-dictionary', 'https://www.findwell.com/real-estate-agents', 'https://www.findwell.com/about', 'https://www.findwell.com/findwell-advantage', 'https://www.findwell.com/real-estate-myth-busters', 'https://www.findwell.com/findwell-customer-reviews', 'https://www.facebook.com/findwell', 'https://twitter.com/findwell', 'https://www.linkedin.com/company/findwell', 'https://www.pinterest.com/findwell/', 'https://instagram.com/findwell', 'https://www.flickr.com/photos/findwell/', '/contact', 'https://www.findwell.com/make-offer', 'https://www.findwell.com/press', 'https://www.findwell.com/careers']
# Stores data for each neighborhood
neighborhoods = []
# Extract data from each neighborhood link
for neighbor_link in range (33, 90):
    url = links[neighbor_link]
    # Temp data storage for one neighborhood
    neighborhood_desc = []
    # request for data from the server using GET
    r = requests.get(url)
    # turn the data into text and use beautiful soup to parse data
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    print(soup.prettify())

    # print the Neighborhood Name
    neighborhood_desc.append((url.split('/')[-2]))

    # Find the description (located before the first h2 tag)
    first_desc = ''
    firstHeader = soup.find('h2')
    prevNode = firstHeader
    # Iterate backwards to get text before the first h2 tag
    while True:
        prevNode = prevNode.previous_sibling
        if prevNode is None:
            break
        elif isinstance(prevNode, bs4.NavigableString):
            # Keep adding valid text data
            first_desc = prevNode.replace("\n", "").replace("\xa0", "") + first_desc
        elif isinstance(prevNode, bs4.Tag):
            # includes the text wrapped in a tags
            if prevNode.name == 'a':
                first_desc = prevNode.string + first_desc
                # break when there is no data break when another h2 or div comes ups in search
            if prevNode.name == '/div' or prevNode.name == 'div':
                break
    neighborhood_desc.append(first_desc)

    # Find text between h2 tags
    for header in soup.find_all('h2'):
        row = []
        row.append(header.get_text())
        nextNode = header
        desc = ''
        while True:
            nextNode = nextNode.next_sibling
            # break when there is no data
            if nextNode is None:
                break
            elif isinstance(nextNode, bs4.NavigableString):
                # Keep adding valid text data
                desc += nextNode.replace("\n", "").replace("\xa0", "")
            elif isinstance(nextNode, bs4.Tag):
                # includes the text wrapped in a tags
                if nextNode.name == 'a':
                    desc += nextNode.string
                    # break when there is no data break when another h2 or div comes ups in search
                if nextNode.name == 'h2' or nextNode.name == '/div' or nextNode.name == 'div':
                    break
        neighborhood_desc.append(desc)

    # Print data to std.out
    cnt = 0
    for element in neighborhood_desc:
        print(cnt, "::: ", element)
        cnt += 1
    neighborhoods.append(neighborhood_desc)

# create the csv file
with open('SeattleNeighborhoods.csv', mode='w') as csv_file:
    fieldnames = ['neighborhood', 'description', 'history', 'vibe', 'activities_attractions']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for desc in neighborhoods:
        writer.writerow({'neighborhood': desc[0],
                         'description': desc[1],
                         'history': desc[2],
                         'vibe': desc[4],
                         'activities_attractions': desc[5]})

