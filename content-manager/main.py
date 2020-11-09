"""Python script to handle data operations on a database."""

import pymongo
from os import environ


"""Creating class Database"""


class Database:
    """Access methods to perform operation on database."""

    myclient = pymongo.MongoClient(environ.get("MONGO_URL"))
    db = myclient["contentinfo"]
    coll = db["bloginfo"]

    def insert_info(self, name, username, email, url, tags,):
        """Insert data into dictionary."""
        blog_info = {"Name": name, "Username": username, "E-mail": email, "URL": url, "Tags": tags}

        inserted_data = self.coll.insert_one(blog_info)
        return {"Success": "{} Was inserted".format(inserted_data.inserted_id)}

    def delete_info(self, user_prompt):
        """Delete entries by deleting the name."""
        user_query = {"Name": user_prompt}
        try:
            self.coll.find_one(user_query)
            print("Entry found...Deleting entry....")
            deleted_data = self.coll.delete_one(user_query)
            return {"Success": "{} entry was deleted".format(deleted_data.deleted_count)}

        except Exception:
            return {"Failure": "{} not found".format(user_query)}

    def get_info(self):
        """Get all user info"""
        entries = [entry for entry in self.coll.find({})]

        # Make the ObjectId a string
        for entry in entries:
            entry["_id"] = str(entry["_id"])

        return entries

    def search_database(self, user_prompt):
        """Search database to return documents."""
        print("Searching.....")
        user_query = {"Name": user_prompt}
        find_name = self.coll.find(user_query)
        if find_name is True:
            for x in find_name:
                return x

        else:
            return {"Entry": "{} not found ".format(user_query)}

    def update_database(self, name, changes={}):
        """Match the user by using the username and write the changes."""
        allowed_keys = ["Username", "E-mail", "URL", "Tags"]

        unknown_keys = set(changes.keys()) - set(allowed_keys)

        if unknown_keys:
            return {"detail": "{}: not allowed".format(unknown_keys)}

        try:
            r = self.coll.update_one({"Name": name}, {"$set": changes})
            return {"_id": r.upserted_id}
        except Exception:
            return {"detail": "Something went wrong"}
