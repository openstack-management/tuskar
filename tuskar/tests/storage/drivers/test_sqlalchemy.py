# -*- encoding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo.db.sqlalchemy import test_base

from tuskar.storage.drivers import sqlalchemy
from tuskar.tests.storage.drivers import base


class SQLAlchemyTestCase(base.BaseDriverTestCase):

    def _get_driver(self):
        return sqlalchemy.SQLAlchemyDriver()


class BaseStoreSQLAlchemyTestCase(SQLAlchemyTestCase, base.BaseStoreMixin):
    pass


class NamedStoreSQLAlchemyTestCase(SQLAlchemyTestCase, base.NamedStoreMixin):
    pass


class VersionStoreSQLAlchemyTestCase(SQLAlchemyTestCase,
                                     base.VersionedStoreMixin):
    pass


class MySQLBaseStoreTestCase(test_base.MySQLOpportunisticTestCase,
                             BaseStoreSQLAlchemyTestCase):
    pass


class MySQLNamedStoreTestCase(test_base.MySQLOpportunisticTestCase,
                              NamedStoreSQLAlchemyTestCase):
    pass


class MySQLVersionedStoreTestCase(test_base.MySQLOpportunisticTestCase,
                                  VersionStoreSQLAlchemyTestCase):
    pass


class PostgreSQLBaseStoreTestCase(test_base.PostgreSQLOpportunisticTestCase,
                                  BaseStoreSQLAlchemyTestCase):
    pass


class PostgreSQLNamedStoreTestCase(test_base.PostgreSQLOpportunisticTestCase,
                                   NamedStoreSQLAlchemyTestCase):
    pass


class PostgreSQLVersionedStoreTestCase(
        test_base.PostgreSQLOpportunisticTestCase,
        VersionStoreSQLAlchemyTestCase):
    pass
