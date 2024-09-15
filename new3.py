import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapws(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    reviews = []

    reelements = soup.find_all('div', class_='review')  
    
    for review in reelements:
        reviewer = review.find('span', class_='reviewer-name').text.strip()  
        rating = review.find('span', class_='review-rating').text.strip() 
        review_text = review.find('p', class_='review-text').text.strip() 
        
        reviews.append({
            'Reviewer': reviewer,
            'Rating': rating,
            'Review': review_text
        })
    
    return reviews

def main():
    base_url = 'https://example-ecommerce-site.com/product-reviews?page='
    all_reviews = []
    
    for page in range(1, 6): 
        url = base_url + str(page)
        reviews = scrapws(url)
        all_reviews.extend(reviews)
 
    df = pd.DataFrame(all_reviews)
    df.to_csv('customer_reviews.csv', index=False)
    print('Reviews saved to customer_reviews.csv')

if __name__ == "__main__":
    main()