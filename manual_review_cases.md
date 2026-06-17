# Edge Case Manual Review Log: Complex Customer Decisions
Grounded strictly in operational profiles where standard RFM scoring fails to reveal the true retention path.

### 1. Customer ID: CUST00142 (The Conflicted Advocate)
* **Data Indicators:** Recency: 4 days, Frequency: 12 orders, Monetary: ₹18,450, Support Tickets: 3 (all categorized under `product_reaction` within the last 7 days).
* **The Conflict:** Standard RFM tags this customer as a "Champion" due to high spend and recent orders, but the support logs show severe product delivery or reaction friction.
* **Resolution:** **Do Not Automate.** Exclude them from upcoming promotional loops. Have an executive customer support manager call them directly to resolve the product issue, issue a full refund, and offer a dermatologist-vetted alternative product.

### 2. Customer ID: CUST00489 (The Disengaged High Spender)
* **Data Indicators:** Recency: 58 days, Frequency: 14 orders, Monetary: ₹22,100, App Sessions (30d): 32, Cart Adds (30d): 0.
* **The Conflict:** They look like they are churning based on their 58-day purchase silence, but their high app log-ins (32 sessions) show they are still actively browsing our app.
* **Resolution:** They want to buy but are hitting a friction point (e.g., out-of-stock items, price increases, or missing features). Send a targeted survey or a personal email asking for product feedback, rather than a generic discount code.

### 3. Customer ID: CUST00711 (The High-Cost Returner)
* **Data Indicators:** Recency: 12 days, Frequency: 9 orders, Monetary: ₹14,200, Return Rate: 78%.
* **The Conflict:** High RFM metrics suggest a valuable customer, but their extreme return rate means they are actually costing the company money in return shipping and logistics.
* **Resolution:** Stop sending them high-discount offers or broad promotions. Route them to a feedback email asking about their fit or product satisfaction issues to fix the high return rate.

### 4. Customer ID: CUST00923 (The Promotion Dependent Spender)
* **Data Indicators:** Recency: 3 days, Frequency: 5 orders, Monetary: ₹9,800, Average Discount Usage: 72%.
* **The Conflict:** Recent and frequent purchasing history, but they only buy when deep discounts are applied, making them unprofitable under standard marketing campaigns.
* **Resolution:** Do not send them standard sitewide coupons. Only include them in automated clearance loops to move excess inventory without eating into regular product margins.

### 5. Customer ID: CUST01104 (The Silent Ticket Submitter)
* **Data Indicators:** Recency: 85 days, Frequency: 2 orders, Monetary: ₹1,800, Support Tickets: 1 (`late_delivery` with a long resolution time of 74 hours).
* **The Conflict:** Their low RFM metrics look like a standard dormant account, but their churn was clearly triggered by a bad shipping experience.
* **Resolution:** Do not treat them as standard inactive users. Send a dedicated "We've fixed our logistics" note along with a credit toward their next order to make up for the delivery delay.

### 6. Customer ID: CUST01355 (The Sudden Category Switcher)
* **Data Indicators:** Frequency: 8 orders, Historical preferred category: "Skin Care", Recent 30-day views: 100% focused on "Baby Care".
* **The Conflict:** Standard segment models will keep sending them skincare ads based on historical data, missing their recent shift in shopping intent.
* **Resolution:** Update their profile tags manually to prioritize "Baby Care" collections, ensuring upcoming emails match their current lifestyle needs.

### 7. Customer ID: CUST01640 (The Window Shopper)
* **Data Indicators:** Recency: 120 days, Total Orders: 1, App Sessions (Last 30 days): 45, Wishlist Adds: 18.
* **The Conflict:** They are technically a dormant, single-purchase account, but their high browse volume and wishlist updates show strong ongoing brand interest.
* **Resolution:** Send a highly personalized email highlighting the specific items currently sitting in their wishlist, paired with a small incentive to help them complete their second purchase.

### 8. Customer ID: CUST01812 (The Institutional/B2B Outlier)
* **Data Indicators:** Recency: 14 days, Frequency: 3 orders, Monetary: ₹74,500.
* **The Conflict:** Their massive spending habits skew our retail consumer models, indicating they are likely a wholesale or B2B buyer rather than a typical D2C customer.
* **Resolution:** Move this account out of standard consumer marketing tracks entirely and hand them off to a dedicated B2B account team.

### 9. Customer ID: CUST02001 (The Multi-Channel Abandoner)
* **Data Indicators:** App Sessions: 22, Cart Adds: 4, Email Opens: 0%, Push Notification Clicks: 100%.
* **The Conflict:** They are highly active inside our app but completely ignore our email marketing campaigns.
* **Resolution:** Stop wasting marketing spend on email channels for this user. Shift all outreach efforts to in-app pop-ups and push notifications where they are actively engaging.

### 10. Customer ID: CUST02239 (The High-Sentiment Churner)
* **Data Indicators:** Recency: 95 days, Frequency: 6 orders, Average Customer Satisfaction Rating: 5/5 stars.
* **The Conflict:** They consistently left perfect reviews on past orders but have suddenly stopped buying completely for over 90 days.
* **Resolution:** This usually points to catalog fatigue or an unresolved service issue. Send a soft re-engagement note featuring newly launched product lines to spark renewed interest.
