import pandas as pd
from pymongo import MongoClient
import time
from urllib.parse import quote_plus

def generate_excel_from_mongo(mongo_uri, db_name, output_excel="mongodb_analysis_report.xlsx"):
    """
    Connect to MongoDB, fetch collection stats and generate an Excel file.
    """
    print(f"Mongo URI: {mongo_uri}")  # Debugging line to check the URI
    client = MongoClient(mongo_uri)
    db = client[db_name]
    
    collections = db.list_collection_names()
    
    data = []
    for collection in collections:
        coll = db[collection]
        
        # Use db.command('collstats', collection_name) to get stats for the collection
        stats = db.command('collstats', collection)
        
        collection_data = {
            "Collection Name": collection,
            "Document Count": stats['count'],
            "Collection Size (MB)": stats['size'] / (1024 * 1024),  # size in MB
            "Avg Doc Size (KB)": stats['avgObjSize'] / 1024 if 'avgObjSize' in stats else 0,
            "Index Count": len(coll.index_information()) if 'indexCount' in stats else 0,
            "Query Time (s)": stats.get('queryTime', 'N/A')  # Assuming 'queryTime' is available
        }
        data.append(collection_data)
    
    df = pd.DataFrame(data)
    
    # Save the data to an Excel file
    df.to_excel(output_excel, index=False)
    print(f"Excel report generated: {output_excel}")
    return output_excel


if __name__ == "__main__":
    # Hardcode MongoDB URI and Database Name
    mongo_uri = ""
    db_name = "kev_test"
    
    # Step 1: Generate Excel report from MongoDB
    print("Generating Excel report from MongoDB...")
    excel_file = generate_excel_from_mongo(mongo_uri, db_name)
    print(f"Excel file saved as: {excel_file}")
