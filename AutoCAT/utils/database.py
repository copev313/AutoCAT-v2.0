import mongoengine as db
from dotenv import load_dotenv
from datetime import datetime as dt
import os
from enum import Enum


class Status(Enum):
    NEW = 'new'
    INPROGRESS = 'in_progress'
    DONE = 'done'


class Vendor(db.Document):
    '''A Vendor data strucure for creating vendor documents.'''
    profile_id = db.StringField(required=True)
    category_id = db.StringField(required=True)
    email = db.EmailField(required=True)
    brand_name = db.StringField(required=True)
    location = db.StringField()
    web_url = db.StringField()
    instagram = db.StringField()
    status = db.EnumField(Status, default=Status.NEW)
    created_at = db.DateTimeField(required=True, default=dt.now)


def add_vendor_to_db(profile_id: str,
                    category_id: str,
                    email: str,
                    brand_name: str,
                    location: str = 'MiddleOf NoWhere',
                    web_url: str = "www.no-url.com",
                    instagram: str = None) -> None:
    '''Adds a new vendor document to our MongoDB 'vendors' collection.'''
    try:
        load_dotenv()
        db.connect(host=os.environ.get('MONGO_HOST'))
        vendor = Vendor(profile_id=profile_id,
                        category_id=category_id,
                        email=email,
                        brand_name=brand_name,
                        location=location,
                        web_url=web_url,
                        instagram=instagram)
        vendor.save()
    except Exception as e:
        print(e)
    finally:
        db.disconnect()
        print('Vendor saved to MongoDB!')
