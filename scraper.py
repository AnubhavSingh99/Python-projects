import requests
from bs4 import BeautifulSoup
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url : str)-> dict:
    product_details={}
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features="lxml")
    
    try:
        # Extract title
        title_element = soup.find('span', attrs={'id': 'productTitle'})
        if title_element:
            title = title_element.get_text().strip()
            product_details['title'] = title
        else:
            product_details['title'] = "Title not found"
        
        # Try multiple price selectors
        price = None
        price_selectors = [
            # Common Amazon price selectors
            {'tag': 'span', 'attrs': {'class': 'a-price-whole'}},
            {'tag': 'span', 'attrs': {'class': 'a-offscreen'}},
            {'tag': 'span', 'attrs': {'id': 'priceblock_ourprice'}},
            {'tag': 'span', 'attrs': {'id': 'priceblock_dealprice'}},
            {'tag': 'span', 'attrs': {'class': 'a-price a-text-price a-size-medium apexPriceToPay'}},
            {'tag': 'span', 'attrs': {'class': 'a-price-range'}},
        ]
        
        for selector in price_selectors:
            price_element = soup.find(selector['tag'], selector['attrs'])
            if price_element:
                price_text = price_element.get_text().strip()
                # Clean up the price text
                if '$' in price_text:
                    # Extract price using different methods
                    if price_text.startswith('$'):
                        price = price_text
                    else:
                        # Try to find the price within the text
                        import re
                        price_match = re.search(r'\$[\d,]+\.?\d*', price_text)
                        if price_match:
                            price = price_match.group()
                    break
        
        # If still no price found, try a broader search
        if not price:
            # Look for any element containing price-like pattern
            price_elements = soup.find_all(text=lambda text: text and '$' in str(text))
            for element in price_elements:
                text = str(element).strip()
                if text.startswith('$') and len(text) < 20:  # Simple price format
                    import re
                    if re.match(r'^\$[\d,]+\.?\d*$', text):
                        price = text
                        break
        
        product_details['price'] = price if price else "Price not found"
        product_details['url'] = product_url
        return product_details
        
    except Exception as e:
        print("Could not fetch details")
        print(f"Error extracting product details: {e}")
        return {
            'title': 'Error fetching title',
            'price': 'Error fetching price', 
            'url': product_url
        }

product_url=input("Enter the product URL: ")
product_details = get_product_details(product_url)
print(product_details)