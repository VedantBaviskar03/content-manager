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

    def update_database(self, username, changes={}):
        """Match the user by using the username and write the changes."""
        allowed_keys = ["name", "email", "url", "tags"]

        unknown_keys = allowed_keys - list(changes.keys())

        if unknown_keys:
            return {"detail": "{}: not allowed".format(unknown_keys)}

        try:
            r = self.coll.update_one({"username": username}, {"$set": changes})
            return r
        except Exception:
            return {"detail": "Something went wrong"}
