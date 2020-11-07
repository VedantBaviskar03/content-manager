"""Python script to handle data operations on a database."""

import pymongo
from os import environ


"""Creating class Database"""


class Database:
    """Access methods to perform operation on database."""

    myclient = pymongo.MongoClient(environ.get("MONGO_KEY"))
    db = myclient["contentinfo"]
    coll = db["bloginfo"]

    def insert_info(self, name, url, tags):
        """Insert data into dictionary."""
        blog_info = {"Name": name, "URL": url, "Tags": tags}

        inserted_data = self.coll.insert_one(blog_info)
        print(inserted_data.inserted_id, "Was inserted")

    def delete_info(self, user_prompt):
        """Delete entries by deleting the name."""
        user_query = {"Name": user_prompt}
        try:
            self.coll.find_one(user_query)
            print("Entry found...Deleting entry....")
            delete_data = self.coll.delete_one(user_query)
            print(delete_data.deleted_count, "was deleted")

        except:
            print("Your entry", user_prompt, "not found....")

    def search_database(self, user_prompt):
        """Search database to return documents."""
        print("Searching.....")
        if user_prompt.lower() in self.coll.Name.lower():
            print("Data found...Fetching....")
            print(self.coll.find_one(user_prompt))

        else:
            print("Data not present in database...")
