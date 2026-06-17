"""
Capstone Part 2: Customer Lifecycle RFM Segmentation Pipeline
Grounding Date Reference Context: 2025-09-30
"""

import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_rfm_pipeline():
    # ----------------------------------------------------
    # 1. MOCK DATA SETUP (Emulating Raw Structure Natively)
    # ----------------------------------------------------
    np.random.seed(42)
    n_customers = 2400
    customer_ids = [f"CUST{i:05d}" for i in range(1, n_customers + 1)]

    # Orders Base Extraction Dataframe
    n_orders = 12000
    order_dates = pd.date_range(start='2024-01-01', end='2025-11-15', periods=n_orders)
    
    orders_df = pd.DataFrame({
        'order_id': [f"ORD{i:06d}" for i in range(1, n_orders + 1)],
        'customer_id': np.random.choice(customer_ids, n_orders),
        'order_date': order_dates,
        'gross_amount': np.random.uniform(150, 2500, n_orders),
        'discount_pct': np.random.choice([0.0, 0.1, 0.3, 0.5], n_orders, p=[0.4, 0.3, 0.2, 0.1]),
        'returned': np.random.choice([0, 1], n_orders, p=[0.92, 0.08])
    })

    # Inject deliberate duplicate records to match raw data audit requirements
    dup_samples = orders_df.sample(n=50, random_state=42).copy()
    dup_samples['order_id'] = dup_samples['order_id'] + "_DUP"
    orders_df = pd.concat([orders_df, dup_samples], ignore_index=True)

    # Support Tickets Structural Context
    tickets_df = pd.DataFrame({
        'customer_id': np.random.choice(customer_ids, 1500),
        'issue_type': np.random.choice(['product_reaction', 'late_delivery', 'general'], 1500)
    })

    # Web Engagement Activity Context
    web_df = pd.DataFrame({
        'customer_id': customer_ids,
        'sessions_30d': np.random.randint(0, 35, n_customers),
        'product_views_30d': np.random.randint(0, 50, n_customers),
        'cart_adds_30d': np.random.randint(0, 10, n_customers)
    })

    # ----------------------------------------------------
    # 2. DATA CLEANING & LEAKAGE CONTROLS
    # ----------------------------------------------------
    # Filter out duplicate rows marked with the _DUP suffix
    clean_orders = orders_df[~orders_df['order_id'].str.contains('_DUP', na=False)].copy()
    
    # Enforce a strict snapshot date cutoff to prevent future data leakage
    snapshot_date = pd.to_datetime('2025-09-30')
    clean_orders['order_date'] = pd.to_datetime(clean_orders['order_date'])
    historical_orders = clean_orders[clean_orders['order_date'] <= snapshot_date].copy()

    print(f">> Processing {historical_orders.shape[0]} valid historical transactions...")

    # ----------------------------------------------------
    # 3. FEATURE ENGINEERING (RFM + BEHAVIORAL SIGNALS)
    # ----------------------------------------------------
    # Compute base RFM metrics per individual customer profile
    rfm_base = historical_orders.groupby('customer_id').agg(
        Latest_Purchase=('order_date', 'max'),
        Frequency=('order_id', 'count'),
        Monetary=('gross_amount', 'sum'),
        Avg_Discount=('discount_pct', 'mean'),
        Return_Rate=('returned', 'mean')
    ).reset_index()

    rfm_base['Recency'] = (snapshot_date - rfm_base['Latest_Purchase']).dt.days

    # Aggregate behavioral metrics from support ticket history
    ticket_counts = tickets_df.groupby('customer_id').size().reset_index(name='ticket_count')
    reaction_counts = tickets_df[tickets_df['issue_type'] == 'product_reaction'].groupby('customer_id').size().reset_index(name='reaction_count')

    # Merge all metrics into a unified segmentation data table
    master_segments = pd.DataFrame({'customer_id': customer_ids})
    master_segments = master_segments.merge(rfm_base, on='customer_id', how='left').fillna({
        'Recency': 999, 'Frequency': 0, 'Monetary': 0.0, 'Avg_Discount': 0.0, 'Return_Rate': 0.0
    })
    master_segments = master_segments.merge(ticket_counts, on='customer_id', how='left').fillna({'ticket_count': 0})
    master_segments = master_segments.merge(reaction_counts, on='customer_id', how='left').fillna({'reaction_count': 0})
    master_segments = master_segments.merge(web_df, on='customer_id', how='left').fillna(0)

    # ----------------------------------------------------
    # 4. CUSTOM SEGMENTATION SEGMENT ENGINE LOGIC
    # ----------------------------------------------------
    def apply_business_segmentation(row):
        # Unpack clear, human-vetted logic constraints
        rec = row['Recency']
        freq = row['Frequency']
        mon = row['Monetary']
        tickets = row['ticket_count']
        reactions = row['reaction_count']
        disc = row['Avg_Discount']
        views = row['product_views_30d']
        adds = row['cart_adds_30d']

        # Rule Set 1: Champions
        if rec <= 20 and freq >= 5 and mon >= 6000:
            return "Champions"
        
        # Rule Set 2: High-Value At-Risk
        if mon >= 4000 and (rec > 25 or tickets >= 2 or reactions >= 1):
            return "High-Value At-Risk"
        
        # Rule Set 3: Low-Intent Browsers
        if freq <= 1 and views >= 15 and adds <= 1:
            return "Low-Intent Browsers"
        
        # Rule Set 4: Discount-Driven Opportunists
        if disc >= 0.25 and freq >= 2:
            return "Discount-Driven Opportunists"
        
        # Rule Set 5: Hibernating Dormant
        if rec > 60 and freq <= 2:
            return "Hibernating Dormant"
        
        # Catch-All Baseline Segment Assignment
        return "Standard Regular Consumer"

    master_segments['segment_name'] = master_segments.apply(apply_business_segmentation, axis=1)

    # ----------------------------------------------------
    # 5. EXPORT AND REPORT GENERATION
    # ----------------------------------------------------
    # Save the clean assignments directly into segments.csv
    export_columns = [
        'customer_id', 'segment_name', 'Recency', 'Frequency', 
        'Monetary', 'ticket_count', 'Return_Rate', 'product_views_30d'
    ]
    master_segments[export_columns].to_csv('segments.csv', index=False)
    print(">> Successfully generated and exported 'segments.csv'.")

    # Generate and save a verification plot showing the segment distribution
    plt.figure(figsize=(11, 6))
    sns.countplot(
        data=master_segments, 
        y='segment_name', 
        order=master_segments['segment_name'].value_counts().index, 
        palette='Set2'
    )
    plt.title('D2C Customer Base Distribution Across Refined Lifecycle Segments')
    plt.xlabel('Total Customer Population Count')
    plt.ylabel('Identified Strategic Segments')
    plt.savefig('segment_distribution_matrix.png', bbox_inches='tight')
    plt.close()
    print(">> Segmentation verification visualization saved as 'segment_distribution_matrix.png'.")

if __name__ == '__main__':
    run_rfm_pipeline()
