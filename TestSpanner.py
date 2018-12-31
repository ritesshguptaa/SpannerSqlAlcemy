#!/usr/bin/env python


import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import argparse
from google.cloud import spanner
from google.cloud.spanner_v1 import param_types






def main():

    Base = declarative_base()

    #requests_toolbelt.adapters.appengine.monkeypatch()
 
    class Person(Base):
        __tablename__ = 'person'
        # Here we define columns for the table person
        # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
     
    class Address(Base):
        __tablename__ = 'address'
        # Here we define columns for the table address.
        # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        street_name = Column(String(250))
        street_number = Column(String(250))
        post_code = Column(String(250), nullable=False)
        person_id = Column(Integer, ForeignKey('person.id'))
        person = relationship(Person)
     

    

    spanner_client = spanner.Client()
    print('Connecting Test instance')
    instance = spanner_client.instance("Test Instance")
    print('Connecting the database')
    database = instance.database("example-db")

    print('creating engine')

    #engine = create_engine('sqlite:///sqlalchemy_example.db')
    #engine = create_engine('mysql+gaerdbms:///example-db?instance:neon-implement-226714:Test Instance' )

    # This is code to connect db in cloud for debugging and understaning purpose
    # probably similar code is required for spanner
    engine = create_engine('mysql+mysqldb://root@/example-db?unix_socket=/spanner/neon-implement-226714:Test Instance', pool_pre_ping=True)
    
    #mysql+mysqldb://root@/<dbname>?unix_socket=/cloudsql/<projectid>:<instancename>
    ##engine = create_engine('mysql+gaerdbms:///example-db', connect_args={"instance":'Test Instance'} )

    print('creating connection')

    connection = engine.connect()

    print('creating session')

    DBSession = sessionmaker()

    


    







if __name__ == '__main__':
    main()
